# Form implementation generated from reading ui file 'Security_Tool.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 311)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 401, 311))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(70, 50, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 60, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(10, 30, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 61, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 221, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser.setGeometry(QtCore.QRect(10, 100, 341, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab_3, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 40, 211, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 49, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 49, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 49, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 70, 211, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 70, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_4, "")

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 30, 75, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 30, 211, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.tab_5)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 49, 16))
        self.label_6.setObjectName("label_6")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_5)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 110, 256, 192))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_7 = QtWidgets.QLabel(self.tab_5)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 49, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_5)
        self.label_8.setGeometry(QtCore.QRect(10, 0, 81, 16))
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab_5, "")

        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")

        # First time use Stylesheet
        Form.setStyleSheet("""
            QWidget {
                background-color: #8ED6FF;
            }
            QPushButton {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #8ED6FF, stop: 1 #004D99);
                border-radius: 6px;
                padding: 5px;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #004D99, stop: 1 #8ED6FF);
            }
            QLineEdit {
                background-color: #BFE7FF;
            }
            QTabBar:tab { 
                background: gray; color: white; padding: 10px; 
            }
            QTabBar:tab:selected { 
                background: lightgray; 
                }
            QTabWidget {
                border: 1, solid;
                border-color: #BFE7FF
            }
        """)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)  # Show the first tab when the program starts.
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        # Form.setWindowTitle(_translate("Form", "Form"))
        
        Form.setWindowTitle('CYBR-260-40 WEEK-02 Grade Calculator')

        self.pushButton.setText(_translate("Form", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.label.setText(_translate("Form", "IP Range"))
        self.label_2.setText(_translate("Form", "SCAN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Tab 3"))
        self.label_3.setText(_translate("Form", "SCAN"))
        self.label_4.setText(_translate("Form", "Host"))
        self.label_5.setText(_translate("Form", "Port(s)"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Tab 4"))
        self.pushButton_4.setText(_translate("Form", "PushButton"))
        self.label_6.setText(_translate("Form", "Host"))
        self.label_7.setText(_translate("Form", "Status"))
        self.label_8.setText(_translate("Form", "Destination"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Tab 5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "Tab 6"))



        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
