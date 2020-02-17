import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic


qtcreator_file  = "the.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QStackedWidget, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QStackedWidget.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.setCurrentWidget(self.START)


        self.start.clicked.connect(lambda: self.StartScanning())

        # for testing
        self.next_scan.clicked.connect(lambda: self.setCurrentWidget(self.SUCCESS))
        self.next_success.clicked.connect(lambda: self.setCurrentWidget(self.INFO))

        self.go_somewhere.clicked.connect(lambda: self.setCurrentWidget(self.WHERE))
        self.back_to_info.clicked.connect(lambda: self.setCurrentWidget(self.INFO))

        self.gate.clicked.connect(lambda: self.ChooseDestination("Gate"))
        self.toilet.clicked.connect(lambda: self.ChooseDestination("Toilets"))
        self.food.clicked.connect(lambda: self.setCurrentWidget(self.FOOD))
        self.shop.clicked.connect(lambda: self.setCurrentWidget(self.SHOPS))
        self.mcd_food.clicked.connect(lambda: self.ChooseDestination("McDonalds"))
        self.bburr_food.clicked.connect(lambda: self.ChooseDestination("Bar Burrito"))
        self.whs_shop.clicked.connect(lambda: self.ChooseDestination("WHSmith"))
        self.next_shop.clicked.connect(lambda: self.ChooseDestination("Next"))

        self.not_correct.clicked.connect(lambda: self.setCurrentWidget(self.WHERE))
        self.yes_go.clicked.connect(lambda: self.setCurrentWidget(self.NAVIGATING))

        self.cancel_navigation.clicked.connect(lambda: self.setCurrentWidget(self.INFO))


    def StartScanning(self):
        self.setCurrentWidget(self.SCAN)



    def ChooseDestination(self, location):
        self.setCurrentWidget(self.CONFIRM_DEST)
        self.destination_label.setText(location + "?")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
