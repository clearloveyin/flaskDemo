import functools
from collections import defaultdict
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import object_session
from backend import settings
from backend.utils import json_dumps, json_loads


class APPSQLAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        options.update(json_serializer=json_dumps)
        return super(APPSQLAlchemy, self).apply_driver_hacks(app, info, options)


db = APPSQLAlchemy(
    session_options={"expire_on_commit": False},
    engine_options={"json_serializer": json_dumps, "json_deserializer": json_loads},
)
db.configure_mappers()


Column = functools.partial(db.Column, nullable=True)


def pagination(q_base, page: int, per_page: int):
    """分页方法"""
    pagination_dict = dict()
    if page and per_page:
        q_base = q_base.paginate(page=page, per_page=per_page, error_out=False)
        q_all = q_base.items
        pagination_dict['currentPage'] = q_base.page
        pagination_dict['nextPage'] = q_base.next_num
        pagination_dict['perPage'] = q_base.per_page
        pagination_dict['previousPage'] = q_base.prev_num
        pagination_dict['totalCount'] = q_base.total
        pagination_dict['totalPages'] = q_base.pages
    else:
        q_all = q_base.all()
    return q_all, pagination_dict
