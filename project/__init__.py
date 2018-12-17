from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = flask(__name__)
app.config.from_pyfile('_config.py')
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from prject.tasks.views import tasks_blueprint

# Register out blueprints
app.register_blueprint(users_blueprint)
aoo.register_blueprint(tasks_blueprint)
