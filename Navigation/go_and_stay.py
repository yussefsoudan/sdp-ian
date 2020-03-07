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
        # success = self.move_base.wait_for_result(rospy.Duration(60))

        # state = self.move_base.get_state()
        result = False

        # if success and state == GoalStatus.SUCCEEDED:
            # We made it!
            #result = True
        #else:
           # self.move_base.cancel_goal()

        self.goal_sent = False
        return result

    def shutdown(self):
        if self.goal_sent:
            self.move_base.cancel_goal()
        #rospy.loginfo("Stop")
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        rospy.init_node('nav_test', anonymous=False)
        navigator = GoToPose()
        #Initialize position and quaternion vectors
        position = {'x': -0.1111, 'y' : -0.0244}
        quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.7038, 'r4' : 0.7103}

        destination = "Gate 0"
        if len(sys.argv)==2:
            destination = sys.argv[1]
        elif len(sys.argv)>2:
            destination = "{} {}".format(sys.argv[1],sys.argv[2])
        else:
            destination = "Gate 0"

        print("Destination given to script: ",destination)
        if destination == "Gate 0":
            # Customize the following values so they are appropriate for your location
            position = {'x': -0.1111, 'y' : -0.0244}
            quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.7038, 'r4' : 0.7103}
            print("go to gate 0")
        elif destination == "Gate 1":
            # Customize the following values so they are appropriate for your location
            position = {'x': 2.2008, 'y' : 2.3629}
            quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.7050, 'r4' : 0.7091}
            print("go to gate 1")
        elif destination == "Gate 2":
            # Customize the following values so they are appropriate for your location
            position = {'x': 3.3750, 'y' : 1.4000}
            quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.0076, 'r4' : 0.9999}
            print("go to gate 2")
        elif destination == "Gate 3":
            # Customize the following values so they are appropriate for your location
            position = {'x': 3.1872, 'y' : -0.1071}
            quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : -0.0014, 'r4' : 0.9999}
            print("go to gate 3")

        elif destination == "Next":

            # Customize the following values so they are appropriate for your location
            position = {'x': 0.490000, 'y' :1.629999}
            quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.937488, 'r4' : 0.348016}
            print("go to caffee next")

        elif destination == "Hugo Boss":

            # Customize the following values so they are appropriate for your location
            position = {'x':1.2200001, 'y' : 2.489999}
            quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.7071067, 'r4' : 0.70710}
            print("go to hugo boss")

        elif destination == "Superdrug":

            # Customize the following values so they are appropriate for your location
            position = {'x':  2.530000, 'y' : 2.49999}
            quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.695228, 'r4' : 0.71878}
            print("go to superdrug")


            # Customize the following values so they are appropriate for your location
            position = {'x':  0.87999, 'y' : 1.11999}
            quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : -0.707106, 'r4' : 0.7071067}
            print("go to toilets")

        elif destination == "Bar Burrito":

            # Customize the following values so they are appropriate for your location
            position = {'x':  2.637212, 'y' : 1.188111}
            quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.951828, 'r4' : 0.306629}
            print("go to barburrito")

        elif destination == "Burger King":

            # Customize the following values so they are appropriate for your location
            position = {'x': 1.7798051, 'y' : 1.3155964}
            quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' :0.25879017, 'r4' : 0.96593356}
            print("go to burger king")

        elif destination == "Caffe Nero":

            # Customize the following values so they are appropriate for your location
            position = {'x':  2.23519587, 'y' : 1.991406}
            quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : -0.7233548, 'r4' :0.6904765}
            print("go to caffee nero")

        rospy.loginfo("Go to (%s, %s) pose", position['x'], position['y'])
        success = navigator.goto(position, quaternion)

        # Sleep to give the last log messages time to be sent
        rospy.sleep(1)

    except rospy.ROSInterruptException:
        rospy.loginfo("Ctrl-C caught. Quitting")
