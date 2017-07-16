from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql

import os

Base = declarative_base()

# Write needed classes here

#create_engine('sqlite:///project.db') # For local use
engine = create_engine(os.environ["DATABASE_URL"])
Base.metadata.create_all(engine)