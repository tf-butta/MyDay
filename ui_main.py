# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TP FINAL_3sAUuoT.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblTitulo = QLabel(self.centralwidget)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitulo.setFont(font)

        self.gridLayout.addWidget(self.lblTitulo, 2, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(400, 400))
        self.label.setPixmap(QPixmap(u"../d4bd2b32-9d77-49e6-872c-0ff1a1f9f6b8.png"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        font1 = QFont()
        font1.setFamilies([u"Tw Cen MT"])
        font1.setPointSize(11)
        self.txtNombre.setFont(font1)

        self.gridLayout.addWidget(self.txtNombre, 3, 0, 1, 2)

        self.txtPass = QLineEdit(self.centralwidget)
        self.txtPass.setObjectName(u"txtPass")
        self.txtPass.setFont(font1)
        self.txtPass.setStyleSheet(u"color: white;\n"
"")

        self.gridLayout.addWidget(self.txtPass, 5, 0, 1, 2)

        self.btnLogin = QPushButton(self.centralwidget)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setFont(font1)
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

        self.gridLayout.addWidget(self.btnLogin, 6, 0, 1, 1)

        self.txtMail = QLineEdit(self.centralwidget)
        self.txtMail.setObjectName(u"txtMail")
        self.txtMail.setFont(font1)

        self.gridLayout.addWidget(self.txtMail, 4, 0, 1, 2)

        self.lblError = QLabel(self.centralwidget)
        self.lblError.setObjectName(u"lblError")
        self.lblError.setFont(font1)
        self.lblError.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lblError, 7, 0, 1, 2)

        self.btnRegistro = QPushButton(self.centralwidget)
        self.btnRegistro.setObjectName(u"btnRegistro")
        self.btnRegistro.setFont(font1)
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

        self.gridLayout.addWidget(self.btnRegistro, 6, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
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
        self.lblTitulo.setText(QCoreApplication.translate("MainWindow", u"Asistente Inteligente de Rutina", None))
        self.label.setText("")
        self.txtNombre.setText("")
        self.txtNombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.txtPass.setText("")
        self.txtPass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesion", None))
        self.txtMail.setText("")
        self.txtMail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Correo:", None))
        self.lblError.setText("")
        self.btnRegistro.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.menuTP_Final.setTitle(QCoreApplication.translate("MainWindow", u"TP Final", None))
    # retranslateUi

