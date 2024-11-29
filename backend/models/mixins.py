from .base import Column, db, primary_key
from backend.lib.constants import STATUS


class TimestampMixin(object):
    update_time = Column(db.DateTime(True), default=db.func.now(), onupdate=db.func.now(), nullable=False, comment='更新时间')
    create_time = Column(db.DateTime(True), default=db.func.now(), nullable=False, comment='创建时间')


class StatusMixin(object):
    status = db.Column(db.Integer, default=STATUS.NORMAL, comment='状态')


class DbBaseModel(db.Model):
    __abstract__ = True

    id = primary_key()

    def to_dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = getattr(self, column.name)
        return d
