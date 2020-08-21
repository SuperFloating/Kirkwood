import pandas as pd
import pymysql
import json

with open('credential.json') as c:
	credential = json.load(c)
host = credential['db_host']
port = credential['db_port']
schema = credential['db_schema']
user = credential['db_user']
password = credential['db_password']


conn = pymysql.connect(host, user = user, port = port,
                           passwd = password, db = schema)

def send_msg():
	print("sending message")

def retrieve_msg():
	print("retrieving message")