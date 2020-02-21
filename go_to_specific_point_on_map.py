#!/usr/bin/env python
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion
import sys

class GoToPose():
    def __init__(self):

        self.goal_sent = False

        # What to do if shut down (e.g. Ctrl-C or failure)
        rospy.on_shutdown(self.shutdown)
        
        # Tell the action client that we want to spin a thread by default
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        rospy.loginfo("Wait for the action server to come up")

        # Allow up to 5 seconds for the action server to come up
        self.move_base.wait_for_server(rospy.Duration(5))

    def goto(self, pos, quat):

        # Send a goal
        self.goal_sent = True
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(pos['x'], pos['y'], 0.000),
        Quaternion(quat['r1'], quat['r2'], quat['r3'], quat['r4']))

        # Start moving
        self.move_base.send_goal(goal)

        # Allow TurtleBot up to 60 seconds to complete task
        success = self.move_base.wait_for_result(rospy.Duration(60)) 

        state = self.move_base.get_state()
        result = False

        if success and state == GoalStatus.SUCCEEDED:
            # We made it!
            result = True
        else:
            self.move_base.cancel_goal()

        self.goal_sent = False
        return result

    def shutdown(self):
        if self.goal_sent:
            self.move_base.cancel_goal()
        rospy.loginfo("Stop")
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        rospy.init_node('nav_test', anonymous=False)
        navigator = GoToPose()
        #Initialize position and quaternion vectors 
        position = {'x': -0.1111, 'y' : -0.0244}
        quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.7038, 'r4' : 0.7103}
        if len(sys.argv)>1:
            gate_number = sys.argv[1]
        else:
            gate_number = 0 

        if gate_number == "0":
            # Customize the following values so they are appropriate for your location
            position = {'x': -0.1111, 'y' : -0.0244}
            quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.7038, 'r4' : 0.7103}
            print("go to gate 0")
        elif gate_number == "1":
            # Customize the following values so they are appropriate for your location
            position = {'x': 2.2008, 'y' : 2.3629}
            quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.7050, 'r4' : 0.7091}
            print("go to gate 1")
        elif gate_number == "2":
            # Customize the following values so they are appropriate for your location
            position = {'x': 3.3750, 'y' : 1.4000}
            quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.0076, 'r4' : 0.9999}
            print("go to gate 2")
        elif gate_number == "3":
            # Customize the following values so they are appropriate for your location
            position = {'x': 3.1872, 'y' : -0.1071}
            quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : -0.0014, 'r4' : 0.9999}
            print("go to gate 3")

        rospy.loginfo("Go to (%s, %s) pose", position['x'], position['y'])
        success = navigator.goto(position, quaternion)

        if success:
            rospy.loginfo("Hooray, reached the desired pose")
        else:
            rospy.loginfo("The base failed to reach the desired pose")

        # Sleep to give the last log messages time to be sent
        rospy.sleep(1)

    except rospy.ROSInterruptException:
        rospy.loginfo("Ctrl-C caught. Quitting")

