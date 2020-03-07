import mysql.connector
def clean_db():
	conn = mysql.connector.connect(host = '192.168.105.28',database = 'main_sdp_db',
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
