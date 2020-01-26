import mysql.connector

#initiate the connection to the DB
conn = mysql.connector.connect(user='gG4r5EDwsV', password='Whvk8bwI9p',
                              host='37.59.55.185',
                              database='gG4r5EDwsV')

curser = conn.cursor()
# query string to be used for DB 
query = "SELECT * FROM flights"

cursor.execute(query)
 
row = cursor.fetchone()
 
while row is not None:
    print(row)
    row = cursor.fetchone()

cursor.close()
conn.close()
 
 
if __name__ == '__main__':
    query_with_fetchone()
