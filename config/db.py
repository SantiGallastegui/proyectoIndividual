from importlib.metadata import metadata
from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:necochea2012@localhost:3306/proyecto")

conn= engine.connect()

meta_data = MetaData()