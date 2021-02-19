import os

class Config:
	"""This class defines environment-specific configuration variables"""
	SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	DEBUG = True
