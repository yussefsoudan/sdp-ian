# Links up the UI buttons, and controls the scanning and navigation processes. It is the Controller of the program.

class IanUiController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # Connect signals and slots
        self.connectButtons()

    def connectButtons(self):

        # START
        self.view.start.clicked.connect(lambda: self.model.scan(self.view))

        # INFO
        self.view.go_somewhere.clicked.connect(lambda: self.view.setCurrentWidget(self.view.WHERE))
        self.view.back_to_start.clicked.connect(lambda: self.view.setCurrentWidget(self.view.START))

        # WHERE
        self.view.gate.clicked.connect(lambda: self.model.chooseDestination(self.view, "Gate " + self.model.cust.gate, self.view.WHERE))
        self.view.toilet.clicked.connect(lambda: self.model.chooseDestination(self.view, "Toilets", self.view.WHERE))
        self.view.food.clicked.connect(lambda: self.view.setCurrentWidget(self.view.FOOD))
        self.view.shop.clicked.connect(lambda: self.view.setCurrentWidget(self.view.SHOPS))
        self.view.back_to_info.clicked.connect(lambda: self.view.setCurrentWidget(self.view.INFO))

        # FOOD
        self.view.bburr_food.clicked.connect(lambda: self.model.chooseDestination(self.view, "Bar Burrito", self.view.FOOD))
        self.view.bking_food.clicked.connect(lambda: self.model.chooseDestination(self.view, "Burger King", self.view.FOOD))
        self.view.kk_food.clicked.connect(lambda: self.model.chooseDestination(self.view, "Krispy Kreme", self.view.FOOD))
        self.view.yo_food.clicked.connect(lambda: self.model.chooseDestination(self.view, "Yo-Sushi", self.view.FOOD))
        self.view.caffenero_food.clicked.connect(lambda: self.model.chooseDestination(self.view, "Caffe Nero", self.view.FOOD))
        self.view.pret_food.clicked.connect(lambda: self.model.chooseDestination(self.view, "Pret A Manger", self.view.FOOD))
        self.view.back_to_where_food.clicked.connect(lambda: self.view.setCurrentWidget(self.view.WHERE))

        # SHOPS
        self.view.whs_shop.clicked.connect(lambda: self.model.chooseDestination(self.view, "WHSmith", self.view.SHOPS))
        self.view.next_shop.clicked.connect(lambda: self.model.chooseDestination(self.view, "Next", self.view.SHOPS))
        self.view.dutyfree_shop.clicked.connect(lambda: self.model.chooseDestination(self.view, "World Duty Free", self.view.SHOPS))
        self.view.superdrug_shop.clicked.connect(lambda: self.model.chooseDestination(self.view, "Superdrug", self.view.SHOPS))
        self.view.mns_shop.clicked.connect(lambda: self.model.chooseDestination(self.view, "M&S", self.view.SHOPS))
        self.view.hugoboss_shop.clicked.connect(lambda: self.model.chooseDestination(self.view, "Hugo Boss", self.view.SHOPS))
        self.view.back_to_where_shops.clicked.connect(lambda: self.view.setCurrentWidget(self.view.WHERE))

        # CONFIRM_DEST


        # COMPLETE
        self.view.more_help.clicked.connect(lambda: self.view.setCurrentWidget(self.view.SCAN))
        self.view.no_more_help.clicked.connect(lambda: self.model.exit(self.view, self.view.COMPLETE))

        # Help buttons
        self.view.info_1.clicked.connect(lambda: self.model.help(self.view, self.view.SCAN))
        self.view.info_2.clicked.connect(lambda: self.model.help(self.view, self.view.INFO))
        self.view.info_3.clicked.connect(lambda: self.model.help(self.view, self.view.WHERE))
        self.view.info_4.clicked.connect(lambda: self.model.help(self.view, self.view.FOOD))
        self.view.info_5.clicked.connect(lambda: self.model.help(self.view, self.view.SHOPS))
        self.view.info_6.clicked.connect(lambda: self.model.help(self.view, self.view.CONFIRM_DEST))
        self.view.info_7.clicked.connect(lambda: self.model.help(self.view, self.view.NAVIGATING))
        self.view.info_8.clicked.connect(lambda: self.model.help(self.view, self.view.PAUSE))
        self.view.info_9.clicked.connect(lambda: self.model.help(self.view, self.view.COMPLETE))

        # Exit buttons
        self.view.exit_1.clicked.connect(lambda: self.model.exit(self.view, self.view.SCAN))
        self.view.exit_2.clicked.connect(lambda: self.model.exit(self.view, self.view.INFO))
        self.view.exit_3.clicked.connect(lambda: self.model.exit(self.view, self.view.WHERE))
        self.view.exit_4.clicked.connect(lambda: self.model.exit(self.view, self.view.FOOD))
        self.view.exit_5.clicked.connect(lambda: self.model.exit(self.view, self.view.SHOPS))
        self.view.exit_6.clicked.connect(lambda: self.model.exit(self.view, self.view.CONFIRM_DEST))
        self.view.exit_7.clicked.connect(lambda: self.model.exit(self.view, self.view.NAVIGATING))
        self.view.exit_8.clicked.connect(lambda: self.model.exit(self.view, self.view.PAUSE))
        self.view.exit_9.clicked.connect(lambda: self.model.exit(self.view, self.view.COMPLETE))

        self.view.cancel_exit.clicked.connect(lambda: self.view.setCurrentWidget(self.view.START))
        self.view.exit_button.clicked.connect(lambda: self.view.setCurrentWidget(self.view.START))

        self.view.yes_go.clicked.connect(lambda: self.model.navigate(self.view))
        self.view.pause_navigation.clicked.connect(lambda: self.model.pause(self.view))

        self.view.pause_new_goal.clicked.connect(lambda: self.view.setCurrentWidget(self.view.WHERE))
        self.view.resume_navigation.clicked.connect(lambda: self.model.navigate(self.view))
