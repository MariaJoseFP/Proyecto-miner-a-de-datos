# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaArbol.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Arbol(object):
    def setupUi(self, Arbol):
        Arbol.setObjectName("Arbol")
        Arbol.resize(456, 815)
        Arbol.setStyleSheet("#Arbol{\n"
"        background-color: rgb(250, 255, 230);\n"
"\n"
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
        self.label = QtWidgets.QLabel(Arbol)
        self.label.setGeometry(QtCore.QRect(180, 30, 91, 41))
        self.label.setStyleSheet("color: #ff5722;\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_matriz = QtWidgets.QTextBrowser(Arbol)
        self.label_matriz.setGeometry(QtCore.QRect(140, 360, 181, 131))
        self.label_matriz.setObjectName("label_matriz")
        self.Button_predecir = QtWidgets.QPushButton(Arbol)
        self.Button_predecir.setGeometry(QtCore.QRect(170, 660, 111, 31))
        self.Button_predecir.setObjectName("Button_predecir")
        self.lineEdit = QtWidgets.QLineEdit(Arbol)
        self.lineEdit.setGeometry(QtCore.QRect(50, 570, 351, 51))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Arbol)
        self.label_4.setGeometry(QtCore.QRect(170, 500, 101, 21))
        self.label_4.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.Button_presicion = QtWidgets.QPushButton(Arbol)
        self.Button_presicion.setGeometry(QtCore.QRect(130, 200, 191, 41))
        self.Button_presicion.setObjectName("Button_presicion")
        self.archivo = QtWidgets.QLabel(Arbol)
        self.archivo.setGeometry(QtCore.QRect(120, 70, 221, 21))
        self.archivo.setText("")
        self.archivo.setObjectName("archivo")
        self.label_6 = QtWidgets.QLabel(Arbol)
        self.label_6.setGeometry(QtCore.QRect(50, 620, 201, 21))
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(Arbol)
        self.label_10.setGeometry(QtCore.QRect(160, 320, 131, 41))
        self.label_10.setObjectName("label_10")
        self.formLayoutWidget = QtWidgets.QWidget(Arbol)
        self.formLayoutWidget.setGeometry(QtCore.QRect(110, 710, 211, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_clase = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_clase.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_clase.setText("")
        self.label_clase.setObjectName("label_clase")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_clase)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_5 = QtWidgets.QLabel(Arbol)
        self.label_5.setGeometry(QtCore.QRect(150, 530, 151, 41))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.formLayoutWidget_3 = QtWidgets.QWidget(Arbol)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(100, 270, 239, 23))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.formLayoutWidget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_8.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Arbol)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(50, 110, 361, 71))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.depth = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.depth.setObjectName("depth")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.depth)
        self.leaf = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.leaf.setObjectName("leaf")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leaf)
        self.label_precision = QtWidgets.QLabel(Arbol)
        self.label_precision.setGeometry(QtCore.QRect(100, 300, 241, 21))
        self.label_precision.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_precision.setText("")
        self.label_precision.setObjectName("label_precision")

        self.retranslateUi(Arbol)
        QtCore.QMetaObject.connectSlotsByName(Arbol)

    def retranslateUi(self, Arbol):
        _translate = QtCore.QCoreApplication.translate
        Arbol.setWindowTitle(_translate("Arbol", "Arbol"))
        self.label.setText(_translate("Arbol", "Árbol"))
        self.Button_predecir.setText(_translate("Arbol", "Predecir clase"))
        self.label_4.setText(_translate("Arbol", "Predicción"))
        self.Button_presicion.setText(_translate("Arbol", "Calcular precisión"))
        self.label_6.setText(_translate("Arbol", "*Atributos separados por comas "))
        self.label_10.setText(_translate("Arbol", "Matriz de confusión:"))
        self.label_7.setText(_translate("Arbol", "Clase asignada:"))
        self.label_5.setText(_translate("Arbol", "Nuevo elemento: "))
        self.label_8.setText(_translate("Arbol", "Precisión del modelo:"))
        self.label_3.setText(_translate("Arbol", "Máximo número de hojas: "))
        self.label_9.setText(_translate("Arbol", "Máxima profundidad: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Arbol = QtWidgets.QWidget()
    ui = Ui_Arbol()
    ui.setupUi(Arbol)
    Arbol.show()
    sys.exit(app.exec_())

