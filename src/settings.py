"""
This file checks for the existence of a .env file and loads the environment variables from it. If the .env
file does not exist then we load the environment variables from the system environment variables.
"""

import os
from dotenv import load_dotenv
import logging

env_file = '../.env'
if os.path.exists(env_file):
    load_dotenv(dotenv_path=env_file)

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,  # DEBUG, INFO, WARNING, ERROR, CRITICAL - change to DEBUG for more verbosity (revert to INFO)
    format='%(levelname)s: %(message)s',
    handlers=[logging.StreamHandler()]
)


# Load the environment variables
MONGO_URL = os.getenv('MONGO_URL')
RMQ_URL = os.getenv('RMQ_URL')

