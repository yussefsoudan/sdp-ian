import os, sys

if len(sys.argv) > 1:
   gate_number = sys.argv[1]
else:
    gate_number = 0 # something else? maybe dont move at all?


if gate_number == 0:
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: \"map\"}, pose: {position: {x: -0.111136, y: -0.0244647, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.7038022, w: 0.71039594}}}'")

if gate_number == 1:
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: \"map\"}, pose: {position: {x: 2.2008500, y: 2.362956, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.705013, w: 0.709193}}}'")

if gate_number == 2:
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: \"map\"}, pose: {position: {x: 3.375043, y: 1.400088, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0076134, w: 0.9999710}}}'")

if gate_number == 3:
    os.system("rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: \"map\"}, pose: {position: {x: 3.1872487, y: -0.1071971, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: -0.00140772, w: 0.9999990}}}'")


