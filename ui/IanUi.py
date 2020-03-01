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

        # START
        self.start.clicked.connect(lambda: self.scan())

        # INFO
        self.go_somewhere.clicked.connect(lambda: self.setCurrentWidget(self.WHERE))
        self.back_to_start.clicked.connect(lambda: self.setCurrentWidget(self.START))

        # WHERE
        self.gate.clicked.connect(lambda: self.chooseDestination("Gate " + self.cust.gate, self.WHERE))

        self.toilet.clicked.connect(lambda: self.chooseDestination("Toilets", self.WHERE))

        self.food.clicked.connect(lambda: self.setCurrentWidget(self.FOOD))
        # self.back_to_where_food.clicked.connect(lambda: self.setCurrentWidget(self.WHERE))

        self.shop.clicked.connect(lambda: self.setCurrentWidget(self.SHOPS))
        # self.back_to_where_shops.clicked.connect(lambda: self.setCurrentWidget(self.WHERE))

        self.back_to_info.clicked.connect(lambda: self.setCurrentWidget(self.INFO))



        # FOOD
        self.bburr_food.clicked.connect(lambda: self.chooseDestination("Bar Burrito", self.FOOD))
        self.bking_food.clicked.connect(lambda: self.chooseDestination("Burger King", self.FOOD))
        self.kk_food.clicked.connect(lambda: self.chooseDestination("Krispy Kreme", self.FOOD))
        self.yo_food.clicked.connect(lambda: self.chooseDestination("Yo-Sushi", self.FOOD))
        self.caffenero_food.clicked.connect(lambda: self.chooseDestination("Caffe Nero", self.FOOD))
        self.eat_food.clicked.connect(lambda: self.chooseDestination("Eat.", self.FOOD))
        self.pret_food.clicked.connect(lambda: self.chooseDestination("Pret A Manger", self.FOOD))
        self.brewdog_food.clicked.connect(lambda: self.chooseDestination("Brewdog", self.FOOD))
        self.back_to_where_food.clicked.connect(lambda: self.setCurrentWidget(self.WHERE))

        # SHOPS
        self.whs_shop.clicked.connect(lambda: self.chooseDestination("WHSmith", self.SHOPS))
        self.next_shop.clicked.connect(lambda: self.chooseDestination("Next", self.SHOPS))
        self.dutyfree_shop.clicked.connect(lambda: self.chooseDestination("World Duty Free", self.SHOPS))
        self.superdrug_shop.clicked.connect(lambda: self.chooseDestination("Superdrug", self.SHOPS))
        self.mns_shop.clicked.connect(lambda: self.chooseDestination("M&S", self.SHOPS))
        self.fatface_shop.clicked.connect(lambda: self.chooseDestination("Fatface", self.SHOPS))
        self.accessorize_shop.clicked.connect(lambda: self.chooseDestination("Accessorize", self.SHOPS))
        self.hugoboss_shop.clicked.connect(lambda: self.chooseDestination("Hugo Boss", self.SHOPS))
        self.back_to_where_shops.clicked.connect(lambda: self.setCurrentWidget(self.WHERE))

        # CONFIRM_DEST




        # COMPLETE

        self.more_help.clicked.connect(lambda: self.setCurrentWidget(self.SCAN))
        self.no_more_help.clicked.connect(lambda: self.exit(self.COMPLETE))

        # Help buttons
        self.info_1.clicked.connect(lambda: self.help(self.SCAN))
        self.info_2.clicked.connect(lambda: self.help(self.INFO))
        self.info_3.clicked.connect(lambda: self.help(self.WHERE))
        self.info_4.clicked.connect(lambda: self.help(self.FOOD))
        self.info_5.clicked.connect(lambda: self.help(self.SHOPS))
        self.info_6.clicked.connect(lambda: self.help(self.CONFIRM_DEST))
        self.info_7.clicked.connect(lambda: self.help(self.NAVIGATING))
        self.info_8.clicked.connect(lambda: self.help(self.PAUSE))
        self.info_9.clicked.connect(lambda: self.help(self.COMPLETE))

        # Exit buttons
        self.exit_1.clicked.connect(lambda: self.exit(self.SCAN))
        self.exit_2.clicked.connect(lambda: self.exit(self.INFO))
        self.exit_3.clicked.connect(lambda: self.exit(self.WHERE))
        self.exit_4.clicked.connect(lambda: self.exit(self.FOOD))
        self.exit_5.clicked.connect(lambda: self.exit(self.SHOPS))
        self.exit_6.clicked.connect(lambda: self.exit(self.CONFIRM_DEST))
        self.exit_7.clicked.connect(lambda: self.exit(self.NAVIGATING))
        self.exit_8.clicked.connect(lambda: self.exit(self.PAUSE))
        self.exit_9.clicked.connect(lambda: self.exit(self.COMPLETE))


        self.cancel_exit.clicked.connect(lambda: self.setCurrentWidget(self.START))
        self.exit_button.clicked.connect(lambda: self.setCurrentWidget(self.START))

    def help(self, previous_widget):
        self.setCurrentWidget(self.HELP)


        self.help_back.clicked.connect(lambda: self.setCurrentWidget(previous_widget))

    def exit(self, previous_widget):
        self.setCurrentWidget(self.EXIT)
        self.cancel_exit.clicked.connect(lambda: self.setCurrentWidget(previous_widget))
        self.exit_button.clicked.connect(lambda: self.go_hub())


    def scan(self):

        self.setCurrentWidget(self.SCAN)

        QtTest.QTest.qWait(1000)

        os.system("python ~/Desktop/Demo2/Scanning/realtime.py")
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



    def chooseDestination(self, location, previous_widget):

        self.setCurrentWidget(self.CONFIRM_DEST)
        self.destination_label.setText(location + "?")
        self.navigating_to_label2.setText(location)
        self.navigating_to_label3.setText(location)
        self.yes_go.clicked.connect(lambda: self.navigate(location))
        self.back_to_prev.clicked.connect(lambda: self.setCurrentWidget(previous_widget))



    def navigate(self, location):

        self.setCurrentWidget(self.NAVIGATING)

        QtTest.QTest.qWait(1000)

        # os.system(" python ~/Desktop/Demo2/Navigation/go_to_specific_point_on_map.py {}".format(self.cust.gate))
	os.system(" python ~/Desktop/Demo2/Navigation/go_and_stay.py {}".format(self.cust.gate))
        self.pause_navigation.clicked.connect(lambda: self.pause(location))

        # QtTest.QTest.qWait(6000)
        # self.setCurrentWidget(self.COMPLETE)

    def pause(self, location):

        self.setCurrentWidget(self.PAUSE)
	QtTest.QTest.qWait(100)
	os.system(" python ~/Desktop/Demo2/Navigation/pause.py")
	
        self.pause_new_goal.clicked.connect(lambda: self.setCurrentWidget(self.WHERE))
        self.resume_navigation.clicked.connect(lambda: self.navigate(location))


def main():
    os.system(" python ~/Desktop/Demo2/Navigation/publish_initial_pos.py")
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('plastique')
    model = IanUiModel()
    view = IanUi()
    view.show()
    IanUiController(model=model, view=view)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
