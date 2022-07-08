from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

win=QWidget()
win.setWindowTitle("software name")
win.resize(600,500)

win.show()
sys.exit(app.exec_())