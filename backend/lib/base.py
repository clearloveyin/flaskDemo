import functools
import asyncio
import traceback
from flask import current_app, request
from flask_restful import Resource, abort
from pydantic import ValidationError
from .exceptions import UserError
from .constants import ErrorCodeEnum
from backend.utils import json_dumps, json_loads
from .. import db


def error_interceptor(view_func):
    """错误拦截器"""
    @functools.wraps(view_func)
    async def wrapper(*args, **kwargs):
        try:
            result = await view_func(*args, **kwargs)
            return result
        except Exception as e:
            db.session.rollback()
            current_app.logger.info(e, {'http_code': 200})
            if isinstance(e, UserError):
                return BaseResource.fail(e.message, e.status_code)
            else:
                traceback.print_exc()
                return BaseResource.fail("服务器异常", ErrorCodeEnum.SERVER_ERROR)
    return wrapper


class BaseResource(Resource):
    def __init__(self, *args, **kwargs):
        super(BaseResource, self).__init__(*args, **kwargs)
        self._user = None

    def dispatch_request(self, *args, **kwargs):
        method = request.method.lower()
        meth = getattr(self, method, None)
        if meth is None or not callable(meth):
            return super().dispatch_request(*args, **kwargs)

        schema = getattr(self, f'{method}_schema', None)
        if schema:
            arguments = dict()
            try:
                arguments.update(request.json)
            except Exception:
                pass
            try:
                arguments.update(request.args)
            except Exception:
                pass
            try:
                arguments.update(request.form)
            except Exception:
                pass
            try:
                kwargs['data'] = schema(**arguments)
            except ValidationError as e:
                return self.fail(["type: {}, loc: {}, msg: {}.".format(i['type'], i['loc'], i['msg']) for i in e.errors()],
                                 ErrorCodeEnum.VALIDATION_ERROR)
            except UserError as e:
                return self.fail(e.message, e.status_code)

        if asyncio.iscoroutinefunction(meth):
            return asyncio.run(meth(*args, **kwargs))
        else:
            return meth(*args, **kwargs)

    @staticmethod
    def done(result=None):
        # current_app.logger.info('', {'http_code': 200, 'status_code': 200})
        if result is None:
            result = {}
        return json_loads(json_dumps({"success": True, "data": result}))

    @staticmethod
    def pagination_done(result, **kwargs):
        # current_app.logger.info('', {'http_code': 200, 'status_code': 200})
        data, pagination_dict = result
        res = dict()
        res["dataList"] = data
        res["paginationMeta"] = pagination_dict
        for k in kwargs:
            res[k] = kwargs[k]
        return json_loads(json_dumps({"success": True, "data": res}))

    @staticmethod
    def fail(message, error_code):
        # current_app.logger.error(message, {'http_code': 200, 'status_code': error_code}, exc_info=True)
        return {"success": False, "error_code": error_code, "message": message}


def json_response(response):
    return current_app.response_class(json_dumps(response), mimetype="application/json")

