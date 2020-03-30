import os
import sys
sys.path.insert(0, '~/sdp-ian/env.py')
import env

flight_id = sys.argv[1]
os.system ("ssh ubuntu@" + SERVER_PI_IP + "nohup python ~/sdp-ian/Live/third_pi/check_db.py " + flight_id)
