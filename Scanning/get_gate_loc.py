import mysql.connector

#initiate the connection to the DB
def gate_infor(flight_id):
    conn = mysql.connector.connect(user='root', password='ubuntu',
                              host='localhost',
                              database='main_sdp_db')

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

#if __name__ == '__main__':
    #query_with_fetchone()
