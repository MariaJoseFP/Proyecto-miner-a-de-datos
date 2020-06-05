# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaEnsamble.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ensamble(object):
    def setupUi(self, Ensamble):
        Ensamble.setObjectName("Ensamble")
        Ensamble.resize(512, 854)
        Ensamble.setStyleSheet("#Ensamble{\n"
"        background-color: rgb(250, 255, 230);\n"
"\n"
"    }\n"
"\n"
"QPushButton{\n"
"     background-color: #ff5722;\n"
"        color: #ffffff;\n"
"          font: inherit;\n"
"          margin: 0;\n"
"        border-radius:5px;\n"
"    }\n"
"    \n"
"    QPushButton:hover{\n"
"    background-color:#78788c;\n"
"    color:#ffffff\n"
"    }\n"
"\n"
"\n"
"QLineEdit{\n"
"   /* background: rgba(0,0,0,0.2);*/\n"
"background-color:#ffffff;\n"
"  height: 50px;\n"
"  width: 100%;\n"
"  margin: 10px 0;\n"
"  padding: 0 10px;\n"
"  border-width: 0;\n"
"  border: none;\n"
"}\n"
"QLabel{\n"
"\n"
"margin:28px 0 0;font-size:14px;/*color:#5a5a5a*/\n"
"    color:#000000\n"
"}")
        self.gridLayoutWidget = QtWidgets.QWidget(Ensamble)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 70, 452, 730))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setStyleSheet("text-decoration: underline;\n"
"margin:28px 0 0;font-size:20px;/*color:#5a5a5a*/\n"
"color:#000000")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setStyleSheet("text-decoration: underline;\n"
"margin:28px 0 0;font-size:20px;/*color:#5a5a5a*/\n"
"color:#000000")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("text-decoration: underline;\n"
"margin:28px 0 0;font-size:20px;/*color:#5a5a5a*/\n"
"color:#000000")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.no_vecinos = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.no_vecinos.setMaximumSize(QtCore.QSize(3000, 50))
        self.no_vecinos.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.no_vecinos.setMaxLength(32762)
        self.no_vecinos.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.no_vecinos.setAlignment(QtCore.Qt.AlignCenter)
        self.no_vecinos.setObjectName("no_vecinos")
        self.verticalLayout_4.addWidget(self.no_vecinos)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.Button_predecir = QtWidgets.QPushButton(Ensamble)
        self.Button_predecir.setGeometry(QtCore.QRect(220, 810, 101, 31))
        self.Button_predecir.setObjectName("Button_predecir")
        self.label_2 = QtWidgets.QLabel(Ensamble)
        self.label_2.setGeometry(QtCore.QRect(160, -10, 201, 71))
        self.label_2.setStyleSheet("color: #ff5722;\n"
"font: 26pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Ensamble)
        QtCore.QMetaObject.connectSlotsByName(Ensamble)

    def retranslateUi(self, Ensamble):
        _translate = QtCore.QCoreApplication.translate
        Ensamble.setWindowTitle(_translate("Ensamble", "Ensamble"))
        self.label_9.setText(_translate("Ensamble", "°Naive Bayes"))
        self.label_7.setText(_translate("Ensamble", "°Árbol"))
        self.label.setText(_translate("Ensamble", "°KNN"))
        self.label_11.setText(_translate("Ensamble", "Número de vecinos:"))
        self.label_8.setText(_translate("Ensamble", "Elemento a clasificar:"))
        self.Button_predecir.setText(_translate("Ensamble", "Predecir"))
        self.label_2.setText(_translate("Ensamble", "Ensamble"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ensamble = QtWidgets.QWidget()
    ui = Ui_Ensamble()
    ui.setupUi(Ensamble)
    Ensamble.show()
    sys.exit(app.exec_())

