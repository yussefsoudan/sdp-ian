import mysql.connector
import sys
sys.path.insert(0, '~/sdp-ian/env.py')
import env
def clean_db():
	conn = mysql.connector.connect(host = SERVER_PI_IP,database = 'main_sdp_db',
	user = 'secondPi', password = 'turtlebot', port = 3306)
	cursor = conn.cursor()
# query string to be used for DB 
	query = "DELETE FROM link WHERE host = 'meowth'"
	cursor.execute(query)
#output = cursor.execute(query)   
#ursor.execute(query)
 
	cursor.close()
	conn.commit()
	conn.close()
