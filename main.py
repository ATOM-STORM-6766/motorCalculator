from PySide6.QtWidgets import QApplication, QWidget
from window.calculator import Ui_Form


class MotorCalculator(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    window = MotorCalculator()
    window.show()
    app.exec()
