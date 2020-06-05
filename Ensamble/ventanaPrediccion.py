# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaPrediccion.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Prediccion(object):
    def setupUi(self, Prediccion):
        Prediccion.setObjectName("Prediccion")
        Prediccion.resize(576, 385)
        Prediccion.setStyleSheet("#Prediccion{\n"
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
        self.verticalLayoutWidget = QtWidgets.QWidget(Prediccion)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 80, 161, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Prediccion)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 80, 161, 181))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cb = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.cb.setText("")
        self.cb.setObjectName("cb")
        self.verticalLayout_2.addWidget(self.cb)
        self.ca = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.ca.setText("")
        self.ca.setObjectName("ca")
        self.verticalLayout_2.addWidget(self.ca)
        self.cknn = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.cknn.setText("")
        self.cknn.setObjectName("cknn")
        self.verticalLayout_2.addWidget(self.cknn)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Prediccion)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(400, 80, 161, 181))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pb = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.pb.setText("")
        self.pb.setObjectName("pb")
        self.verticalLayout_3.addWidget(self.pb)
        self.pa = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.pa.setText("")
        self.pa.setObjectName("pa")
        self.verticalLayout_3.addWidget(self.pa)
        self.pknn = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.pknn.setText("")
        self.pknn.setObjectName("pknn")
        self.verticalLayout_3.addWidget(self.pknn)
        self.label_4 = QtWidgets.QLabel(Prediccion)
        self.label_4.setGeometry(QtCore.QRect(210, 20, 81, 51))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"color: #ff5722;")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_11 = QtWidgets.QLabel(Prediccion)
        self.label_11.setGeometry(QtCore.QRect(390, 20, 111, 51))
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"color: #ff5722;\n"
"")
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Prediccion)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 300, 160, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cnv = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.cnv.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.cnv.setAlignment(QtCore.Qt.AlignCenter)
        self.cnv.setObjectName("cnv")
        self.horizontalLayout.addWidget(self.cnv)
        self.clase = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.clase.setText("")
        self.clase.setObjectName("clase")
        self.horizontalLayout.addWidget(self.clase)
        self.label_5 = QtWidgets.QLabel(Prediccion)
        self.label_5.setGeometry(QtCore.QRect(60, 0, 71, 91))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("md.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Prediccion)
        self.label_6.setGeometry(QtCore.QRect(460, 250, 51, 81))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("grafica.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.Button_grafica = QtWidgets.QPushButton(Prediccion)
        self.Button_grafica.setGeometry(QtCore.QRect(450, 340, 93, 28))
        self.Button_grafica.setObjectName("Button_grafica")
        self.archivo = QtWidgets.QLabel(Prediccion)
        self.archivo.setGeometry(QtCore.QRect(210, 20, 16, 16))
        self.archivo.setText("")
        self.archivo.setObjectName("archivo")

        self.retranslateUi(Prediccion)
        QtCore.QMetaObject.connectSlotsByName(Prediccion)

    def retranslateUi(self, Prediccion):
        _translate = QtCore.QCoreApplication.translate
        Prediccion.setWindowTitle(_translate("Prediccion", "Clasificador prediccción"))
        self.label_2.setText(_translate("Prediccion", "Naive bayes"))
        self.label.setText(_translate("Prediccion", "Árbol"))
        self.label_3.setText(_translate("Prediccion", "K-Nearest-Neighbor"))
        self.label_4.setText(_translate("Prediccion", "Clase"))
        self.label_11.setText(_translate("Prediccion", "Probabilidad"))
        self.cnv.setText(_translate("Prediccion", "Clase:"))
        self.Button_grafica.setText(_translate("Prediccion", "Mostrar gráfica"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Prediccion = QtWidgets.QWidget()
    ui = Ui_Prediccion()
    ui.setupUi(Prediccion)
    Prediccion.show()
    sys.exit(app.exec_())

