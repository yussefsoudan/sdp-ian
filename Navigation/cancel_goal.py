#!/usr/bin/env python
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseActionFeedback
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion
import sys

class GoToPose():
    def __init__(self):

        self.goal_sent = False
        rospy.on_shutdown(self.shutdown)
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)


        rospy.loginfo("CANCEL SCRIPT MESSAGE : Wait for the action server to come up")
        self.move_base.wait_for_server(rospy.Duration(5))

    def stop(self):
        # Send a goal = current position
        self.goal_sent = True
        self.move_base.cancel_all_goals()

        result = False
        self.goal_sent = False
        return result

    def shutdown(self):
        if self.goal_sent:
            self.move_base.cancel_goal()
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        rospy.init_node('nav_test', anonymous=False)
        navigator = GoToPose()
        success = navigator.stop()
        rospy.sleep(1)

    except rospy.ROSInterruptException:
        rospy.loginfo("Ctrl-C caught. Quitting")

