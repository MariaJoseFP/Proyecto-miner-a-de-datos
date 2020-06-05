# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaBayes.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Bayes(object):
    def setupUi(self, Bayes):
        Bayes.setObjectName("Bayes")
        Bayes.resize(470, 770)
        Bayes.setStyleSheet("#Bayes{\n"
"        background-color: rgb(250, 255, 230);\n"
"        font-family: 10pt \"MS Shell Dlg 2\";\n"
"    }\n"
"QPushButton{\n"
"        background-color: #ff5722;\n"
"          font: inherit;\n"
"        color: #ffffff;\n"
"        border-radius:3px;\n"
"        font-size:15px;\n"
"    }\n"
"    \n"
"    /*Definimos el estilo para un efecto hover sobre el botón,\n"
"    este cambiará su background cuando pasemos el mouse por\n"
"    encima*/\n"
"    QPushButton:hover{\n"
"    background-color:#78788c;\n"
"    color:#ffffff;\n"
"    }\n"
"QLineEdit,QTextBrowser{\n"
"   /*background: rgba(0,0,0,0.2);*/\n"
"background-color:#ffffff;\n"
"  height: 50px;\n"
"  width: 100%;\n"
"  margin: 10px 0;\n"
"  padding: 0 10px;\n"
"  border-width: 0;\n"
"  border: none;\n"
"  outline: none;\n"
"}\n"
"QSpinBox{\n"
"border: none;\n"
"}")
        self.label_4 = QtWidgets.QLabel(Bayes)
        self.label_4.setGeometry(QtCore.QRect(170, 450, 101, 21))
        self.label_4.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.Button_predecir = QtWidgets.QPushButton(Bayes)
        self.Button_predecir.setGeometry(QtCore.QRect(160, 620, 111, 31))
        self.Button_predecir.setObjectName("Button_predecir")
        self.label_3 = QtWidgets.QLabel(Bayes)
        self.label_3.setGeometry(QtCore.QRect(110, 80, 221, 21))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Bayes)
        self.label_5.setGeometry(QtCore.QRect(160, 490, 151, 41))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(Bayes)
        self.label_10.setGeometry(QtCore.QRect(160, 290, 131, 41))
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(Bayes)
        self.label_6.setGeometry(QtCore.QRect(60, 590, 201, 21))
        self.label_6.setObjectName("label_6")
        self.verticalLayoutWidget = QtWidgets.QWidget(Bayes)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 180, 311, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_presicion1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_presicion1.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_presicion1.setText("")
        self.label_presicion1.setObjectName("label_presicion1")
        self.verticalLayout.addWidget(self.label_presicion1)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_presicion2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_presicion2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_presicion2.setText("")
        self.label_presicion2.setObjectName("label_presicion2")
        self.verticalLayout.addWidget(self.label_presicion2)
        self.label_matriz = QtWidgets.QTextBrowser(Bayes)
        self.label_matriz.setGeometry(QtCore.QRect(140, 320, 171, 121))
        self.label_matriz.setObjectName("label_matriz")
        self.label = QtWidgets.QLabel(Bayes)
        self.label.setGeometry(QtCore.QRect(130, 40, 181, 41))
        self.label.setStyleSheet("color: #ff5722;\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.Button_presicion = QtWidgets.QPushButton(Bayes)
        self.Button_presicion.setGeometry(QtCore.QRect(130, 110, 191, 41))
        self.Button_presicion.setObjectName("Button_presicion")
        self.lineEdit = QtWidgets.QLineEdit(Bayes)
        self.lineEdit.setGeometry(QtCore.QRect(60, 540, 351, 41))
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(52767)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayoutWidget = QtWidgets.QWidget(Bayes)
        self.formLayoutWidget.setGeometry(QtCore.QRect(100, 700, 211, 31))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_clase = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_clase.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_clase.setText("")
        self.label_clase.setObjectName("label_clase")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_clase)

        self.retranslateUi(Bayes)
        QtCore.QMetaObject.connectSlotsByName(Bayes)

    def retranslateUi(self, Bayes):
        _translate = QtCore.QCoreApplication.translate
        Bayes.setWindowTitle(_translate("Bayes", "Naive Bayes"))
        self.label_4.setText(_translate("Bayes", "Predicción"))
        self.Button_predecir.setText(_translate("Bayes", "Predecir clase"))
        self.label_5.setText(_translate("Bayes", "Nuevo elemento: "))
        self.label_10.setText(_translate("Bayes", "Matriz de confusión:"))
        self.label_6.setText(_translate("Bayes", "*Atributos separados por comas "))
        self.label_8.setText(_translate("Bayes", "Precisión con el conjunto de entrenamiento:"))
        self.label_9.setText(_translate("Bayes", "Precisión con el conjunto de prueba:"))
        self.label.setText(_translate("Bayes", "Naive bayes"))
        self.Button_presicion.setText(_translate("Bayes", "Calcular precisión"))
        self.label_7.setText(_translate("Bayes", "Clase asignada:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bayes = QtWidgets.QWidget()
    ui = Ui_Bayes()
    ui.setupUi(Bayes)
    Bayes.show()
    sys.exit(app.exec_())

