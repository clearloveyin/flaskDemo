from flask_restful import Api
from flask import Blueprint
from backend.app.demo.api import DemoApi

bp = Blueprint('api', __name__, url_prefix='')
api = Api(bp)
# demo
api.add_resource(DemoApi, "/demo")


def init_app(app):
    app.register_blueprint(bp)
