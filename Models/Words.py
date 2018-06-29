# -*- coding: utf-8 -*-
# @Author: perfectus
# @Date:   2018-06-27 16:56:48
# @Last Modified by:   sumansaurabh
# @Last Modified time: 2018-06-29 14:41:30

from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from jwt import DecodeError, ExpiredSignature
from datetime import datetime, timedelta
import jwt
from jwt import DecodeError, ExpiredSignature
import config
from Models.Base import Base


class Words(Base):
	__tablename__ = 'words'

	def _get_date():
		x=datetime.now()
		print("--################# -> x",x)
		return x

	word = Column(String(100), primary_key=True)
	meaning = Column(String(2500))
	last_appeared=Column(DateTime, default=_get_date())
	attempts=Column(Float, default=0)
	correct=Column(Float, default=0)
	status=Column(Integer, default=0)


		
	def __repr__(self):
		return '<Words %r>' % (self.word)

