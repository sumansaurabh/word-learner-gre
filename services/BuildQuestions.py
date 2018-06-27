# -*- coding: utf-8 -*-
# @Author: perfectus
# @Date:   2018-06-27 20:45:28
# @Last Modified by:   perfectus
# @Last Modified time: 2018-06-27 21:50:43

import config
from Models.Words import Words
from datetime import datetime, timedelta
import random
from  sqlalchemy.sql.expression import func, select




def fetch_words(n):
	

	other_time = datetime.now() - timedelta(hours=0.01)



	wrong_words=config.db.session.query(Words).filter(Words.correct/Words.attempts>0.7).limit(6)

	word_list=[]

	for itm in wrong_words:

		word={
			"word": itm.word,
			"options": []
		}


		options_obj=config.db.session.query(Words).order_by(func.random()).limit(4)
		options_list=[]

		print("#######111##########")
		for x in options_obj:
			options_list.append(x.meaning)
		idx=random.randint(0,4)

		options_list=options_list[:idx]+[itm.meaning]+options_list[idx:]

		print(options_list)


		word["options"]=options_list
		word["answer"]=idx+1
		word["answer_sent"]=itm.meaning
		print("#########444########")


		word_list.append(word)
		print itm

	new_words=config.db.session.query(Words).filter(Words.last_appeared<other_time).limit(10)
	for itm in new_words:
		word={
			"word": itm.word,
			"options": []
		}


		options_obj=config.db.session.query(Words).order_by(func.random()).limit(4)
		options_list=[]

		print("#######111##########")
		for x in options_obj:
			options_list.append(x.meaning)
		idx=random.randint(0,4)

		options_list=options_list[:idx]+[itm.meaning]+options_list[idx:]

		word["options"]=options_list
		word["answer"]=idx+1
		word["answer_sent"]=itm.meaning
		print("#########444########")


		word_list.append(word)
		print itm

	random.shuffle(word_list)

	return word_list



