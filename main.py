from PySide6.QtWidgets import QApplication, QWidget
from window.calculator import Ui_MotorsCalculator

from constant import DATA_FOR_MOTORS

from TrimLog import *
osc = ObjectStateConstant()
pm = PipManage()
logger.include_headline = False
log__init__(osc, pm)


class MotorCalculator(QWidget, Ui_MotorsCalculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()

        # value
        self.motors_Now: str = ""
        self.motors_now_Attr: list = []

    def bind(self):
        # bind motorName
        for motorName in DATA_FOR_MOTORS["motors"]:
            motorName: dict
            self.comboBox_motorsType.addItem(motorName.get("name"))
        self.change_motorType()

        # bind choose func
        self.comboBox_motorsType.activated.connect(self.change_motorType)

    def change_motorType(self):
        # bind motorAttribute
        motorAttribute: list = DATA_FOR_MOTORS["motors"]
        for find_ in motorAttribute:
            if find_.get("name") == self.comboBox_motorsType.currentText():
                self.motors_Now: str = find_.get("data")[:-1]
                break
        self.motors_now_Attr: list = self.motors_Now.split("\t")
        logger.info(self.motors_now_Attr)

        self.lineEdit_freeSpeed.setText(self.motors_now_Attr[0])
        self.lineEdit_stallTorque.setText(self.motors_now_Attr[1])
        self.lineEdit_stallCurrent.setText(self.motors_now_Attr[2])
        self.lineEdit_freeCurrent.setText(self.motors_now_Attr[3])


if __name__ == "__main__":
    # logger.info(DATA_FOR_MOTORS)
    app = QApplication([])
    window = MotorCalculator()
    window.show()
    app.exec()
