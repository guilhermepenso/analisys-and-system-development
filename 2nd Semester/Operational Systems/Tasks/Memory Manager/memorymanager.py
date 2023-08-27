from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindows
import sys

def demo():
    app=QApplication(sys.argv)
    win=QMainWindow()
    win.setGeometry(300,300,300,300)
    win.setWindowTittle("Demo app")
    label= QtWidgets.QLabel(win)
    label.setText("Kyosune")
    label.move(100,100)
    
    win.show()
    sys.exit(app.exec_())
    
demo() 