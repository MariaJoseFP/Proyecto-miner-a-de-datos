# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanax.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(419, 419)
        MainWindow.setStyleSheet("/*Cambiamos el color de la ventana*/\n"
"    #MainWindow{\n"
"        background-color: rgb(250, 255, 230);\n"
"    }\n"
"\n"
"    /*Estilos para el botón*/\n"
"    QPushButton{\n"
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
"\n"
"    /*Definimos los estilos para los QLineEdit*/\n"
"    QLineEdit{\n"
"        border-radius: 3px;\n"
"        border: 2px solid #00796b;\n"
"    }\n"
"\n"
"    /*Definimos los estilos para los QLabel*/\n"
"    QLabel{\n"
"        font-family: \'Roboto\';\n"
"        font: 25 11pt \"Calibri Light\";\n"
"    }\n"
"\n"
"    /*Definimos los estilos para los QLabels cuyos nombres son\n"
"    \'label_usuario\' y \'label-password\'*/\n"
"    #label_usuario, #label_password{\n"
"        font-size: 17px;\n"
"        color: #212121;\n"
"    }\n"
"    \n"
"    /*Estilo para el QLable cuyo nombre es #label_login*/\n"
"    #label_login{\n"
"        font-size:30px;\n"
"        color: #fff;\n"
"    }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 60, 271, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Button_abrir = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Button_abrir.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.Button_abrir)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.elementos = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.elementos.setText("")
        self.elementos.setObjectName("label_2")
        self.verticalLayout.addWidget(self.elementos )
        self.atributos = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.atributos.setText("")
        self.atributos.setObjectName("label_3")
        self.verticalLayout.addWidget(self.atributos)
        self.Button_pca = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Button_pca.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.Button_pca)
        self.Button_clasif = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Button_clasif.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.Button_clasif)
        self.Button_ensamble = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Button_ensamble.setObjectName("Button_ensamble")
        self.verticalLayout.addWidget(self.Button_ensamble)
        self.Button_ensamble.setText("Ensamble")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_abrir.setText(_translate("MainWindow", "Abrir archivo"))
        self.Button_pca.setText(_translate("MainWindow", "Carcular PCA"))
        self.Button_clasif.setText(_translate("MainWindow", "Clasificadores"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

