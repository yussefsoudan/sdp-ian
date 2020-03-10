import os
import sys
flight_id = sys.argv[1]
os.system ("ssh ubuntu@192.168.105.28 nohup python ~/sdp-ian/Live/third_pi/check_db.py " + flight_id)
