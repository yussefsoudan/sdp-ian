#!/usr/bin/env python
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseActionFeedback
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion
import sys

# class getPosition():
#     def __init__(self):

#         # self.goal_sent = False
#         # rospy.on_shutdown(self.shutdown)
#         # self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)

#         # Get the current position from move_base/feedback
#         self.position_msg = rospy.wait_for_message('/move_base/feedback', MoveBaseActionFeedback)
#         self.coordinates = self.get_coordinates()

        # rospy.loginfo("Wait for the action server to come up")
        # self.move_base.wait_for_server(rospy.Duration(1))

    # def stop(self):
    #     # Send a goal = current position
    #     self.goal_sent = True
    #     goal = MoveBaseGoal()
    #     goal.target_pose.header.frame_id = 'map'
    #     goal.target_pose.header.stamp = rospy.Time.now()
    #     goal.target_pose.pose = self.position_msg.feedback.base_position.pose

    #     self.move_base.send_goal(goal)

    #     result = False
    #     self.goal_sent = False
    #     return result

    # def shutdown(self):
    #     if self.goal_sent:
    #         self.move_base.cancel_goal()
    #     rospy.sleep(1)

def get_coordinates():
    position_msg = rospy.wait_for_message('/move_base/feedback', MoveBaseActionFeedback)
    coordinates = position_msg.feedback.base_position.pose
    print("Coordinates given",coordinates.position.x, coordinates.position.y)
    return(coordinates.position.x, coordinates.position.y)

# if __name__ == '__main__':
#     try:
#         rospy.init_node('nav_test', anonymous=False)
#         navigator = getPosition()
#         # success = navigator.stop()
#         c = navigator.get_coordinates()
#         # rospy.sleep(1)

#     except rospy.ROSInterruptException:
#         rospy.loginfo("Ctrl-C caught. Quitting")

