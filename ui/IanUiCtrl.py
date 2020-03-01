# Links up the UI buttons, and controls the scanning and navigation processes. It is the Controller of the program.

class IanUiController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # Connect signals and slots
        self.connectButtons()
    
    def connectButtons(self):

        # START
        self.view.start.clicked.connect(lambda: self.view.scan())

        # INFO
        self.view.go_somewhere.clicked.connect(lambda: self.view.setCurrentWidget(self.view.WHERE))
        self.view.back_to_start.clicked.connect(lambda: self.view.setCurrentWidget(self.view.START))

        # WHERE
        self.view.gate.clicked.connect(lambda: self.chooseDestination("Gate " + self.cust.gate, self.view.WHERE))

        self.view.toilet.clicked.connect(lambda: self.chooseDestination("Toilets", self.view.WHERE))

        self.view.food.clicked.connect(lambda: self.view.setCurrentWidget(self.view.FOOD))

        self.view.shop.clicked.connect(lambda: self.view.setCurrentWidget(self.view.SHOPS))

        self.view.back_to_info.clicked.connect(lambda: self.view.setCurrentWidget(self.view.INFO))

        # FOOD
        self.view.bburr_food.clicked.connect(lambda: self.chooseDestination("Bar Burrito", self.view.FOOD))
        self.view.bking_food.clicked.connect(lambda: self.chooseDestination("Burger King", self.view.FOOD))
        self.view.kk_food.clicked.connect(lambda: self.chooseDestination("Krispy Kreme", self.view.FOOD))
        self.view.yo_food.clicked.connect(lambda: self.chooseDestination("Yo-Sushi", self.view.FOOD))
        self.view.caffenero_food.clicked.connect(lambda: self.chooseDestination("Caffe Nero", self.view.FOOD))
        self.view.eat_food.clicked.connect(lambda: self.chooseDestination("Eat.", self.view.FOOD))
        self.view.pret_food.clicked.connect(lambda: self.chooseDestination("Pret A Manger", self.view.FOOD))
        self.view.brewdog_food.clicked.connect(lambda: self.chooseDestination("Brewdog", self.view.FOOD))
        self.view.back_to_where_food.clicked.connect(lambda: self.view.setCurrentWidget(self.view.WHERE))

        # SHOPS
        self.view.whs_shop.clicked.connect(lambda: self.chooseDestination("WHSmith", self.view.SHOPS))
        self.view.next_shop.clicked.connect(lambda: self.chooseDestination("Next", self.view.SHOPS))
        self.view.dutyfree_shop.clicked.connect(lambda: self.chooseDestination("World Duty Free", self.view.SHOPS))
        self.view.superdrug_shop.clicked.connect(lambda: self.chooseDestination("Superdrug", self.view.SHOPS))
        self.view.mns_shop.clicked.connect(lambda: self.chooseDestination("M&S", self.view.SHOPS))
        self.view.fatface_shop.clicked.connect(lambda: self.chooseDestination("Fatface", self.view.SHOPS))
        self.view.accessorize_shop.clicked.connect(lambda: self.chooseDestination("Accessorize", self.view.SHOPS))
        self.view.hugoboss_shop.clicked.connect(lambda: self.chooseDestination("Hugo Boss", self.view.SHOPS))
        self.view.back_to_where_shops.clicked.connect(lambda: self.view.setCurrentWidget(self.view.WHERE))

        # CONFIRM_DEST


        # COMPLETE

        self.view.more_help.clicked.connect(lambda: self.view.setCurrentWidget(self.view.SCAN))
        self.view.no_more_help.clicked.connect(lambda: self.exit(self.view.COMPLETE))

        # Help buttons
        self.view.info_1.clicked.connect(lambda: self.help(self.view.SCAN))
        self.view.info_2.clicked.connect(lambda: self.help(self.view.INFO))
        self.view.info_3.clicked.connect(lambda: self.help(self.view.WHERE))
        self.view.info_4.clicked.connect(lambda: self.help(self.view.FOOD))
        self.view.info_5.clicked.connect(lambda: self.help(self.view.SHOPS))
        self.view.info_6.clicked.connect(lambda: self.help(self.view.CONFIRM_DEST))
        self.view.info_7.clicked.connect(lambda: self.help(self.view.NAVIGATING))
        self.view.info_8.clicked.connect(lambda: self.help(self.view.PAUSE))
        self.view.info_9.clicked.connect(lambda: self.help(self.view.COMPLETE))

        # Exit buttons
        self.view.exit_1.clicked.connect(lambda: self.exit(self.view.SCAN))
        self.view.exit_2.clicked.connect(lambda: self.exit(self.view.INFO))
        self.view.exit_3.clicked.connect(lambda: self.exit(self.view.WHERE))
        self.view.exit_4.clicked.connect(lambda: self.exit(self.view.FOOD))
        self.view.exit_5.clicked.connect(lambda: self.exit(self.view.SHOPS))
        self.view.exit_6.clicked.connect(lambda: self.exit(self.view.CONFIRM_DEST))
        self.view.exit_7.clicked.connect(lambda: self.exit(self.view.NAVIGATING))
        self.view.exit_8.clicked.connect(lambda: self.exit(self.view.PAUSE))
        self.view.exit_9.clicked.connect(lambda: self.exit(self.view.COMPLETE))

        self.view.cancel_exit.clicked.connect(lambda: self.view.setCurrentWidget(self.view.START))
        self.view.exit_button.clicked.connect(lambda: self.view.setCurrentWidget(self.view.START))




    def help(self, previous_widget):
        self.view.setCurrentWidget(self.HELP)


        self.view.help_back.clicked.connect(lambda: self.view.setCurrentWidget(previous_widget))

    def exit(self, previous_widget):
        self.view.setCurrentWidget(self.view.EXIT)
        self.view.cancel_exit.clicked.connect(lambda: self.view.setCurrentWidget(previous_widget))
        self.view.exit_button.clicked.connect(lambda: self.go_hub())widget):
        self.view.setCurrentWidget(self.view.EXIT)
        self.view.cancel_exit.clicked.connect(lambda: self.view.setCurrentWidget(previous_widget))
        self.view.exit_button.clicked.connect(lambda: self.go_hub())


    def chooseDestination(self, location, previous_widget):

        self.view.setCurrentWidget(self.view.CONFIRM_DEST)
        self.view.destination_label.setText(location + "?")
        self.view.navigating_to_label2.setText(location)
        self.view.navigating_to_label3.setText(location)
        self.view.yes_go.clicked.connect(lambda: self.view.navigate(location))
        self.view.back_to_prev.clicked.connect(lambda: self.view.setCurrentWidget(previous_widget))