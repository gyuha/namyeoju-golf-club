# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTimeEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(582, 633)
        self.action_always_top = QAction(MainWindow)
        self.action_always_top.setObjectName(u"action_always_top")
        self.action_always_top.setCheckable(True)
        self.action_clipboard_toggle = QAction(MainWindow)
        self.action_clipboard_toggle.setObjectName(u"action_clipboard_toggle")
        self.action_clipboard_toggle.setCheckable(True)
        self.action_clipboard_toggle.setChecked(True)
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.teStartTime = QTimeEdit(self.centralwidget)
        self.teStartTime.setObjectName(u"teStartTime")

        self.gridLayout.addWidget(self.teStartTime, 2, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.leID = QLineEdit(self.centralwidget)
        self.leID.setObjectName(u"leID")
        self.leID.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.leID, 1, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.dteRereservation = QDateTimeEdit(self.centralwidget)
        self.dteRereservation.setObjectName(u"dteRereservation")

        self.gridLayout.addWidget(self.dteRereservation, 2, 3, 1, 1)

        self.leRunMultiple = QLineEdit(self.centralwidget)
        self.leRunMultiple.setObjectName(u"leRunMultiple")

        self.gridLayout.addWidget(self.leRunMultiple, 3, 1, 1, 1)

        self.lePassword = QLineEdit(self.centralwidget)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setMaximumSize(QSize(16777215, 16777215))
        self.lePassword.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lePassword, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnClose = QPushButton(self.centralwidget)
        self.btnClose.setObjectName(u"btnClose")

        self.horizontalLayout.addWidget(self.btnClose)

        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")

        self.horizontalLayout.addWidget(self.btnStart)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wolf catcher", None))
        self.action_always_top.setText(QCoreApplication.translate("MainWindow", u"\ud56d\uc0c1\uc704", None))
        self.action_clipboard_toggle.setText(QCoreApplication.translate("MainWindow", u"\ud074\ub9bd\ubcf4\ub4dc\uc5d0\uc11c \ucd94\uac00", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc(&q)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc544\uc774\ub514", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uc2e4\ud589 \uac04\uaca9", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uc608\uc57d \uc2dc\uac04", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791 \uc2dc\uac04", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc554\ud638", None))
        self.btnClose.setText(QCoreApplication.translate("MainWindow", u"\ub2eb\uae30", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
    # retranslateUi

