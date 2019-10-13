# 管理文件
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
import logging

from app import create_app, db

app = create_app('development')

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.route('/test', methods=['get'])
def index():

    return '这是测试页面'


if __name__ == '__main__':
    manager.run()
