#!/usr/bin/env python
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseActionFeedback
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion,Twist
import sys

def get_vel():
    rospy.init_node('vel_test', anonymous=False)
    vel_msg = rospy.wait_for_message('/cmd_vel', Twist)
    cmd_x = vel_msg.linear.x
    cmd_y = vel_msg.linear.y
    ang_x = vel_msg.angular.x
    ang_y = vel_msg.angular.y

    print("Linear Velocity is x : {}, y: {}, Angular Velocicity is x : {}, y: {} ".format(cmd_x,cmd_y,ang_x,ang_y))
    return(cmd_x,cmd_y,ang_x,ang_y)
def get_status():
    # rospy.init_node('status_test', anonymous=False)
    status_msg = rospy.wait_for_message('/move_base/status', GoalStatusArray)
    status = status_msg.status_list[0].status
    print("Status is ", status)
    return(status)

def get_coordinates():

    position_msg = rospy.wait_for_message('/move_base/feedback', MoveBaseActionFeedback)
    coordinates = position_msg.feedback.base_position.pose
    print("Coordinates given",coordinates.position.x, coordinates.position.y)
    #convert the coordinates to the UI scale
    x_map,y_map = convert_coordinates(coordinates.position.x, coordinates.position.y)
    return(x_map,y_map)

def get_goal_pos(destination):
    if destination == "Gate 0":
        # Customize the following values so they are appropriate for your location
        position = {'x': -0.1111, 'y' : -0.0244}
    elif destination == "Gate 1":
        # Customize the following values so they are appropriate for your location
        position = {'x': 2.2008, 'y' : 2.3629}
    elif destination == "Gate 2":
        # Customize the following values so they are appropriate for your location
        position = {'x': 3.3750, 'y' : 1.4000}
    elif destination == "Gate 3":
        # Customize the following values so they are appropriate for your location
        position = {'x': 3.1872, 'y' : -0.1071}
    elif destination == "Next":
        # Customize the following values so they are appropriate for your location
        position = {'x': 0.490000, 'y' :1.629999}
    elif destination == "Hugo Boss":
        # Customize the following values so they are appropriate for your location
        position = {'x':1.2200001, 'y' : 2.489999}
    elif destination == "Superdrug":
        # Customize the following values so they are appropriate for your location
        position = {'x':  2.530000, 'y' : 2.49999}
    elif destination == "Toilets":
        # Customize the following values so they are appropriate for your location
        position = {'x':  0.8599, 'y' : 0.9099}
    elif destination == "Bar Burrito":
        # Customize the following values so they are appropriate for your location
        position = {'x':  2.637212, 'y' : 1.188111}
    elif destination == "Burger King":
        # Customize the following values so they are appropriate for your location
        position = {'x': 1.7798051, 'y' : 1.3155964}
    elif destination == "Caffe Nero":
        # Customize the following values so they are appropriate for your location
        position = {'x':  2.23519587, 'y' : 1.991406}

    print("Destination Position x: {}, y:{}".format(position['x'],position['y']))
    x_map,y_map = convert_coordinates(position['x'],position['y'])
    return (x_map,y_map)

def convert_coordinates(x,y):
    x_temp = x/4.0 # divide by max of x in real arena
    y_temp = y/3.0 # divide by max y in real arena
    x_map = ((1-temp_x) * 345) + 315 # it was 350 , we do 1-x because we have some x that are negative
    y_map = (temp_y * 255) + 130 # it was 100 
    return (x_map,y_map)


