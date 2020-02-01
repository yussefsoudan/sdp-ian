import mysql.connector

#initiate the connection to the DB
def query_db(flight_id):
    conn = mysql.connector.connect(user='gG4r5EDwsV', password='Whvk8bwI9p',
                              host='37.59.55.185',
                              database='gG4r5EDwsV')

    cursor = conn.cursor()
# query string to be used for DB 
    query = "SELECT * FROM flights WHERE flight_id = '{}'".format(flight_id) 
    output = []
    cursor.execute(query)
 
    row = cursor.fetchone()
 
    while row is not None:
        print(row)
        row = cursor.fetchone()
        output.append(row)
    cursor.close()
    conn.close()
 
    return output

#if __name__ == '__main__':
    #query_with_fetchone()

