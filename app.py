"""This sample is published as part of the blog article at www.toptal.com/blog
Visit www.toptal.com/blog and subscribe to our newsletter to read great posts
"""
import json
import os
import sys
import flask
import jwt
import requests
import config
from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from jwt import DecodeError, ExpiredSignature
from routes.api import api
from routes.home import home
from Models.Base import Base

LIST_MODULES = [api, home]
template_dir = os.path.abspath('./static/dist/')
app = Flask(__name__, template_folder=template_dir)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iq_deployment.db'
app.config['FACEBOOK_SECRET'] = os.environ.get('FACEBOOK_SECRET')

config.db = SQLAlchemy(app)




@app.before_first_request
def setup():
    # Recreate database each time for demo

    print("sdglknsdbksdnbjkndskbndsknbkn --------- ")
    # Base.metadata.drop_all(bind=config.db.engine)
    Base.metadata.create_all(bind=config.db.engine)
    # config.db.session.add(User('Bob Jones', 'bob@gmail.com'))
    # config.db.session.add(User('Joe Quimby', 'eat@joes.com'))
    config.db.session.commit()


def initialize_app(app=app, config_cls='Default'):
	"""
	Compose the dependencies and initialize the Flask app.

	:param app:Existing flask object
	:param config_cls:Flask config class
	:return:
	"""
	try:
		config_cls = getattr(config, config_cls)
		app.config.from_object(config_cls)
	except AttributeError:
		traceback = sys.exc_traceback
		raise (AttributeError, "Config class '%s' does not exist in app.config module" % config_cls,
			   traceback)
	for module in LIST_MODULES:
		app.register_blueprint(module)


@app.context_processor
def context_processor():
	"""
	Context processors run before the template is rendered and have
	the ability to inject new values into the template context.
	A context processor is a function that returns a dictionary.
	"""
	inject_object = dict(base_url=request.base_url,
					   url_root=request.url_root)
	return inject_object


manager = Manager(app)


@manager.command
def run(address='0.0.0.0', port='5000', config='Default'):
	"""Run development server"""
	setup()
	initialize_app(app, config_cls=config)
	app.run(host=address, port=int(port))


if __name__ == '__main__':
	manager.run()










































"""

@app.route('/auth/signup', methods=['POST'])
def signup():
	data = request.json

	email = data["email"]
	password = data["password"]

	user = User(email=email, password=password)
	db.session.add(user)
	db.session.commit()

	return jsonify(token=user.token())


@app.route('/auth/login', methods=['POST'])
def login():
	data = request.json

	email = data.get("email")
	password = data.get("password")

	user = User.query.filter_by(email=email).first()
	if not user:
		return jsonify(error="No such user"), 404

	if user.password == password:
		return jsonify(token=user.token()), 200
	else:
		return jsonify(error="Wrong email or password"), 400


@app.route('/user')
def user_info():
	if not request.headers.get('Authorization'):
		return jsonify(error='Authorization header missing'), 401

	token = request.headers.get('Authorization').split()[1]
	try:
		payload = jwt.decode(token, app.config['TOKEN_SECRET'])
	except DecodeError:
		return jsonify(error='Invalid token'), 401
	except ExpiredSignature:
		return jsonify(error='Expired token'), 401
	else:
		user_id = payload['sub']
		user = User.query.filter_by(id=user_id).first()
		if user is None:
			return jsonify(error='Should not happen ...'), 500

		return jsonify(id=user.id, email=user.email), 200

	return jsonify(error="never reach here..."), 500


@app.route('/auth/facebook', methods=['POST'])
def auth_facebook():
	access_token_url = 'https://graph.facebook.com/v2.8/oauth/access_token'
	graph_api_url = 'https://graph.facebook.com/v2.8/me?fields=id,email'

	params = {
		'client_id': request.json['clientId'],
		'redirect_uri': request.json['redirectUri'],
		'client_secret': app.config['FACEBOOK_SECRET'],
		'code': request.json['code']
	}

	# Exchange authorization code for access token.
	r = requests.get(access_token_url, params=params)
	# use json.loads instad of urlparse.parse_qsl
	access_token = json.loads(r.text)

	# Step 2. Retrieve information about the current user.
	r = requests.get(graph_api_url, params=access_token)
	profile = json.loads(r.text)

	# Step 3. Create a new account or return an existing one.
	user = User.query.filter_by(facebook_id=profile['id']).first()
	if user:
		return jsonify(token=user.token())

	u = User(facebook_id=profile['id'], email=profile['email'])
	db.session.add(u)
	db.session.commit()
	return jsonify(token=u.token())


@app.route('/islive')
def islive():
	return "it's live"


@app.route('/')
def index():
	return flask.redirect('/static/index.html')


if __name__ == '__main__':
	app.run(debug=True, port=5002, host='0.0.0.0')
"""