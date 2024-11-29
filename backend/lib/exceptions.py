from .constants import ErrorCodeEnum


class WebException(Exception):
    status_code = 400


class ApiError(WebException):
    """
    用户操作错误
    """
    status_code = 400

    def __init__(self, message, status_code=None, payload=None, user_id=None):
        """
        :param message: 错误消息
        :param status_code: 错误代号
        :param payload: 错误数据
        :return:
        """
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code or self.status_code
        self.payload = payload
        if user_id:
            self.user_id = user_id

    def as_dict(self):
        rv = dict(self.payload or ())
        rv['success'] = False
        rv['message'] = self.message
        rv['code'] = self.status_code
        return rv


class UserError(ApiError):
    """
    用户操作接口错误
    """
    status_code = ErrorCodeEnum.USER_ERROR


class ApiVerError(ApiError):
    """
    接口版本异常
    """
    status_code = 30400
