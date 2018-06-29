# -*- coding: utf-8 -*-
"""
routes.api.py
~~~~~~

:copyright: (c) 2014
"""
from flask import (Blueprint, current_app, render_template,
				   request, send_from_directory, jsonify)

from Models.Words import Words
import flask
import requests
from services import BuildQuestions
from datetime import datetime, timedelta
import config
from Base_controller import login_required, jsonify_resp
import logging																																										
import sys


api = Blueprint('api', __name__)

@api.route('/api/add', methods=['POST'])
def add_word():
	"""Checkk authentication flow"""
	data = request.json

	word = data["word"]
	meaning = data["meaning"]
	word_type=data["word_type"]

	word = Words(word=word, meaning=meaning, word_type=word_type)
	print(word)
	config.db.session.add(word)
	config.db.session.commit()

	return jsonify({'hello': "I am your coffee"})


@api.route('/api/<word_type>/fetch', methods=['GET'])
@jsonify_resp
def get_word_list(word_type):
	"""Checkk authentication flow"""
	print("##################")
	print("word word_type->",word_type)

	word_list=BuildQuestions.fetch_words(word_type, 10)
	return {"data": word_list}, 200

@api.route('/api/<word_type>/fetch_limited/<limit>', methods=['GET'])
@jsonify_resp
def get_limited_word_list(word_type, limit):
	"""Checkk authentication flow"""

	word_list=BuildQuestions.fetch_limited_question(word_type, limit)
	return {"data": word_list}, 200
	

@api.route('/api/submit', methods=['POST'])
@jsonify_resp
def submit_word():
	"""Checkk authentication flow"""

	data=request.json

	print(data)

	if data['state']=="CORRECT":
		config.db.session.query(Words).filter_by(word=data['word']).update({"attempts": Words.attempts+1, "correct":Words.correct+1, "last_appeared": datetime.now()})
	else:
		config.db.session.query(Words).filter_by(word=data['word']).update({"attempts": Words.attempts+1, "last_appeared": datetime.now()})
	
	config.db.session.commit()

	data=BuildQuestions.get_average_score(data['word_type'])


	
	return {'data': data}, 200

@api.route('/api/<word_type>/average_score', methods=['GET'])
@jsonify_resp
def get_average_score(word_type):
	"""Checkk authentication flow"""

	data=BuildQuestions.get_average_score(word_type)


	
	return {'data': data}, 200


@api.route('/api/ignore_word', methods=['POST'])
@jsonify_resp
def ignore_word():
	"""Checkk authentication flow"""

	data=request.json

	print(data)

	config.db.session.query(Words).filter_by(word=data['word']).update({"status": -1})
	config.db.session.commit()
	
	return {'data': data}, 200


@api.route('/api/<word_type>/allWords', methods=['GET'])
@jsonify_resp
def all_words(word_type):
	"""Checkk authentication flow"""

	words=[]
	data=config.db.session.query(Words).filter_by(word_type=word_type).all()
	not_attempted=0
	ignored_word=0
	for itm in data:
		# print(itm)
		if itm.attempts==0:
			not_attempted+=1
		if itm.status==-1:
			ignored_word+=1

		words.append(itm.__dict())

	
	return {'data': words, "not_attempted": not_attempted, "ignored_word": ignored_word}, 200

