import pandas as pd
import pymysql
import json
import datetime

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
	time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	content = request['message']['content']
	msg_info = "(%d, %d, \"%s\", \"%s\", \"%s\");" % (store_msg.msgid, target, author, time, content)
	with conn.cursor() as cur:
		cur.execute("INSERT INTO message (messageid, chatroomid, userid, clock, content) VALUES " + msg_info)
	conn.commit()



# reads in a json object request
def retrieve_msg(request):
	print("retrieving message...")
	target = request['message']['chatroomid']
	last_msgid = request['message']['messageid']
	with conn.cursor() as cur: 
		sql = "SELECT * FROM message WHERE chatroomid = %d AND messageid > %d;" % (target, last_msgid)
		cur.execute(sql)
		msgs = cur.fetchall()
	# print(msgs)
	# print(type(msgs))

	msg_list = []
	for i in range(0,len(msgs)):
		thismsg = msgs[i]
		# print(thismsg)
		thismsg_in_json = json.dumps(dict(messageid = thismsg[0], chatroomid = thismsg[1], 
						userid = thismsg[2], clock = thismsg[3].strftime("%Y-%m-%d %H:%M:%S"), content = thismsg[4]))
		msg_list.append(thismsg_in_json)

	retrv = '{"messages" : %s}' % msg_list

	print(retrv)





















