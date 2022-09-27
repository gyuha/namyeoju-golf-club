from PySide6.QtCore import QThread


class ReservationThread(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        driver = self.parent.driver
        tab = driver.switch_to.new_window('tab')
        driver.get('https://www.namyeoju.co.kr/Reservation/Reservation.aspx')
        print('📢[ReservationThread.py:12]')
        tab.close()