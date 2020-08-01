import sys
import tasker
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(598, 451)

        self.updatePos = False

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.posSelecter = QtWidgets.QPushButton(self.centralwidget)
        self.posSelecter.setGeometry(QtCore.QRect(470, 350, 81, 41))
        self.posSelecter.setObjectName("posSelecter")
        self.posSelecter.clicked.connect(self.selectorClick)

        self.posShower = QtWidgets.QLineEdit(self.centralwidget)
        self.posShower.setGeometry(QtCore.QRect(450, 320, 131, 20))
        self.posShower.setObjectName("posShower")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 598, 20))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def selectorClick(self):
        self.updatePos = True

        if tasker.onNextClick():
            x, y = tasker.getPos()
            self.posShower.setText(f"{x}, {y}")
            self.updatePos = False


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Task Helper"))
        self.posSelecter.setText(_translate("MainWindow", "Select Position"))
        if self.updatePos:
            print("true")
            x, y = tasker.getPos()
            self.posShower.setText(f"{x}, {y}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
