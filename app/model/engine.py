from sqlalchemy import create_engine
from app.app import app

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
connection = engine.connect()
