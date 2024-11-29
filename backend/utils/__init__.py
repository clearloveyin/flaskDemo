import binascii
import datetime
import decimal
import json
import random
import uuid
import simplejson
from sqlalchemy.orm.query import Query


def generate_token(length):
    chars = "abcdefghijklmnopqrstuvwxyz" "ABCDEFGHIJKLMNOPQRSTUVWXYZ" "0123456789"

    rand = random.SystemRandom()
    return "".join(rand.choice(chars) for x in range(length))


class JSONEncoder(simplejson.JSONEncoder):
    """Adapter for `simplejson.dumps`."""

    def default(self, o):
        # Some SQLAlchemy collections are lazy.
        if isinstance(o, Query):
            result = list(o)
        elif isinstance(o, decimal.Decimal):
            result = float(o)
        elif isinstance(o, (datetime.timedelta, uuid.UUID)):
            result = str(o)
        # See "Date Time String Format" in the ECMA-262 specification.
        elif isinstance(o, datetime.datetime):
            result = o.strftime("%Y-%m-%d %H:%M:%S")
            # if o.microsecond:
            #     result = result[:23] + result[26:]
            # if result.endswith("+00:00"):
            #     result = result[:-6] + "Z"
        elif isinstance(o, datetime.date):
            result = o.isoformat()
        elif isinstance(o, datetime.time):
            if o.utcoffset() is not None:
                raise ValueError("JSON can't represent timezone-aware times.")
            result = o.isoformat()
            if o.microsecond:
                result = result[:12]
        elif isinstance(o, memoryview):
            result = binascii.hexlify(o).decode()
        elif isinstance(o, bytes):
            result = binascii.hexlify(o).decode()
        else:
            result = super(JSONEncoder, self).default(o)
        return result


def json_loads(data, *args, **kwargs):
    """A custom JSON loading function which passes all parameters to the
    json.loads function."""
    return json.loads(data, *args, **kwargs)


def json_dumps(data, *args, **kwargs):
    """A custom JSON dumping function which passes all parameters to the
    json.dumps function."""
    kwargs.setdefault("cls", JSONEncoder)
    kwargs.setdefault("ensure_ascii", False)
    # Float value nan or inf in Python should be render to None or null in json.
    # Using allow_nan = True will make Python render nan as NaN, leading to parse error in front-end
    kwargs.setdefault("allow_nan", False)
    return json.dumps(data, *args, **kwargs)


def get_remaining_seconds(end_time: datetime.datetime):
    """结束倒计时，单位秒"""
    if not end_time:
        return 0
    now = datetime.datetime.now()
    # 计算剩余时间
    remaining_time = end_time - now
    # 将时间差转换为秒
    remaining_seconds = int(remaining_time.total_seconds())
    return remaining_seconds if remaining_seconds > 0 else 0


def format_price(price):
    """去除小数点后边的0"""
    return int(price) if price == int(price) else price
