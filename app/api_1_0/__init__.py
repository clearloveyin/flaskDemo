from flask import Blueprint
# 创建蓝图,取名和给模块取名
api = Blueprint('api_1_0', __name__)
# 把要写的模块导入(注意:导在下面是为了循环导入)
from . import test_api


