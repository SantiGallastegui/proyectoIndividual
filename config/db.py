from importlib.metadata import metadata
from sqlalchemy import create_engine, MetaData

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:admin@localhost:3306/proyecto")
# engine = create_engine("postgres://xlkqosnfemzjec:a34a13ff2cf813543f6367d83a37bff0b17a7df850ccce255b7f1837113616a0@ec2-35-168-122-84.compute-1.amazonaws.com:5432/dfeu34lpun977g")
conn= engine.connect()

meta_data = MetaData()