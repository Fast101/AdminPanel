from flask import Flask, render_template, request, redirect, url_for, flash, g
app = Flask(__name__)
app.secret_key = 'enter secret key'
from flask import session

from database_setup import *

from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
dbsession = DBSession()

if __name__ == '__main__':
	app.run(debug=True, threaded=True)