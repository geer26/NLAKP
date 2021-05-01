from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
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

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

#login = LoginManager(app)

#db = SQLAlchemy(app)
#migrate = Migrate(app, db)

from app import routes