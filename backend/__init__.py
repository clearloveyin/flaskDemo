from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from .models import db

app = Flask(__name__)
CORS(app, supports_credentials=True)
migrate = Migrate(compare_type=True, include_schemas=True)


@app.cli.command()
def initialize():
    # 初始化数据
    from lib.initialize import Initialize
    Initialize()
