# -*- coding: utf-8 -*-
# @Author: perfectus
# @Date:   2018-06-27 16:56:48
# @Last Modified by:   perfectus
# @Last Modified time: 2018-06-27 17:02:54

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from jwt import DecodeError, ExpiredSignature
from datetime import datetime, timedelta
import jwt
from jwt import DecodeError, ExpiredSignature
import config
from Models.Base import Base


class Scores(Base):
	__tablename__ = 'scores'

	def _get_date():
		return datetime.datetime.now()

	timestamp = Column(DateTime, primary_key=True, default=_get_date)
	attempts=Column(Integer)
	correct=Column(Integer)

		
	def __repr__(self):
		return '<Scores %r: %r/%r>' % (self.timestamp, self.correct, self.attempts)

