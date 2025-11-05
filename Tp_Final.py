# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfazbTPApj.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 30, 361, 31))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 90, 71, 20))
        self.lblHora = QLabel(self.centralwidget)
        self.lblHora.setObjectName(u"lblHora")
        self.lblHora.setGeometry(QRect(390, 90, 49, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 110, 49, 16))
        self.lblFecha = QLabel(self.centralwidget)
        self.lblFecha.setObjectName(u"lblFecha")
        self.lblFecha.setGeometry(QRect(360, 110, 49, 16))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(320, 260, 171, 131))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 30, 49, 16))
        self.lblIconoClima = QLabel(self.groupBox)
        self.lblIconoClima.setObjectName(u"lblIconoClima")
        self.lblIconoClima.setGeometry(QRect(50, 30, 49, 16))
        self.lblTemperaturaClima = QLabel(self.groupBox)
        self.lblTemperaturaClima.setObjectName(u"lblTemperaturaClima")
        self.lblTemperaturaClima.setGeometry(QRect(100, 30, 49, 16))
        self.btnActualizarClima = QPushButton(self.groupBox)
        self.btnActualizarClima.setObjectName(u"btnActualizarClima")
        self.btnActualizarClima.setGeometry(QRect(30, 70, 111, 41))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(320, 130, 171, 121))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 30, 111, 16))
        self.lblTempArduino = QLabel(self.groupBox_2)
        self.lblTempArduino.setObjectName(u"lblTempArduino")
        self.lblTempArduino.setGeometry(QRect(130, 30, 41, 16))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 50, 49, 16))
        self.lblLuz = QLabel(self.groupBox_2)
        self.lblLuz.setObjectName(u"lblLuz")
        self.lblLuz.setGeometry(QRect(40, 50, 49, 16))
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 70, 49, 16))
        self.lblEstado = QLabel(self.groupBox_2)
        self.lblEstado.setObjectName(u"lblEstado")
        self.lblEstado.setGeometry(QRect(50, 70, 49, 16))
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 90, 91, 16))
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(110, 90, 49, 16))
        self.btnActualizar = QPushButton(self.centralwidget)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setGeometry(QRect(330, 400, 151, 41))
        self.btnEnviarMail = QPushButton(self.centralwidget)
        self.btnEnviarMail.setObjectName(u"btnEnviarMail")
        self.btnEnviarMail.setGeometry(QRect(330, 450, 151, 41))
        self.btnSalir = QPushButton(self.centralwidget)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(330, 500, 151, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Asistente de Rutina Inteligente", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Hora actual:", None))
        self.lblHora.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.lblFecha.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Clima actual", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Clima:", None))
        self.lblIconoClima.setText("")
        self.lblTemperaturaClima.setText("")
        self.btnActualizarClima.setText(QCoreApplication.translate("MainWindow", u"Actualizar clima", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Sensores Arduino", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Temperatura sensor:", None))
        self.lblTempArduino.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Luz:", None))
        self.lblLuz.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.lblEstado.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Horas dormidas:", None))
        self.label_9.setText("")
        self.btnActualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar datos", None))
        self.btnEnviarMail.setText(QCoreApplication.translate("MainWindow", u"Enviar mail resumen", None))
        self.btnSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

