# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MotorsCalculator(object):
    def setupUi(self, MotorsCalculator):
        if not MotorsCalculator.objectName():
            MotorsCalculator.setObjectName(u"MotorsCalculator")
        MotorsCalculator.resize(743, 633)
        self.horizontalLayout = QHBoxLayout(MotorsCalculator)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(MotorsCalculator)
        self.tabWidget.setObjectName(u"tabWidget")
        self.rm = QWidget()
        self.rm.setObjectName(u"rm")
        self.label = QLabel(self.rm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 301, 41))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.layoutWidget = QWidget(self.rm)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 60, 231, 341))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox_motorsType = QComboBox(self.layoutWidget)
        self.comboBox_motorsType.setObjectName(u"comboBox_motorsType")

        self.horizontalLayout_2.addWidget(self.comboBox_motorsType)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_freeSpeed = QLineEdit(self.layoutWidget)
        self.lineEdit_freeSpeed.setObjectName(u"lineEdit_freeSpeed")

        self.horizontalLayout_3.addWidget(self.lineEdit_freeSpeed)

        self.comboBox_freeSpeed = QComboBox(self.layoutWidget)
        self.comboBox_freeSpeed.setObjectName(u"comboBox_freeSpeed")

        self.horizontalLayout_3.addWidget(self.comboBox_freeSpeed)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_stallTorque = QLineEdit(self.layoutWidget)
        self.lineEdit_stallTorque.setObjectName(u"lineEdit_stallTorque")

        self.horizontalLayout_4.addWidget(self.lineEdit_stallTorque)

        self.comboBox_stallTorque = QComboBox(self.layoutWidget)
        self.comboBox_stallTorque.setObjectName(u"comboBox_stallTorque")

        self.horizontalLayout_4.addWidget(self.comboBox_stallTorque)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_stallCurrent = QLineEdit(self.layoutWidget)
        self.lineEdit_stallCurrent.setObjectName(u"lineEdit_stallCurrent")

        self.horizontalLayout_5.addWidget(self.lineEdit_stallCurrent)

        self.comboBox_stallCurrent = QComboBox(self.layoutWidget)
        self.comboBox_stallCurrent.setObjectName(u"comboBox_stallCurrent")

        self.horizontalLayout_5.addWidget(self.comboBox_stallCurrent)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEdit_freeCurrent = QLineEdit(self.layoutWidget)
        self.lineEdit_freeCurrent.setObjectName(u"lineEdit_freeCurrent")

        self.horizontalLayout_6.addWidget(self.lineEdit_freeCurrent)

        self.comboBox_freeCurrent = QComboBox(self.layoutWidget)
        self.comboBox_freeCurrent.setObjectName(u"comboBox_freeCurrent")

        self.horizontalLayout_6.addWidget(self.comboBox_freeCurrent)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.lineEdit_motorsPerGearbox = QLineEdit(self.layoutWidget)
        self.lineEdit_motorsPerGearbox.setObjectName(u"lineEdit_motorsPerGearbox")

        self.horizontalLayout_7.addWidget(self.lineEdit_motorsPerGearbox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.lineEdit_gearboxEfficiency = QLineEdit(self.layoutWidget)
        self.lineEdit_gearboxEfficiency.setObjectName(u"lineEdit_gearboxEfficiency")

        self.horizontalLayout_8.addWidget(self.lineEdit_gearboxEfficiency)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_armLoad = QLabel(self.layoutWidget)
        self.label_armLoad.setObjectName(u"label_armLoad")
        self.label_armLoad.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_armLoad)

        self.lineEdit_armLoad = QLineEdit(self.layoutWidget)
        self.lineEdit_armLoad.setObjectName(u"lineEdit_armLoad")

        self.horizontalLayout_9.addWidget(self.lineEdit_armLoad)

        self.comboBox_armLoad = QComboBox(self.layoutWidget)
        self.comboBox_armLoad.setObjectName(u"comboBox_armLoad")

        self.horizontalLayout_9.addWidget(self.comboBox_armLoad)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.lineEdit_armLength = QLineEdit(self.layoutWidget)
        self.lineEdit_armLength.setObjectName(u"lineEdit_armLength")

        self.horizontalLayout_10.addWidget(self.lineEdit_armLength)

        self.comboBox_armLength = QComboBox(self.layoutWidget)
        self.comboBox_armLength.setObjectName(u"comboBox_armLength")

        self.horizontalLayout_10.addWidget(self.comboBox_armLength)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.layoutWidget1 = QWidget(self.rm)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(310, 30, 361, 384))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_ratioTag = QLabel(self.layoutWidget1)
        self.label_ratioTag.setObjectName(u"label_ratioTag")
        font2 = QFont()
        font2.setPointSize(14)
        self.label_ratioTag.setFont(font2)

        self.verticalLayout_12.addWidget(self.label_ratioTag)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_11)

        self.lineEdit_DGing1 = QLineEdit(self.layoutWidget1)
        self.lineEdit_DGing1.setObjectName(u"lineEdit_DGing1")

        self.verticalLayout_5.addWidget(self.lineEdit_DGing1)

        self.lineEdit_DGing2 = QLineEdit(self.layoutWidget1)
        self.lineEdit_DGing2.setObjectName(u"lineEdit_DGing2")

        self.verticalLayout_5.addWidget(self.lineEdit_DGing2)

        self.lineEdit_DGing3 = QLineEdit(self.layoutWidget1)
        self.lineEdit_DGing3.setObjectName(u"lineEdit_DGing3")

        self.verticalLayout_5.addWidget(self.lineEdit_DGing3)

        self.lineEdit_DGing4 = QLineEdit(self.layoutWidget1)
        self.lineEdit_DGing4.setObjectName(u"lineEdit_DGing4")

        self.verticalLayout_5.addWidget(self.lineEdit_DGing4)


        self.horizontalLayout_11.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_12)

        self.lineEdit_DGed1 = QLineEdit(self.layoutWidget1)
        self.lineEdit_DGed1.setObjectName(u"lineEdit_DGed1")

        self.verticalLayout_6.addWidget(self.lineEdit_DGed1)

        self.lineEdit_DGed2 = QLineEdit(self.layoutWidget1)
        self.lineEdit_DGed2.setObjectName(u"lineEdit_DGed2")

        self.verticalLayout_6.addWidget(self.lineEdit_DGed2)

        self.lineEdit_DGed3 = QLineEdit(self.layoutWidget1)
        self.lineEdit_DGed3.setObjectName(u"lineEdit_DGed3")

        self.verticalLayout_6.addWidget(self.lineEdit_DGed3)

        self.lineEdit_DGed4 = QLineEdit(self.layoutWidget1)
        self.lineEdit_DGed4.setObjectName(u"lineEdit_DGed4")

        self.verticalLayout_6.addWidget(self.lineEdit_DGed4)


        self.horizontalLayout_11.addLayout(self.verticalLayout_6)


        self.gridLayout.addLayout(self.horizontalLayout_11, 0, 1, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.label_17 = QLabel(self.layoutWidget1)
        self.label_17.setObjectName(u"label_17")
        font3 = QFont()
        font3.setPointSize(10)
        self.label_17.setFont(font3)

        self.verticalLayout_11.addWidget(self.label_17)

        self.label_18 = QLabel(self.layoutWidget1)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)

        self.verticalLayout_11.addWidget(self.label_18)


        self.gridLayout.addLayout(self.verticalLayout_11, 1, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_13)

        self.lineEdit_ARS_NL = QLineEdit(self.layoutWidget1)
        self.lineEdit_ARS_NL.setObjectName(u"lineEdit_ARS_NL")

        self.verticalLayout_7.addWidget(self.lineEdit_ARS_NL)

        self.lineEdit_ARS_L = QLineEdit(self.layoutWidget1)
        self.lineEdit_ARS_L.setObjectName(u"lineEdit_ARS_L")

        self.verticalLayout_7.addWidget(self.lineEdit_ARS_L)


        self.horizontalLayout_12.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_14 = QLabel(self.layoutWidget1)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_14)

        self.lineEdit_ATtm9_NL = QLineEdit(self.layoutWidget1)
        self.lineEdit_ATtm9_NL.setObjectName(u"lineEdit_ATtm9_NL")

        self.verticalLayout_8.addWidget(self.lineEdit_ATtm9_NL)

        self.lineEdit_ATtm9_L = QLineEdit(self.layoutWidget1)
        self.lineEdit_ATtm9_L.setObjectName(u"lineEdit_ATtm9_L")

        self.verticalLayout_8.addWidget(self.lineEdit_ATtm9_L)


        self.horizontalLayout_12.addLayout(self.verticalLayout_8)


        self.gridLayout.addLayout(self.horizontalLayout_12, 1, 1, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_15)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lineEdit_CDpM = QLineEdit(self.layoutWidget1)
        self.lineEdit_CDpM.setObjectName(u"lineEdit_CDpM")

        self.horizontalLayout_15.addWidget(self.lineEdit_CDpM)

        self.comboBox_CDpM = QComboBox(self.layoutWidget1)
        self.comboBox_CDpM.setObjectName(u"comboBox_CDpM")

        self.horizontalLayout_15.addWidget(self.comboBox_CDpM)


        self.verticalLayout_9.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_13.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_16)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lineEdit_SL = QLineEdit(self.layoutWidget1)
        self.lineEdit_SL.setObjectName(u"lineEdit_SL")

        self.horizontalLayout_16.addWidget(self.lineEdit_SL)

        self.comboBox_SL = QComboBox(self.layoutWidget1)
        self.comboBox_SL.setObjectName(u"comboBox_SL")

        self.horizontalLayout_16.addWidget(self.comboBox_SL)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_13.addLayout(self.verticalLayout_10)


        self.gridLayout.addLayout(self.horizontalLayout_13, 2, 1, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.rm, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(MotorsCalculator)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MotorsCalculator)
    # setupUi

    def retranslateUi(self, MotorsCalculator):
        MotorsCalculator.setWindowTitle(QCoreApplication.translate("MotorsCalculator", u"MotorCalculator v0.0.1 by 6766", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MotorsCalculator", u"Rotary Mechanism", None))
        self.label_2.setText(QCoreApplication.translate("MotorsCalculator", u"\u7535\u673a\u578b\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("MotorsCalculator", u"Free Speed", None))
        self.label_4.setText(QCoreApplication.translate("MotorsCalculator", u"Stall Torque", None))
        self.label_5.setText(QCoreApplication.translate("MotorsCalculator", u"Stall Current", None))
        self.label_6.setText(QCoreApplication.translate("MotorsCalculator", u"Free Current", None))
        self.label_7.setText(QCoreApplication.translate("MotorsCalculator", u"Motors per Gearbox", None))
        self.label_8.setText(QCoreApplication.translate("MotorsCalculator", u"Gearbox Efficiency", None))
        self.label_armLoad.setText(QCoreApplication.translate("MotorsCalculator", u"Arm Load", None))
        self.label_10.setText(QCoreApplication.translate("MotorsCalculator", u"Arm Length", None))
        self.label_ratioTag.setText(QCoreApplication.translate("MotorsCalculator", u"Overall Ratio: 1:1", None))
        self.label_11.setText(QCoreApplication.translate("MotorsCalculator", u"Driving Gear", None))
        self.label_12.setText(QCoreApplication.translate("MotorsCalculator", u"Driven Gear", None))
        self.label_17.setText(QCoreApplication.translate("MotorsCalculator", u"No Load:", None))
        self.label_18.setText(QCoreApplication.translate("MotorsCalculator", u"Loaded:", None))
        self.label_13.setText(QCoreApplication.translate("MotorsCalculator", u"Arm\n"
"Rotational\n"
"Speed", None))
        self.label_14.setText(QCoreApplication.translate("MotorsCalculator", u"Arm Time to\n"
"move\n"
"90-degrees", None))
        self.label_15.setText(QCoreApplication.translate("MotorsCalculator", u"Current Draw\n"
"per Motor\n"
" (loaded)", None))
        self.label_16.setText(QCoreApplication.translate("MotorsCalculator", u"Stall Load", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rm), QCoreApplication.translate("MotorsCalculator", u"rotary mechanism", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MotorsCalculator", u"Tab 2", None))
    # retranslateUi

