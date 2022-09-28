from datetime import datetime
from enum import Enum
from gettext import gettext

import PySide6.QtCore
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QTime, QTimer, QDate
from PySide6.QtWidgets import QListWidgetItem, QMainWindow
from selenium.webdriver.common.by import By

from lib.Config import Config
from lib.webdriver import get_driver
from ui.ui_MainWindow import Ui_MainWindow
from ReservationThread import ReservationThread


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
        self.is_login = False
        self.timer = QTimer()
        self.delta_timer = 0

    def set_config_data(self):
        self.ui.leID.setText(self.config.setting["id"])
        self.ui.lePassword.setText(self.config.setting["password"])

        # 예약일
        reserve_date = QDate.fromString(
            self.config.setting["reserve_date"], "yyyy-MM-dd"
        )
        self.ui.deReserveDate.setDate(reserve_date)

        # 시간
        input = self.config.setting["start_time"]
        start_time = QTime().fromString(input, "hh:mm")
        self.ui.teStartTime.setTime(start_time)

        input = self.config.setting["end_time"]
        end_time = QTime().fromString(input, "hh:mm")
        self.ui.teEndTime.setTime(end_time)

        self.ui.leRunDuration.setText(str(self.config.setting["run_duration"]))
        self.run_duration = self.config.setting["run_duration"]
        self.retry_count = self.config.setting["retry_count"]

    def __init_connect(self):
        self.ui.btnStart.clicked.connect(self.on_click_start)

    def on_click_start(self):
        self.driver = get_driver()
        self.login()

    def login(self):
        self.ui.btnStart.setEnabled(False)
        if self.is_login == True:
            return

        url = self.config.setting["loginUrl"]
        self.log("로그인 시도")
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
        btn = self.driver.find_element(
            By.XPATH, '//*[@id="aspnetForm"]/div[4]/div[2]/div[1]/div[2]/p[2]'
        )

        if btn.text != "로그아웃":
            self.log("로그인 실패")
            self.login()
            return

        self.log("로그인 성공")
        self.is_login = True

        # 예약
        th = ReservationThread(self, self.retry_count)
        self.log("예약 시작")
        th.start()

    def log(self, text: str):
        now = datetime.now().strftime("%Y/%d/%m %H:%M%S")
        text = self.ui.teLog.appendPlainText("[{0}]: {1}".format(now, text))
        self.ui.teLog.verticalScrollBar().setValue(self.ui.teLog.verticalScrollBar().maximum())
    
    def stop(self):
        self.ui.btnStart.setEnabled(True)

    # def stop(self):
    #     self.timer.stop()

    # def on_timer(self):
    #     self.delta_timer = self.delta_timer + self.TIMER_DELAY
    #     if self.delta_timer < self.run_delay:
    #         return
    #     self.delta_timer = self.delta_timer - self.run_delay
    #     self.run_count = self.run_count + 1

    #     if self.run_count >= self.config.setting["runMultiple"]:
    #         self.stop()
    #     th = ReservationThread(self)
    #     th.start()
