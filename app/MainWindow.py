from datetime import datetime
from enum import Enum
from gettext import gettext
from lib2to3.pgen2 import driver
import re
import threading
import time
from PySide6 import QtCore
from PySide6 import QtGui
import PySide6.QtCore
from PySide6.QtWidgets import QListWidgetItem, QMainWindow
from PySide6.QtCore import QTime, QTimer

from app.ui.ui_MainWindow import Ui_MainWindow
from app.lib.Config import Config
from app.lib.webdriver import get_driver

from selenium.webdriver.common.by import By


class MainWindow(QMainWindow):
    TIMER_DELAY = 100

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.config = Config()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.set_config_data()
        self.__init_connect()
        self.driver = None
        self.is_login = False;
        self.timer = QTimer()
        self.delta_timer = 0

    def set_config_data(self):
        self.ui.leID.setText(self.config.setting["id"])
        self.ui.lePassword.setText(self.config.setting["password"])
        input = self.config.setting["reservationDateTime"]
        reservationDateTime = datetime.strptime(input, "%Y-%m-%d %H:%M")
        self.ui.dteRereservation.setDateTime(reservationDateTime)
        input = self.config.setting["startTime"]
        startTime = QTime().fromString(input, "hh:mmAP")
        self.ui.teStartTime.setTime(startTime)
        self.ui.leRunMultiple.setText(str(self.config.setting["runMultiple"]))

    def __init_connect(self):
        self.ui.btnStart.clicked.connect(self.on_click_start)
        self.ui.btnClose.clicked.connect(self.close)
        # self.ui.getButton.clicked.connect(self.get_button)
        # self.ui.complete_delete_button.clicked.connect(self.__complete_delete)
        # self.ui.site_open_button.clicked.connect(self.__on_site_open_button)

    def on_click_start(self):
        self.driver = get_driver()
        self.login()

    def login(self):
        self.ui.btnStart.setEnabled(False)
        if self.is_login == True:
            return

        url = self.config.setting["loginUrl"]
        self.driver.get(url)
        self.driver.implicitly_wait(15)

        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_userID").send_keys(
            self.ui.leID.text()
        )
        self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_userPass").send_keys(
            self.ui.lePassword.text()
        )
        self.driver.find_element(
            By.XPATH, '//*[@id="section"]/div/div/ul[1]/li[2]/a'
        ).click()
        self.driver.implicitly_wait(15)
        btn = self.driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/div[4]/div[2]/div[1]/div[2]/p[2]')

        if btn.text != '로그아웃':
            self.login()
            return

        self.is_login = True

        self.run_count = 0
        self.timer.start(self.TIMER_DELAY)
        self.timer.timeout.connect(self.on_timer)
        self.run_delay = self.config.setting["runDelay"]

    def stop(self):
        self.timer.stop()
    
    def on_timer(self):
        self.delta_timer = self.delta_timer + self.TIMER_DELAY
        if self.delta_timer < self.run_delay:
            return
        self.delta_timer = self.delta_timer - self.run_delay
        self.run_count = self.run_count + 1

        if self.run_count >= self.config.setting["runMultiple"]:
            self.stop()
    

