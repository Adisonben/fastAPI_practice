from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = 'postgres'
password = '12116521'
host = 'localhost'
port = '5432'
database = 'postgres'
# for creating connection string
connection_str = f'postgresql:// {user}:{password}@{host}:{port}/{database}'
engine = create_engine(connection_str)