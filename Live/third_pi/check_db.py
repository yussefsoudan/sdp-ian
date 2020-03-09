import time 
import sys
import mysql.connector
import os

#starttime=time.time() 
conn = mysql.connector.connect(host = 'localhost',database = 'main_sdp_db',
	user = 'root', password = 'turtlebot')	
cursor = conn.cursor()
query = "SELECT status FROM flights WHERE flight_id = '{}'".format(sys.argv[1])
cursor.execute(query)
row = cursor.fetchone()
output1 = row
cursor.close()
conn.close()
print(output1[0])
while True:
	output2 = []
	conn = mysql.connector.connect(host = 'localhost',database = 'main_sdp_db',
	user = 'root', password = 'turtlebot')
	cursor = conn.cursor()	
	cursor.execute(query)
	row = cursor.fetchone()
	output2 = row
	if output1[0] != output2[0]:
		print('flight change')
		#print(output2[0])
		os.system ("ssh ubuntu@192.168.105.149 nohup python ~/Desktop/Demo2/sdp-ian/Live/change.py " + output2[0])
		break
	else: 
		print('flight not change')
	cursor.close()
	conn.close()
	time.sleep(5)
