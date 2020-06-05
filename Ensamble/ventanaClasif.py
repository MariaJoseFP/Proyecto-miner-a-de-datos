# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaClasif.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Clasificador(object):
    def setupUi(self, Clasificador):
        Clasificador.setObjectName("Clasificador")
        Clasificador.resize(400, 300)
        Clasificador.setStyleSheet("#Clasificador{\n"
"        background-color: rgb(250, 255, 230);\n"
"    }\n"
"QPushButton{\n"
"        background-color: #ff5722;\n"
"        border-radius: 4px;\n"
"        color: #fff;\n"
"        font-family: \'Roboto\';\n"
"        font-size: 17px;\n"
"    }\n"
"    \n"
"    /*Definimos el estilo para un efecto hover sobre el botón,\n"
"    este cambiará su background cuando pasemos el mouse por\n"
"    encima*/\n"
"    QPushButton:hover{\n"
"    background-color: #ff7043;\n"
"    }\n"
"")
        self.verticalLayoutWidget = QtWidgets.QWidget(Clasificador)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 80, 160, 100))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.clasif_KNN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clasif_KNN.setObjectName("clasif_KNN")
        self.verticalLayout.addWidget(self.clasif_KNN)
        self.clasif_Bayes = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clasif_Bayes.setObjectName("clasif_Bayes")
        self.verticalLayout.addWidget(self.clasif_Bayes)
        self.clasif_Arbol = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clasif_Arbol.setObjectName("clasif_Arbol")
        self.verticalLayout.addWidget(self.clasif_Arbol)
        self.label = QtWidgets.QLabel(Clasificador)
        self.label.setGeometry(QtCore.QRect(120, 30, 161, 16))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Clasificador)
        QtCore.QMetaObject.connectSlotsByName(Clasificador)

    def retranslateUi(self, Clasificador):
        _translate = QtCore.QCoreApplication.translate
        Clasificador.setWindowTitle(_translate("Clasificador", "Clasificadores"))
        self.clasif_KNN.setText(_translate("Clasificador", "KNN"))
        self.clasif_Bayes.setText(_translate("Clasificador", "Naive Bayes"))
        self.clasif_Arbol.setText(_translate("Clasificador", "Árbol"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Clasificador = QtWidgets.QWidget()
    ui = Ui_Clasificador()
    ui.setupUi(Clasificador)
    Clasificador.show()
    sys.exit(app.exec_())

