import time 
import sys
import mysql.connector

#starttime=time.time() 
conn = mysql.connector.connect(host = 'localhost',database = 'main_sdp_db',
	user = 'root', password = 'turtlebot')	
cursor = conn.cursor()
query = "SELECT status FROM flights WHERE flight_id = '{}'".format(sys.argv[1])
cursor.execute(query)
row = cursor.fetchone()
output1 = row
cursor.close()
#print(output[0])
while True:
	output2 = []
	cursor.execute(query)
	row = cursor.fetchone()
	output2 = row
	if output1[0] != output2[0]:
		print('flight change')
		break
	cursor.close()

	time.sleep(60.0 - ((time.time() - starttime) % 60.0))
