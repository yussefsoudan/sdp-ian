import mysql.connector

#initiate the connection to the DB
def gate_no(flight_id):
    conn = mysql.connector.connect(user='group6', password='turtlebot',
                              host='localhost',
                              database='main_sdp_db')

    cursor = conn.cursor()
# query string to be used for DB 
    query = "SELECT * FROM flights WHERE flight_id = '{}'".format(flight_id) 
    
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
