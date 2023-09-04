import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

RO_TOKEN = os.environ.get('RO_TOKEN')
SB_TOKEN = os.environ.get('SB_TOKEN')
