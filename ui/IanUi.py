# Loads the .ui file and is the entry point of the UI. It is the View of the program.

import sys, time, os

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest, uic

# the model and controller classes
from IanUiCtrl import IanUiController
from IanUiMod import IanUiModel

__version__ = 0.1
__author__ = 'Daragh Meehan & Eloise Milliken'

class Customer:

    name = "Joe Blogs"
    flight = "AA100"
    gate = "2"
    depart_time = "15:00"

qtdesigner_file  = "the.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtdesigner_file)


class IanUi(QtWidgets.QStackedWidget, Ui_MainWindow):

    cust = Customer()

    def __init__(self):
        
        QtWidgets.QStackedWidget.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.setCurrentWidget(self.START)
        

    def scan(self):

        self.setCurrentWidget(self.SCAN)

        QtTest.QTest.qWait(1000)

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

        self.name_label.setText("Name: " + self.cust.name)
        self.flight_label.setText("Flight: " + self.cust.flight)
        self.gate_label.setText("Gate: " + self.cust.gate)
        self.depart_time_label.setText("Departure time: " + self.cust.depart_time)

	    # NAVIGATION
        self.passenger_info_1.setText("Name: " + self.cust.name + "\n" + "Flight: " + self.cust.flight + "\n"
        "Gate: " + self.cust.gate + "\n" + "Departure time: " + self.cust.depart_time)

        # PAUSE
        self.passenger_info_2.setText("Name: " + self.cust.name + "\n" + "Flight: " + self.cust.flight + "\n"
        "Gate: " + self.cust.gate + "\n" + "Departure time: " + self.cust.depart_time)

        if self.currentWidget() == self.SCAN: self.setCurrentWidget(self.SUCCESS)

        QtTest.QTest.qWait(2000)

        if self.currentWidget() == self.SUCCESS: self.setCurrentWidget(self.INFO)

    
    def navigate(self, location):

        self.setCurrentWidget(self.NAVIGATING)

        QtTest.QTest.qWait(1000)
        
        # os.system(" python ~/Desktop/Demo2/Navigation/go_to_specific_point_on_map.py {}".format(self.cust.gate))
        os.system(" python ~/Desktop/Demo2/sdp-ian/Navigation/go_and_stay.py {}".format(self.cust.gate))
        self.pause_navigation.clicked.connect(lambda: self.pause(location))

        # QtTest.QTest.qWait(6000)
        # self.setCurrentWidget(self.COMPLETE)

    def pause(self, location):

        self.setCurrentWidget(self.PAUSE)
        QtTest.QTest.qWait(100)
        os.system(" python ~/Desktop/Demo2/sdp-ian/Navigation/pause.py")
	
        self.pause_new_goal.clicked.connect(lambda: self.setCurrentWidget(self.WHERE))
        self.resume_navigation.clicked.connect(lambda: self.navigate(location))


def main():
    os.system(" python ~/Desktop/Demo2/sdp-ian/Navigation/publish_initial_pos.py")
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('plastique')
    model = IanUiModel()
    view = IanUi()
    view.show()
    IanUiController(model=model, view=view)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
