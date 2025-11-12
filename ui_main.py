# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TP FINAL_3yqqgIg.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #0D1B2A; /* azul noche */\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnLogin = QPushButton(self.centralwidget)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(273, 230, 101, 26))
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(11)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet(u"QPushButton {\n"
"    background-color: #1B263B;   /* azul oscuro */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #415A77;   /* azul m\u00e1s claro al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #778DA9;   /* tono al presionar */\n"
"}\n"
"")
        self.lblTitulo = QLabel(self.centralwidget)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setGeometry(QRect(250, 30, 361, 31))
        font1 = QFont()
        font1.setFamilies([u"Tw Cen MT"])
        font1.setPointSize(18)
        self.lblTitulo.setFont(font1)
        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(280, 70, 221, 26))
        self.txtNombre.setFont(font)
        self.txtMail = QLineEdit(self.centralwidget)
        self.txtMail.setObjectName(u"txtMail")
        self.txtMail.setGeometry(QRect(280, 110, 221, 26))
        self.txtMail.setFont(font)
        self.txtPass = QLineEdit(self.centralwidget)
        self.txtPass.setObjectName(u"txtPass")
        self.txtPass.setGeometry(QRect(280, 150, 221, 26))
        self.txtPass.setFont(font)
        self.txtPass.setStyleSheet(u"color: white;\n"
"")
        self.btnRegistro = QPushButton(self.centralwidget)
        self.btnRegistro.setObjectName(u"btnRegistro")
        self.btnRegistro.setGeometry(QRect(400, 230, 101, 26))
        self.btnRegistro.setFont(font)
        self.btnRegistro.setStyleSheet(u"QPushButton {\n"
"    background-color: #1B263B;   /* azul oscuro */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #415A77;   /* azul m\u00e1s claro al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #778DA9;   /* tono al presionar */\n"
"}\n"
"")
        self.lblError = QLabel(self.centralwidget)
        self.lblError.setObjectName(u"lblError")
        self.lblError.setGeometry(QRect(260, 290, 261, 31))
        self.lblError.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menuTP_Final = QMenu(self.menubar)
        self.menuTP_Final.setObjectName(u"menuTP_Final")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTP_Final.menuAction())

        self.retranslateUi(MainWindow)
        self.btnLogin.clicked.connect(MainWindow.iniciar_sesion)
        self.btnRegistro.clicked.connect(MainWindow.crear_cuenta)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesion", None))
        self.lblTitulo.setText(QCoreApplication.translate("MainWindow", u"Asistente Inteligente de Rutina", None))
        self.txtNombre.setText("")
        self.txtNombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.txtMail.setText("")
        self.txtMail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Correo:", None))
        self.txtPass.setText("")
        self.txtPass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrasenia:", None))
        self.btnRegistro.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.lblError.setText("")
        self.menuTP_Final.setTitle(QCoreApplication.translate("MainWindow", u"TP Final", None))
    # retranslateUi

