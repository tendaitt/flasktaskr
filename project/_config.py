import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True
SECRET_KEY = 'b_\xa2\x85\xde\x8djL[u\xa5\xb1T\xcaIXgi\xf3\xd4u<9?\xcf'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = False