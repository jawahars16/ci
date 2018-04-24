import logging
import os

from common.task_loader import TaskLoader
from datacontext.database import Database

# Configure logging
logging.getLogger().setLevel(logging.DEBUG)

# Create database
db = Database('sqlite:///data/database.db')

# Initiatlize task loader
taskloader = TaskLoader(os.path.join(os.path.dirname(__file__), 'task'))
