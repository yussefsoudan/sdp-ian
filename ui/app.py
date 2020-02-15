import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class stackedExample(QWidget):

   def __init__(self):
      super(stackedExample, self).__init__()


      self.stack1 = QWidget()
      self.stack2 = QWidget()
      self.stack3 = QWidget()
      self.stack4 = QWidget()
      self.stack5 = QWidget()
      self.stack6 = QWidget()

      self.stack1UI()
      self.stack2UI()
      self.stack3UI()
      self.stack4UI()
      self.stack5UI()
      self.stack6UI()

      self.Stack = QStackedWidget (self)
      self.Stack.addWidget (self.stack1)
      self.Stack.addWidget (self.stack2)
      self.Stack.addWidget (self.stack3)
      self.Stack.addWidget (self.stack4)
      self.Stack.addWidget (self.stack5)
      self.Stack.addWidget (self.stack6)


      hbox = QHBoxLayout(self)
      #hbox.addWidget(self.leftlist)
      hbox.addWidget(self.Stack)



      self.setLayout(hbox)

      self.setGeometry(300, 300, 1000,700)
      self.setStyleSheet("background-color: #FFFFFF;")
      self.show()

   def click(self):
       self.Stack.setCurrentWidget(self.stack3)

   def click2(self):
       self.Stack.setCurrentWidget(self.stack4)

   def click3(self):
       self.Stack.setCurrentWidget(self.stack2)

   def stack1UI(self):
      layout = QVBoxLayout()
      button = QPushButton('Start')
      button.setGeometry(0,0, 100,100)

      button.setStyleSheet("background-color: #FFFFFF;font-size:100px;font-family:Avenir;")
      l3 = QLabel()
      pixmap = QPixmap('logoPic.jpg')
      #icon = QIcon('logoPic.jpg')
      pixmap2 = pixmap.scaledToWidth(1000)
      #button.setIcon(icon)
      l3.setPixmap(pixmap2)
      #pixmap.resize(10,10)

      layout.addWidget(l3)
      layout.addWidget(button)

      #layout.addStretch(1)


      button.clicked.connect(self.click)


      #self.setTabText(0,"Contact Details")
      self.stack1.setLayout(layout)
      #self.resize(pixmap.width(),pixmap.height())

   def stack2UI(self):
      layout = QVBoxLayout()

      label = QLabel()
      label.setText('Go Somewhere?')
      label.setAlignment(Qt.AlignCenter)
      label.setStyleSheet("font-size:50px;font-family:Avenir;")
      layout.addWidget(label)
      #button.clicked.connect(self.click2)

      layoutH = QHBoxLayout()
      button1 = QPushButton('Gate')
      button1.setStyleSheet("font-size:70px;font-family:Avenir;")
      button2 = QPushButton('Toilets')
      button2.setStyleSheet("font-size:70px;font-family:Avenir;")
      button3 = QPushButton('Shops')
      button3.setStyleSheet("font-size:70px;font-family:Avenir;")
      layoutH.addWidget(button1)
      layoutH.addWidget(button2)
      layoutH.addWidget(button3)

      layout.addLayout(layoutH)

      self.stack2.setLayout(layout)

   def stack3UI(self):
      layout = QVBoxLayout()

      label = QLabel()
      label.setText('Please Scan Your Boarding Pass')
      label.setStyleSheet("font-size:50px;font-family:Avenir;")
      label.setAlignment(Qt.AlignCenter)
      layout.addWidget(label)

      button1 = QPushButton('Done')
      button1.setStyleSheet("background-color: #FFFFFF;font-size:30px;font-family:Avenir;")

      layout.addWidget(button1)
      button1.clicked.connect(self.click3)

      self.stack3.setLayout(layout)

   def stack4UI(self):
      layout = QHBoxLayout()
      button1 = QPushButton('Gate')
      button2 = QPushButton('Toilets')
      button3 = QPushButton('Shops')
      layout.addWidget(button1)
      layout.addWidget(button2)
      layout.addWidget(button3)
      self.stack4.setLayout(layout)

   def stack5UI(self):
      layout = QHBoxLayout()
      button1 = QPushButton('Gate')
      button2 = QPushButton('Toilets')
      button3 = QPushButton('Shops')
      layout.addWidget(button1)
      layout.addWidget(button2)
      layout.addWidget(button3)
      self.stack5.setLayout(layout)

   def stack6UI(self):
      layout = QHBoxLayout()
      button1 = QPushButton('Gate')
      button2 = QPushButton('Toilets')
      button3 = QPushButton('Shops')
      layout.addWidget(button1)
      layout.addWidget(button2)
      layout.addWidget(button3)
      self.stack6.setLayout(layout)

   #def display(self,i):
      #self.Stack.setCurrentIndex(i)

def main():
   app = QApplication(sys.argv)
   ex = stackedExample()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
