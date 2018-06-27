from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def as_dict(self):
	"""Converts SQL class to dictionary"""
	return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Base.__dict = as_dict
