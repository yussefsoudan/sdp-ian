import sys, time
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest, uic

class Customer:

    name = "Joe Blogs"
    flight = "AA100"
    gate = "7"
    depart_time = "15:00"

qtcreator_file  = "the.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QStackedWidget, Ui_MainWindow):

    cust = Customer()

    def __init__(self):
        QtWidgets.QStackedWidget.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setCurrentWidget(self.START)

        # START
        self.start.clicked.connect(lambda: self.scan())

        # for testing
        self.next_scan.clicked.connect(lambda: self.setCurrentWidget(self.SUCCESS))
        self.next_success.clicked.connect(lambda: self.setCurrentWidget(self.INFO))
        # end

        # INFO
        self.go_somewhere.clicked.connect(lambda: self.setCurrentWidget(self.WHERE))
        self.back_to_info.clicked.connect(lambda: self.setCurrentWidget(self.INFO))

        # WHERE
        self.gate.clicked.connect(lambda: self.chooseDestination("Gate " + self.cust.gate, self.WHERE))

        self.toilet.clicked.connect(lambda: self.chooseDestination("Toilets", self.WHERE))

        self.food.clicked.connect(lambda: self.setCurrentWidget(self.FOOD))
        # self.back_to_where_food.clicked.connect(lambda: self.setCurrentWidget(self.WHERE))

        self.shop.clicked.connect(lambda: self.setCurrentWidget(self.SHOPS))
        # self.back_to_where_shops.clicked.connect(lambda: self.setCurrentWidget(self.WHERE))

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
        self.not_correct.clicked.connect(lambda: self.setCurrentWidget(self.WHERE))

        # NAVIGATION

        # PAUSE

        # Help buttons
        self.info_1.clicked.connect(lambda: self.setCurrentWidget(self.HELP))
        self.info_2.clicked.connect(lambda: self.setCurrentWidget(self.HELP))
        self.info_3.clicked.connect(lambda: self.setCurrentWidget(self.HELP))
        self.info_4.clicked.connect(lambda: self.setCurrentWidget(self.HELP))
        self.info_5.clicked.connect(lambda: self.setCurrentWidget(self.HELP))
        self.info_6.clicked.connect(lambda: self.setCurrentWidget(self.HELP))
        self.info_7.clicked.connect(lambda: self.setCurrentWidget(self.HELP))


    def scan(self):

        self.setCurrentWidget(self.SCAN)

        # scan here

        self.name_label.setText("Name: " + self.cust.name)
        self.flight_label.setText("Flight: " + self.cust.flight)
        self.gate_label.setText("Gate: " + self.cust.gate)
        self.depart_time_label.setText("Departure time: " + self.cust.depart_time)

        QtTest.QTest.qWait(2000)

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

        # navigate here

    def navigate(self, location):

        self.setCurrentWidget(self.NAVIGATING)
        self.pause_navigation.clicked.connect(lambda: self.setCurrentWidget(self.PAUSE))
        self.resume_navigation.clicked.connect(lambda: self.setCurrentWidget(self.NAVIGATING))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
    sys.exit()
