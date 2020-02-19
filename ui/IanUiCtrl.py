# The Controller class to connect the GUI and the model
class IanUiController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # Connect signals and slots
        self.connectSignals()
    
    def connectSignals(self):
        print(1)
    #     """Connect signals and slots."""
    #     for btnText, btn in self._view.buttons.items():
    #         if btnText not in {'=', 'C'}:
    #             btn.clicked.connect(partial(self._buildExpression, btnText))

    #     self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
    