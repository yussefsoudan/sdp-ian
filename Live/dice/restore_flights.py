import mysql.connector

connection = mysql.connector.connect(host='192.168.105.28', 
database='main_sdp_db', user='secondPi', password='turtlebot', port=3306)

cursor = conn.cursor()

# These queries bring all flights back by 20 minutes and the status 'On time'.
status_query = "UPDATE flights SET status = 'On time'"
boarding_time_query = "UPDATE flights SET boarding_time = SUBTIME(boarding_time, '0:20:0')"
depature_time_query = "UPDATE flights SET depature_time = SUBTIME(depature_time, '0:20:0')"

# The final query, the status_query, will automatically update the flight_changes table,
# which will then cause the third_pi/check_db.py script to alert the user.
cursor.execute(boarding_time_query)
cursor.commit()
cursor.execute(depature_time_query)
cursor.commit()
cursor.execute(status_query)
cursor.commit()

cursor.close()
connection.close()
