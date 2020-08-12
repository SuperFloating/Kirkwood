import pandas as pd
import pymysql

host = "kirkwooddb.chvh78zduuko.us-west-2.rds.amazonaws.com"
port = 3306
dbname = "test"
user = "admin"
password = "KirkwoodDB"

conn = pymysql.connect(host, user = user, port = port,
                           passwd = password, db = dbname)

def send_msg():
	print("sending message")

def retrieve_msg():
	print("retrieving message")