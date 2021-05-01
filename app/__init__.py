from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
#from config import SQLite, PostgreSQL
import os


app = Flask(__name__)

'''
dbtype = os.environ.get('DB_TYPE')
if not dbtype or dbtype == 'SQLite':
    app.config.from_object(SQLite)
elif dbtype and dbtype == 'PostgreSQL':
    app.config.from_object(PostgreSQL)
'''

login = LoginManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes