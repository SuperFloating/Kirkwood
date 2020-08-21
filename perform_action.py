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

# reads in a json object request
def send_msg(request):
	print("sending message")
	target = request['message']['chatroomid']
	author = request['message']['userid']
	time = request['message']['clock']
	content = request['message']['content']
	msg_info = "(%d, %d, \"%s\", \"%s\", \"%s\");" % (1, target, author, time, content)
	with conn.cursor() as cur:
		print("cp1")
		cur.execute("INSERT INTO message (messageid, chatroomid, userid, clock, content) VALUES " + msg_info)
	conn.commit()
	print("cp2")


# reads in a json object request
def retrieve_msg(request):
	print("retrieving message")