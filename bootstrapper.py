import logging

from datacontext.database import Database

logging.getLogger().setLevel(logging.INFO)

db = Database('sqlite:///data/database.db')
db.create()