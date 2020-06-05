# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaKNN.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KNN(object):
    def setupUi(self, KNN):
        KNN.setObjectName("KNN")
        KNN.resize(438, 769)
        KNN.setStyleSheet("#KNN{\n"
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
"    color:#ffffff\n"
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
        self.formLayoutWidget = QtWidgets.QWidget(KNN)
        self.formLayoutWidget.setGeometry(QtCore.QRect(64, 50, 311, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.Button_presicion = QtWidgets.QPushButton(self.formLayoutWidget)
        self.Button_presicion.setObjectName("Button_presicion")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Button_presicion)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setStyleSheet("color: #ff5722;\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.verticalLayoutWidget = QtWidgets.QWidget(KNN)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 180, 328, 104))
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
        self.label_3 = QtWidgets.QLabel(KNN)
        self.label_3.setGeometry(QtCore.QRect(70, 30, 221, 21))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(KNN)
        self.label_4.setGeometry(QtCore.QRect(80, 450, 101, 21))
        self.label_4.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(KNN)
        self.label_5.setGeometry(QtCore.QRect(80, 490, 151, 41))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(KNN)
        self.label_6.setGeometry(QtCore.QRect(80, 590, 191, 16))
        self.label_6.setObjectName("label_6")
        self.Button_predecir = QtWidgets.QPushButton(KNN)
        self.Button_predecir.setGeometry(QtCore.QRect(150, 620, 111, 31))
        self.Button_predecir.setObjectName("Button_predecir")
        self.label_matriz = QtWidgets.QTextBrowser(KNN)
        self.label_matriz.setGeometry(QtCore.QRect(120, 320, 171, 121))
        self.label_matriz.setObjectName("label_matriz")
        self.label_10 = QtWidgets.QLabel(KNN)
        self.label_10.setGeometry(QtCore.QRect(140, 290, 131, 41))
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(KNN)
        self.lineEdit.setGeometry(QtCore.QRect(50, 530, 371, 61))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayoutWidget_2 = QtWidgets.QWidget(KNN)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(110, 690, 211, 31))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_clase = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_clase.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_clase.setText("")
        self.label_clase.setObjectName("label_clase")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_clase)

        self.retranslateUi(KNN)
        QtCore.QMetaObject.connectSlotsByName(KNN)

    def retranslateUi(self, KNN):
        _translate = QtCore.QCoreApplication.translate
        KNN.setWindowTitle(_translate("KNN", "Clasificador KNN"))
        self.label_2.setText(_translate("KNN", "Número de vecinos"))
        self.Button_presicion.setText(_translate("KNN", "Calcular precisión"))
        self.label.setText(_translate("KNN", "KNN"))
        self.label_8.setText(_translate("KNN", "Presición con el conjunto de entrenamiento:"))
        self.label_9.setText(_translate("KNN", "Presición con el conjunto de prueba:"))
        self.label_4.setText(_translate("KNN", "Predicción"))
        self.label_5.setText(_translate("KNN", "Nuevo elemento: "))
        self.label_6.setText(_translate("KNN", "*Atributos separados por comas"))
        self.Button_predecir.setText(_translate("KNN", "Predecir clase"))
        self.label_10.setText(_translate("KNN", "Matriz de confusión:"))
        self.label_7.setText(_translate("KNN", "Clase asignada:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KNN = QtWidgets.QWidget()
    ui = Ui_KNN()
    ui.setupUi(KNN)
    KNN.show()
    sys.exit(app.exec_())

