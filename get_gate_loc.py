import mysql.connector

#initiate the connection to the DB
def gate_infor(gate_no):
    conn = mysql.connector.connect(user='group6', password='turtlebot',
                              host='localhost',
                              database='main_sdp_db')

    cursor = conn.cursor()
# query string to be used for DB 
    query = "SELECT x_coord FROM gates WHERE gate_no = '{}'".format(gate_no) 
    output = []
    cursor.execute(query)
    row = cursor.fetchone()
    while row is not None:
        output.append(row)
	row = cursor.fetchone()

    query = "SELECT y_coord FROM gates WHERE gate_no = '{}'".format(gate_no) 
    cursor.execute(query)
    row = cursor.fetchone()
    while row is not None:
        output.append(row)
	row = cursor.fetchone()

    query = "SELECT z_coord FROM gates WHERE gate_no = '{}'".format(gate_no) 
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
