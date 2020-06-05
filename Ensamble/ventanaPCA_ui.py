# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanag.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 350)
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(250, 255, 230);\n"
"}\n"
"        \n"
"\n"
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
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(170, 40, 261, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.calcular_pca = QtWidgets.QPushButton(Form)
        self.calcular_pca.setGeometry(QtCore.QRect(250, 170, 93, 28))
        self.calcular_pca.setObjectName("calcular_pca") 
        self.label_5 = QtWidgets.QLabel(Form)
        #self.label_5.setGeometry(QtCore.QRect(255, 200, 71, 91))
        self.label_5.setGeometry(QtCore.QRect(50, 0, 71, 91))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("pca.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "No. de componentes"))
        self.calcular_pca.setText(_translate("Form", "Calcular"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

