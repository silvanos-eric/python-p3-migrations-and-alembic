#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///migration_test.db')

Base = declarative_base()