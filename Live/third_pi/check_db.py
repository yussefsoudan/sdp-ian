import time 
import sys
import mysql.connector
import os

#starttime=time.time() 
conn = mysql.connector.connect(host = 'localhost',database = 'main_sdp_db',
	user = 'root', password = 'turtlebot')	
cursor = conn.cursor()
flight_id = sys.argv[1]
query = "SELECT status FROM flights WHERE flight_id = '{}'".format(flight_id)
cursor.execute(query)
row = cursor.fetchone()
output1 = row
original_status = str(output1[0])

cursor.close()
conn.close()
print('Original status: ' + original_status)
while True:
	output2 = []
	conn = mysql.connector.connect(host = 'localhost',database = 'main_sdp_db',
	user = 'root', password = 'turtlebot')
	cursor = conn.cursor()	
	cursor.execute("SELECT status_after FROM flight_changes WHERE flight_id = '{}'".format(flight_id))
	row = cursor.fetchone()
	output2 = row
	cursor.close()
	conn.close()
	if row is not None:	
		current_status = str(output2[0])
		print('The flight status has changed!')
		print('New status: ' + current_status)
		
		output3 = []
		conn = mysql.connector.connect(host = 'localhost',database = 'main_sdp_db',
		user = 'root', password = 'turtlebot')
		cursor = conn.cursor()
		query = "SELECT depature_time FROM flights WHERE flight_id = '{}'".format(flight_id)
		cursor.execute(query)
		
		row = cursor.fetchone()
		output3 = row
		new_depart_time = str(output3[0])
		
		os.system ("ssh ubuntu@192.168.105.149 nohup python ~/sdp-ian/Live/second_pi/change.py " + current_status + " " + new_depart_time)
		cursor.close()
		conn.close()
		break
	else: 
		print('No status change...')
	
	time.sleep(5)
