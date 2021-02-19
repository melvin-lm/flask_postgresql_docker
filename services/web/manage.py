from flask import Flask
from database import db

def create_app():
	app = Flask(__name__)
	app.config.from_object("config.Config")
	app.app_context().push()
	db.init_app(app)
	return app

def init_db():
	db.create_all()

	

