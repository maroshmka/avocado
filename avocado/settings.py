import os
from dotenv import load_dotenv
load_dotenv('.env', verbose=True)

SLACK_API_WEBHOOK = os.getenv('SLACK_API_WEBHOOK')
