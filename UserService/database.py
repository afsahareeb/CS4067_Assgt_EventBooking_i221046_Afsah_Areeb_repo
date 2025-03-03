from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:1234@localhost/event_booking"

engine = create_engine(DATABASE_URL) # establis connection with database
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False) # to interact with db(read/write)
Base = declarative_base() # to create models
metadata = MetaData() # stores schema information
