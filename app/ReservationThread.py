from PySide6.QtCore import QThread
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import MainWindow


class ReservationThread(QThread):
    def __init__(self, parent: MainWindow, retry_count: int = 5):
        super().__init__(parent)
        self.parent = parent
        self.retry_count = retry_count
    
    def run(self):
        self.driver = self.parent.driver
        self.retry_count = 5
        self.check_reserve_date()
    
    def check_reserve_date(self):
        self.parent.log("예약 조회 시작")
        self.driver.get('https://www.namyeoju.co.kr/Reservation/Reservation.aspx')
        self.driver.implicitly_wait(5)

        days = self.driver.find_elements(By.CLASS_NAME, 'reserved')
        if len(days) == 0 and self.retry_count > 0:
            self.parent.log("[{0}] 예약 할 시간이 없습니다. 다시 시도 합니다.".format(self.retry_count))
            self.retry_count -= 1
            self.check_reserve_date()
            return
        
        if len(days) == 0:
            self.parent.log("예약을 종료 합니다.")
            self.parent.stop()
            return;
            
        for d in days:
            print('📢[ReservationThread.py:32]', d.text)

        