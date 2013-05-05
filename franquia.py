# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created: Sat May  4 12:01:21 2013
#      by: PyQt4 UI code generator 4.9.1


from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
import sys
from class_acesso import Iconecta

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(236, 156)
        #Atualizar
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 100, 94, 24))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.atualizar)
        #Sair
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 100, 61, 24))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.sair)
        #Franquia
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 60, 221, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        #Contato
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 130, 56, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        QtCore.QObject.connect(self.label_2, QtCore.SIGNAL("linkActivated(QString)"), self.openUrl)
        #Plano
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 151, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Franquia I-conecta", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Atualizar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "Sair", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Atualize o consumo.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", '<a href="http://www.twitter.com/pinheirofellipe">Contato</a></em>', None, QtGui.QApplication.UnicodeUTF8))

    def atualizar(self):
        f = Iconecta()
        f.configura()
        consumo = f.franquia()

        self.label.setText(QtGui.QApplication.translate("Dialog", consumo, None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", plano, None, QtGui.QApplication.UnicodeUTF8))

    def openUrl(self, URL):
        QtGui.QDesktopServices().openUrl(QUrl(URL))

    def sair(self):
        sys.exit()


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
