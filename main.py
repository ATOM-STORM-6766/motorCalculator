from PySide6.QtWidgets import QApplication, QWidget
from window.calculator import Ui_MotorsCalculator

from constant import *

from TrimLog import *
osc = ObjectStateConstant()
osc.version = "v0.1.0"
osc.version_tuple = (0, 1, 0)
pm = PipManage()
logger.include_headline = False
log__init__(osc, pm)


class MotorCalculator(QWidget, Ui_MotorsCalculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.unit_list1 = [
            self.comboBox_freeSpeed,
            self.comboBox_stallTorque,
            self.comboBox_stallCurrent,
            self.comboBox_freeCurrent,
            self.comboBox_armLoad,
            self.comboBox_armLength,
            self.comboBox_CDpM,
            self.comboBox_SL]
        self.placeholder_list = [self.lineEdit_motorsPerGearbox,
                                 self.lineEdit_gearboxEfficiency,
                                 self.lineEdit_armLoad,
                                 self.lineEdit_armLength,
                                 [self.lineEdit_DGing1,
                                  self.lineEdit_DGing2,
                                  self.lineEdit_DGing3,
                                  self.lineEdit_DGing4],
                                 [self.lineEdit_DGed1,
                                  self.lineEdit_DGed2,
                                  self.lineEdit_DGed3,
                                  self.lineEdit_DGed4],
                                 ]
        self.answer_list = [
            self.lineEdit_ARS_NL,
            self.lineEdit_ARS_L,
            self.lineEdit_ATtm9_NL,
            self.lineEdit_ATtm9_L,
            self.lineEdit_CDpM,
            self.lineEdit_SL]

        self.bind()
        self.placeholder_set()

        # value
        self.motors_Now: str = ""
        self.motors_now_Attr: list = []
        self.change_motorType()
        self.refresh_calculate()

    def bind(self):
        # bind motorName
        for motorName in DATA_FOR_MOTORS["motors"]:
            motorName: dict
            self.comboBox_motorsType.addItem(motorName.get("name"))
        self.change_motorType()

        # bind choose func
        self.comboBox_motorsType.activated.connect(self.change_motorType)

        # bind motor unit
        index = 0
        for i in dict(UNIT["page"][0]["unit"]).values():
            # print(self.unit_list1)
            self.unit_list1[index].addItems(i)
            index += 1

        # bind line editor func
        self.lineEdit_motorsPerGearbox.editingFinished.connect(
            self.refresh_calculate)

        self.lineEdit_gearboxEfficiency.editingFinished.connect(self.refresh_calculate)
        self.lineEdit_armLength.editingFinished.connect(self.refresh_calculate)
        self.lineEdit_armLoad.editingFinished.connect(self.refresh_calculate)
        self.lineEdit_DGing1.editingFinished.connect(self.refresh_calculate)
        self.lineEdit_DGing2.editingFinished.connect(self.refresh_calculate)
        self.lineEdit_DGing3.editingFinished.connect(self.refresh_calculate)
        self.lineEdit_DGing4.editingFinished.connect(self.refresh_calculate)
        self.lineEdit_DGed1.editingFinished.connect(self.refresh_calculate)
        self.lineEdit_DGed2.editingFinished.connect(self.refresh_calculate)
        self.lineEdit_DGed3.editingFinished.connect(self.refresh_calculate)
        self.lineEdit_DGed4.editingFinished.connect(self.refresh_calculate)

    def placeholder_set(self):
        index = 0
        for i in dict(PLACEHOLDER["page"][0]["placeholder"]).values():
            if index <= 3:
                if index == 1:
                    self.placeholder_list[index].setPlaceholderText(
                        str(i) + "%")
                else:
                    self.placeholder_list[index].setPlaceholderText(str(i))
            else:
                index_2 = 0
                for j in i:
                    self.placeholder_list[index][index_2].setPlaceholderText(
                        str(j))
                    index_2 += 1
            index += 1

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

    def refresh_calculate(self):
        # 计算模块
        for r in self.answer_list:
            r.setText("")
        # 数据处理
        placeholder = PLACEHOLDER["page"][0]["placeholder"]
        lineEdit_DGing1 = float(self.lineEdit_DGing1.text()) \
            if self.lineEdit_DGing1.text() != "" else placeholder["DrivingGear"][0]
        lineEdit_DGing2 = float(self.lineEdit_DGing2.text()) \
            if self.lineEdit_DGing2.text() != "" else placeholder["DrivingGear"][1]
        lineEdit_DGing3 = float(self.lineEdit_DGing3.text()) \
            if self.lineEdit_DGing3.text() != "" else placeholder["DrivingGear"][2]
        lineEdit_DGing4 = float(self.lineEdit_DGing4.text()) \
            if self.lineEdit_DGing4.text() != "" else placeholder["DrivingGear"][3]
        lineEdit_DGed1 = float(self.lineEdit_DGed1.text()) \
            if self.lineEdit_DGed1.text() != "" else placeholder["DrivenGear"][0]
        lineEdit_DGed2 = float(self.lineEdit_DGed2.text()) \
            if self.lineEdit_DGed2.text() != "" else placeholder["DrivenGear"][1]
        lineEdit_DGed3 = float(self.lineEdit_DGed3.text()) \
            if self.lineEdit_DGed3.text() != "" else placeholder["DrivenGear"][2]
        lineEdit_DGed4 = float(self.lineEdit_DGed4.text()) \
            if self.lineEdit_DGed4.text() != "" else placeholder["DrivenGear"][3]
        lineEdit_motorsPerGearbox = float(self.lineEdit_motorsPerGearbox.text()) \
            if self.lineEdit_motorsPerGearbox.text() != "" else placeholder["motorsPerGearbox"]
        lineEdit_gearboxEfficiency = float(self.lineEdit_gearboxEfficiency.text()) * 0.01\
            if self.lineEdit_gearboxEfficiency.text() != "" else placeholder["GearboxEfficiency"] * 0.01
        lineEdit_armLoad = float(self.lineEdit_armLoad.text()) \
            if self.lineEdit_armLoad.text() != "" else placeholder["armLoad"]
        lineEdit_armLength = float(self.lineEdit_armLength.text()) \
            if self.lineEdit_armLength.text() != "" else placeholder["armLength"]
        attr0 = float(self.motors_now_Attr[0])
        attr1 = float(self.motors_now_Attr[1])
        attr2 = float(self.motors_now_Attr[2])
        attr3 = float(self.motors_now_Attr[3])
        # 计算公式
        ratio = (lineEdit_DGing1 * lineEdit_DGing2 *
                 lineEdit_DGing3 * lineEdit_DGing4 /
                 lineEdit_DGed1 / lineEdit_DGed2 /
                 lineEdit_DGed3 / lineEdit_DGed4)
        ARS_NL: float = (attr0 * ratio * (360 / 60))
        SL: float = (attr1 *
                     lineEdit_motorsPerGearbox *
                     (1 / ratio) *
                     meter2inch * n2nlb *  # 单位转换：1m=39.37in 1N=0.2248N lbs
                     lineEdit_gearboxEfficiency /
                     lineEdit_armLength)
        ARS_L: float = ((-1) * (ARS_NL / SL) * lineEdit_armLoad) + ARS_NL
        ATtM9_NL: float = 90 / ARS_NL
        ATtM9_L: float = 90 / ARS_L
        CDpM: float = (((attr2 * lineEdit_motorsPerGearbox - attr3 * lineEdit_motorsPerGearbox) /
                        (attr1 * lineEdit_motorsPerGearbox)) *
                       (lineEdit_armLoad * lineEdit_armLength * ratio / (meter2inch * n2nlb))
                       + (attr3 * lineEdit_motorsPerGearbox)
                       ) / lineEdit_motorsPerGearbox
        # 渲染
        self.lineEdit_ARS_NL.setText(str(round_up(ARS_NL, 2)) + "  deg/s")
        self.lineEdit_ARS_L.setText(str(round_up(ARS_L, 2)) + "  deg/s")
        self.lineEdit_ATtm9_NL.setText(str(round_up(ATtM9_NL, 2)) + "  sec")
        self.lineEdit_ATtm9_L.setText(str(round_up(ATtM9_L, 2)) + "  sec")
        self.lineEdit_CDpM.setText(str(round_up(CDpM, 2)))
        self.lineEdit_SL.setText(str(round_up(SL, 2)))

        self.label_ratioTag.setText("Overall Ratio->" + str(round_up(1 / ratio, 2)) + ":1")


if __name__ == "__main__":
    # logger.info(UNIT)
    app = QApplication([])
    window = MotorCalculator()
    window.show()
    app.exec()
