# Handles the data (e.g. passenger's flight information) and logic of the program. It is the Model of the program.

import os, time
from get_pos import get_coordinates, get_status, get_vel, get_goal_pos

from PyQt5 import QtTest

# encapsulates the user's flight information
class Customer:

    def __init__(self, name=None, flight=None, gate=None, depart_time=None):
        self.name = name
        self.flight = flight
        self.gate = gate
        self.depart_time = depart_time

    # determines if the user's data has been set
    def isNullPassenger(self):
        return (self.name == None or self.flight == None
        or self.gate == None or self.depart_time == None)

    # clears customer data
    def clearCustomer(self):
        self.name = None
        self.flight = None
        self.gate = None
        self.depart_time = None

# for testing
sampleCustomer = Customer("Joe Bloggs", "AA100", "2", "15:00")

class IanUiModel:
    
    global_loc = ""
    isNavigating = False
    cust = Customer()

    def __init__(self):
        pass

    # the scanning functionality
    def scan(self, view):
    
        view.setCurrentWidget(view.SCAN)
        QtTest.QTest.qWait(2000)

        os.system("python ~/sdp-ian/Scanning/realtime.py")
	
        info_file = open("info_file.txt","r")
        file_lines = info_file.readlines()
        self.cust.name = file_lines[0].strip()
        self.cust.flight = file_lines[1].strip()
        self.cust.gate = file_lines[2].strip()
        gate_status = file_lines[3].strip()
        board_time = file_lines[4].strip()
        self.cust.depart_time = file_lines[5].strip()
        dest = file_lines[6].strip()

        os.system("python ~/sdp-ian/Live/second_pi/check_for_status_change.py {}".format(self.cust.flight))

        # if scanning failed goes back to the home page
        if self.cust.isNullPassenger():
            view.setCurrentWidget(view.START)
            return

	# shows the success screen for a few seconds
        view.setCurrentWidget(view.SUCCESS)
	
        self.updateDetails(view)

        QtTest.QTest.qWait(4000)

        view.setCurrentWidget(view.INFO)

    # updates the user's flight information in the UI itself
    def updateDetails(self, view):

        # for reuse
        name_string = "Name: " + self.cust.name
        flight_string = "Flight: " + self.cust.flight
        gate_string = "Gate: " + self.cust.gate
        depart_time_string = "Departure time: " + self.cust.depart_time

        # setting labels in INFO
        view.name_label.setText(name_string)
        view.flight_label.setText(flight_string)
        view.gate_label.setText(gate_string)
        view.depart_time_label.setText(depart_time_string)

	# in NAVIGATION
        view.passenger_info_1.setText("{}\n{}\n{}\n{}".format(
            name_string, flight_string, gate_string, depart_time_string))

        # and in PAUSE
        view.passenger_info_2.setText("{}\n{}\n{}\n{}".format(
            name_string, flight_string, gate_string, depart_time_string))


    # goes to help page, and goes back to the last page when exiting
    def help(self, view, previous_widget):
        view.setCurrentWidget(view.HELP)
        view.help_back.clicked.connect(lambda: view.setCurrentWidget(previous_widget))
	
    # the same as help() but for the exit page
    def exit(self, view, previous_widget):
        view.setCurrentWidget(view.EXIT)
        view.cancel_exit.clicked.connect(lambda: view.setCurrentWidget(previous_widget))
        view.exit_button.clicked.connect(lambda: self.goHub(view))
	
    # sets the navigation goal
    def chooseDestination(self, view, location, previous_widget):
		
        view.setCurrentWidget(view.CONFIRM_DEST)
	
        view.destination_label.setText(location + "?")
        view.navigating_to_label2.setText(location)
        view.navigating_to_label3.setText(location)
        print("Location given choose Dest:", location) 
        global global_loc
        global_loc = location

        x_map,y_map = get_goal_pos(global_loc)
         # Turn Goal Coordinates to Point in UI map
        # goal_x,goal_y = get_goal_pos(global_loc) 
        # x = goal_x/4.0
        # y = goal_y/3.0
        # x_map = ((1-x) * 345) + 315 # it was 350 
        # y_map = (y * 255) + 130 # it was 100 
        self.showGoal(view, x_map ,y_map)

        view.back_to_prev.clicked.connect(lambda: view.setCurrentWidget(previous_widget))

    def showLocation(self, view, x, y):
        view.map_location.setGeometry(x,y,21,21)

    def showGoal(self, view, x, y):
        view.map_goal.setGeometry(x,y,21,21)

    # sets the estimated journey time for the chosen destination
    def estTime(self, view, goal):

        if goal == "Toilets":
            time = 13
        elif goal == "Next":
            time = 14
        elif goal == "Hugo Boss":
            time = 20
        elif goal == "Burger King":
            time = 19
        elif goal == "Caffe Nero":
            time = 25
        elif goal == "Superdrug":
            time = 29
        elif goal == "Bar Burrito":
            time = 28
        elif goal == "Gate 1":
            time = 0
        elif goal == "Gate 2":
            time = 0
        elif goal == "Gate 3":
            time = 0

        view.est_time.setText("Est. Journey Time: " + str(time) + " seconds")
        view.est_time_2.setText("Est. Journey Time: " + str(time) + " seconds")

        return time

    # the navigation functionality
    def navigate(self, view):

        print("I am navigating")
        global isNavigating
        isNavigating = True

        estimatedTotalTime = self.estTime(view, global_loc)

        QtTest.QTest.qWait(10)
        view.setCurrentWidget(view.NAVIGATING)
        QtTest.QTest.qWait(10)

        # print("Location given Navigate:",location)
	
        os.system(" python ~/sdp-ian/Navigation/go_and_stay.py {}".format(global_loc))
        
        QtTest.QTest.qWait(100)
        # isNavigating = False
        
        startTime = time.time()
        secondsElapsed = 0

        while isNavigating:

            print("I am navigating")
            vel_x,vel_y,ang_x,ang_y = get_vel()
            status = get_status()
	
	    # updates the estimated journey time left if it changes
            if secondsElapsed >= estimatedTotalTime:
                pass
            else:
                secondsSinceStart = int(time.time() - startTime)
                if secondsSinceStart > secondsElapsed:
                    secondsElapsed = secondsSinceStart
                    secondsLeft = estimatedTotalTime - secondsElapsed
                    view.est_time.setText("Est. Journey Time: " + str(secondsLeft) + " seconds")
                    view.est_time_2.setText("Est. Journey Time: " + str(secondsLeft) + " seconds")

            if (vel_x == 0.0 and vel_y == 0.0 and ang_x == 0.0 and ang_y == 0.0 and status == 3):
                #wait for the status to update to make sure we are not navigating to new goal 
                QtTest.QTest.qWait(3000)
                status = get_status()
                if status != 3:
                    print("Should continue with navigation")
                    continue
                isNavigating = False
                print("Status is in navigation function : {}".format(status))
                print("Break out of WHILE loop")
                break
            elif (vel_x == 0.0 and vel_y == 0.0 and ang_x == 0.0 and ang_y == 0.0):
                continue
            else:
                x_map,y_map = get_coordinates()
                # x = x_point/3.95
                # y = y_point/3.0

                # x_map = ((1-x) * 345) + 315
                # y_map = (y * 255) + 130
                print(x_map,y_map)
                self.showLocation(view, x_map  ,y_map)
            QtTest.QTest.qWait(10)

        # if status == 3 :
        # # QtTest.QTest.qWait(6000)
        #     os.system(" python ~/sdp-ian/Navigation/cancel_goal.py")
        #     self.setCurrentWidget(self.COMPLETE)

    # pauses navigation
    def pause(self, view):
        global isNavigating
        isNavigating = False

        view.setCurrentWidget(view.PAUSE)
        QtTest.QTest.qWait(10)
        os.system(" python ~/sdp-ian/Navigation/cancel_goal.py")

    # ian back to the hub
    def goHub(self, view):
        os.system("python ~/sdp-ian/Navigation/go_and_stay.py")
