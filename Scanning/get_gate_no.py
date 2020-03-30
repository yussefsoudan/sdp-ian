import mysql.connector
import sys
sys.path.insert(0, '~/sdp-ian/env.py')
import env

#initiate the connection to the DB
def gate_no(name):
	conn = mysql.connector.connect(user='secondPi', password='turtlebot',
                              host=SERVER_PI_IP,
                              database='main_sdp_db',port =3306)
	cursor = conn.cursor()
# query string to be used for DB 
	query = "SELECT flight_id FROM passengers WHERE name = '{}'".format(name) 
	output = []
	cursor.execute(query)
 	row = cursor.fetchone()
 	while row is not None:
        	output.append(row)
		row = cursor.fetchone()
	cursor.close()
	conn.close()
 	return output[0]

#if __name__ == '__main__':
    #query_with_fetchone()
