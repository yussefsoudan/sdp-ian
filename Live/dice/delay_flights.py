import mysql.connector
import sys
sys.path.insert(0, '~/sdp-ian/env.py')
import env


connection = mysql.connector.connect(host=SERVER_PI_IP, 
database='main_sdp_db', user='secondPi', password='turtlebot', port=3306)

cursor = connection.cursor()

# These queries delay all flights by 20 minutes.
status_query = "UPDATE flights SET status = 'Delayed'"
boarding_time_query = "UPDATE flights SET boarding_time = ADDTIME(boarding_time, '0:20:0')"
depature_time_query = "UPDATE flights SET depature_time = ADDTIME(depature_time, '0:20:0')"

# The final query, the status_query, will automatically update the flight_changes table,
# which will then cause the third_pi/check_db.py script to alert the user.
cursor.execute(boarding_time_query)
connection.commit()
cursor.execute(depature_time_query)
connection.commit()
cursor.execute(status_query)
connection.commit()

cursor.close()
connection.close()
