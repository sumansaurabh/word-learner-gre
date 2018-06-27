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

	word = Words(word=word, meaning=meaning)
	print(word)
	config.db.session.add(word)
	config.db.session.commit()

	return jsonify({'hello': "I am your coffee"})


@api.route('/api/fetch', methods=['GET'])
@jsonify_resp
def get_word_list():
	"""Checkk authentication flow"""

	word_list=BuildQuestions.fetch_words(10)
	return {"data": word_list}, 200
	

	

	return jsonify({'hello': "I am your coffee"})


