# -*- coding: utf-8 -*-
# @Author: perfectus
# @Date:   2018-06-27 20:45:28
# @Last Modified by:   sumansaurabh
# @Last Modified time: 2018-06-29 23:17:18

import config
from Models.Words import Words
from datetime import datetime, timedelta
import random
from  sqlalchemy.sql.expression import func, select
from sqlalchemy.sql import label



def fetch_limited_question(word_type, n):

	word_list=[]
	other_time = datetime.now() - timedelta(hours=1)
	new_words=config.db.session.query(Words).filter_by(word_type=word_type).filter(Words.last_appeared<other_time).filter(Words.status==0).order_by(func.random()).limit(n)
	for itm in new_words:
		word={
			"word": itm.word,
			"options": []
		}


		options_obj=config.db.session.query(Words).order_by(func.random()).limit(4)
		options_list=[]

		for x in options_obj:
			options_list.append(x.meaning)
		idx=random.randint(0,4)

		options_list=options_list[:idx]+[itm.meaning]+options_list[idx:]

		word["options"]=options_list
		word["answer_idx"]=idx+1
		word["answer"]=itm.meaning
		word["attempts"]=itm.attempts
		word["correct"]=itm.correct
		word["state"]="ACTIVE"


		word_list.append(word)

	return word_list



def fetch_words(word_type, n):

	wrong_words=config.db.session.query(Words).filter_by(word_type=word_type).filter(Words.status==0).filter(Words.attempts!=0).filter((Words.correct/Words.attempts)<0.7).limit(4)

	word_list=[]

	for itm in wrong_words:
		print(itm)

		word={
			"word": itm.word,
			"options": []
		}


		options_obj=config.db.session.query(Words).filter_by(word_type=word_type).order_by(func.random()).limit(4)
		options_list=[]

		for x in options_obj:
			options_list.append(x.meaning)
		idx=random.randint(0,4)

		options_list=options_list[:idx]+[itm.meaning]+options_list[idx:]



		word["options"]=options_list
		word["answer_idx"]=idx+1
		word["answer"]=itm.meaning
		word["attempts"]=itm.attempts
		word["correct"]=itm.correct
		word["state"]="ACTIVE"


		word_list.append(word)

	other_time = datetime.now() - timedelta(hours=1)
	new_words=config.db.session.query(Words).filter_by(word_type=word_type).filter(Words.last_appeared<other_time).filter(Words.status==0).order_by(func.random()).limit(4-len(word_list))
	for itm in new_words:
		word={
			"word": itm.word,
			"options": []
		}


		options_obj=config.db.session.query(Words).order_by(func.random()).limit(4)
		options_list=[]

		for x in options_obj:
			options_list.append(x.meaning)
		idx=random.randint(0,4)

		options_list=options_list[:idx]+[itm.meaning]+options_list[idx:]

		word["options"]=options_list
		word["answer_idx"]=idx+1
		word["answer"]=itm.meaning
		word["attempts"]=itm.attempts
		word["correct"]=itm.correct
		word["state"]="ACTIVE"


		word_list.append(word)

	random.shuffle(word_list)

	return word_list


def get_average_score(word_type):
	"""Average score of last 7 days"""
	other_time = datetime.now() - timedelta(hours=168)
	x = config.db.session.query(label('total', func.sum(Words.attempts)), label('correct', func.sum(Words.correct))).filter_by(word_type=word_type).first()
	return {
		"attempts" : x[0],
		"correct": x[1]
	}





