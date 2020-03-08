# Handles the data (e.g. passenger info, ) and logic of the program. It is the Model of the program.
# Holds the passenger data
# Should hold the destination? current widget?

import os
from get_pos import get_coordinates

from PyQt5 import QtTest

class Customer:

    def __init__(self, name=None, flight=None, gate=None, depart_time=None):
        self.name = name
        self.flight = flight
        self.gate = gate
        self.depart_time = depart_time

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
    cust = Customer()

    def __init__(self):
        pass

    # the scanning functionality
    def scan(self, view):
        view.setCurrentWidget(view.SCAN)

        QtTest.QTest.qWait(2000)

        os.system("python ~/Desktop/Demo2/sdp-ian/Scanning/realtime.py")
        info_file = open("info_file.txt","r")
        file_lines = info_file.readlines()
        self.cust.name = file_lines[0].strip()
        self.cust.flight = file_lines[1].strip()
        self.cust.gate = file_lines[2].strip()
        gate_status = file_lines[3].strip()
        board_time = file_lines[4].strip()
        self.cust.depart_time = file_lines[5].strip()
        dest = file_lines[6].strip()

        # if scanning failed
        if self.cust.isNullPassenger():
            # maybe add scanning failed pop up?
            view.setCurrentWidget(view.START)
            return

        view.setCurrentWidget(view.SUCCESS)

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

	    # NAVIGATION
        view.passenger_info_1.setText("{}\n{}\n{}\n{}".format(
            name_string, flight_string, gate_string, depart_time_string))

        # PAUSE
        view.passenger_info_2.setText("{}\n{}\n{}\n{}".format(
            name_string, flight_string, gate_string, depart_time_string))

        # for testing
        # if view.currentWidget() == view.SCAN: view.setCurrentWidget(view.SUCCESS)

        QtTest.QTest.qWait(4000)

        # for testing
        # if view.currentWidget() == view.SUCCESS: view.setCurrentWidget(view.INFO)

        view.setCurrentWidget(view.INFO)

    def help(self, view, previous_widget):
        view.setCurrentWidget(view.HELP)
        view.help_back.clicked.connect(lambda: view.setCurrentWidget(previous_widget))

    def exit(self, view, previous_widget):
        view.setCurrentWidget(view.EXIT)
        view.cancel_exit.clicked.connect(lambda: view.setCurrentWidget(previous_widget))
        view.exit_button.clicked.connect(lambda: self.goHub(view))

    def chooseDestination(self, view, location, previous_widget):
        view.setCurrentWidget(view.CONFIRM_DEST)
        view.destination_label.setText(location + "?")
        view.navigating_to_label2.setText(location)
        view.navigating_to_label3.setText(location)
        print("Location given choose Dest:",location)
        global global_loc
        global_loc = location

        view.back_to_prev.clicked.connect(lambda: view.setCurrentWidget(previous_widget))

    def showLocation(self, view, x, y):
        view.map_location.setGeometry(x,y,21,21)
        view.map_location_2.setGeometry(x,y,21,21)


    # the navigation functionality
    def navigate(self, view):
        QtTest.QTest.qWait(10)

        

        view.setCurrentWidget(view.NAVIGATING)
        # while True:
        # position = getPosition()
  
            # break
        # self.showLocation(view, 400,200)

        QtTest.QTest.qWait(10)
        # print("Location given Navigate:",location)
        # os.system(" python ~/Desktop/Demo2/Navigation/go_to_specific_point_on_map.py {}".format(self.cust.gate))
        os.system(" python ~/Desktop/Demo2/sdp-ian/Navigation/go_and_stay.py {}".format(global_loc))
        #view.pause_navigation.clicked.connect(lambda: self.pause(view))
        while True:
            
            x_point,y_point = get_coordinates()
            x = x_point/4.0 
            y = y_point/3.0

            x_map = ((1-x) * 345) + 350
            y_map = (y * 255) + 100
            print(x_map,y_map)
            self.showLocation(view, x_map,y_map)

        # QtTest.QTest.qWait(6000)
        # self.setCurrentWidget(self.COMPLETE)

    # the pausing functionality
    # move to ctrl?
    def pause(self, view):

        view.setCurrentWidget(view.PAUSE)
        QtTest.QTest.qWait(10)
        os.system(" python ~/Desktop/Demo2/sdp-ian/Navigation/cancel_goal.py")

    def goHub(self, view):
        pass
