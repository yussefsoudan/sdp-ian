import mysql.connector
import sys
sys.path.insert(0, '~/sdp-ian/env.py')
import env

#initiate the connection to the DB
def get_infor(flight_id):
    conn = mysql.connector.connect(user='secondPi', password='turtlebot',
                              host=SERVER_PI_IP,
                              database='main_sdp_db',port =3306)

    cursor = conn.cursor()
# query string to be used for DB 
    query = "SELECT gate_no FROM flights WHERE flight_id = '{}'".format(flight_id) 
    output = []
    cursor.execute(query)
    row = cursor.fetchone()
    while row is not None:
        output.append(row)
	row = cursor.fetchone()

    query = "SELECT status FROM flights WHERE flight_id = '{}'".format(flight_id) 
    cursor.execute(query)
    row = cursor.fetchone()
    while row is not None:
        output.append(row)
	row = cursor.fetchone()

    query = "SELECT boarding_time FROM flights WHERE flight_id = '{}'".format(flight_id) 
    cursor.execute(query)
    row = cursor.fetchone()
    while row is not None:
        output.append(row)
	row = cursor.fetchone()

    query = "SELECT depature_time FROM flights WHERE flight_id = '{}'".format(flight_id) 
    cursor.execute(query)
    row = cursor.fetchone()
    while row is not None:
        output.append(row)
        row = cursor.fetchone()

    query = "SELECT destination FROM flights WHERE flight_id = '{}'".format(flight_id) 
    cursor.execute(query)
    row = cursor.fetchone()
    while row is not None:
        output.append(row)
        row = cursor.fetchone()

    cursor.close()
    conn.close()
    return output
