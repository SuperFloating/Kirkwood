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
def store_msg(request):
	print("storing message...")

	# gets an id for this message
	try:
		store_msg.msgid += 1
	except AttributeError:
		with conn.cursor() as cur: 
			cur.execute("SELECT MAX(messageid) FROM message")
			fetchid = cur.fetchone()
		print(fetchid)
		if fetchid[0] == None: 
			store_msg.msgid = 0
		else: 
			store_msg.msgid = fetchid[0] + 1

	target = request['message']['chatroomid']
	author = request['message']['userid']
	time = request['message']['clock']
	content = request['message']['content']
	msg_info = "(%d, %d, \"%s\", \"%s\", \"%s\");" % (store_msg.msgid, target, author, time, content)
	with conn.cursor() as cur:
		cur.execute("INSERT INTO message (messageid, chatroomid, userid, clock, content) VALUES " + msg_info)
	conn.commit()	



# reads in a json object request
def retrieve_msg(request):
	print("retrieving message...")