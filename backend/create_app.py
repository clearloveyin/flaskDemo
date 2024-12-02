import os
import re
import warnings
from backend import app, db, migrate


def create_app():
    flask_env = os.getenv('FLASK_CONFIG') or 'development'
    app.config.from_object('backend.settings.common')
    app.config.from_object('backend.settings.%s' % flask_env)
    import_env(app.config['ENV_FILE'])
    db.init_app(app)
    migrate.init_app(app, db)
    from . import router
    router.init_app(app)
    return app


def import_env(env_file):
    if not os.path.exists(env_file):
        warnings.warn("can't read {0} - it doesn't exist".format(env_file))
    else:
        with open(env_file, "r") as f:
            for line in f:
                try:
                    line = line.lstrip()
                    key, value = line.strip().split('=', 1)
                except ValueError:
                    pass
                else:
                    app.config[key] = re.sub(r"\A[\"']|[\"']\Z", "", value)
