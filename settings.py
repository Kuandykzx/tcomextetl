import os

from dotenv import load_dotenv

load_dotenv()

DATA_PATH = os.getenv('DATA_PATH')
TEMP_PATH = os.getenv('TEMP_PATH')
PARAMS_CONFIG_PATH = os.getenv('PARAMS_CONFIG_PATH')

FTP_PATH = os.getenv('FTP_PATH')
FTP_HOST = os.getenv('FTP_HOST')
FTP_USER = os.getenv('FTP_USER')
FTP_PASS = os.getenv('FTP_PASS')

GOSZAKUP_API_HOST = os.getenv('GOSZAKUP_API_HOST')
GOSZAKUP_TOKEN = os.getenv('GOSZAKUP_TOKEN')
