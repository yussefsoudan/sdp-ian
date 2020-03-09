import mysql.connector
def link(flight_id):
	conn = mysql.connector.connect(host = '192.168.105.28',database = 'main_sdp_db',
	user = 'secondPi', password = 'turtlebot', port = 3306)	
	cursor = conn.cursor()

	sql = "INSERT INTO link (host, flight_id) VALUES ('meowth', '{}')".format(flight_id)
	cursor.execute(sql)

	cursor.close()
	conn.commit()	
	conn.close()
#print output
#if __name__ == '__main__':
    #query_with_fetchone()

