# Links up the UI buttons, and controls the scanning and navigation processes. It is the Controller of the program.

class IanUiController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # Connect signals and slots
        self.connectSignals()
    
    def connectSignals(self):
        pass
    #     """Connect signals and slots."""
    #     for btnText, btn in self._view.buttons.items():
    #         if btnText not in {'=', 'C'}:
    #             btn.clicked.connect(partial(self._buildExpression, btnText))

    #     self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
    