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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(743, 633)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.rm = QWidget()
        self.rm.setObjectName(u"rm")
        self.label = QLabel(self.rm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 301, 41))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.widget = QWidget(self.rm)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 60, 231, 341))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_4.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_5.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_6.addWidget(self.lineEdit_4)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_7.addWidget(self.lineEdit_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.lineEdit_6 = QLineEdit(self.widget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_8.addWidget(self.lineEdit_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.lineEdit_7 = QLineEdit(self.widget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_9.addWidget(self.lineEdit_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.lineEdit_8 = QLineEdit(self.widget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_10.addWidget(self.lineEdit_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.widget1 = QWidget(self.rm)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(310, 30, 361, 371))
        self.verticalLayout_12 = QVBoxLayout(self.widget1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.widget1)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_12.addWidget(self.label_19)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_11 = QLabel(self.widget1)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_5.addWidget(self.label_11)

        self.lineEdit_9 = QLineEdit(self.widget1)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.verticalLayout_5.addWidget(self.lineEdit_9)

        self.lineEdit_10 = QLineEdit(self.widget1)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.verticalLayout_5.addWidget(self.lineEdit_10)

        self.lineEdit_12 = QLineEdit(self.widget1)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.verticalLayout_5.addWidget(self.lineEdit_12)

        self.lineEdit_11 = QLineEdit(self.widget1)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.verticalLayout_5.addWidget(self.lineEdit_11)


        self.horizontalLayout_11.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_12 = QLabel(self.widget1)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_6.addWidget(self.label_12)

        self.lineEdit_13 = QLineEdit(self.widget1)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.verticalLayout_6.addWidget(self.lineEdit_13)

        self.lineEdit_14 = QLineEdit(self.widget1)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.verticalLayout_6.addWidget(self.lineEdit_14)

        self.lineEdit_15 = QLineEdit(self.widget1)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.verticalLayout_6.addWidget(self.lineEdit_15)

        self.lineEdit_16 = QLineEdit(self.widget1)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.verticalLayout_6.addWidget(self.lineEdit_16)


        self.horizontalLayout_11.addLayout(self.verticalLayout_6)


        self.gridLayout.addLayout(self.horizontalLayout_11, 0, 1, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.label_17 = QLabel(self.widget1)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_11.addWidget(self.label_17)

        self.label_18 = QLabel(self.widget1)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_11.addWidget(self.label_18)


        self.gridLayout.addLayout(self.verticalLayout_11, 1, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_13 = QLabel(self.widget1)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_7.addWidget(self.label_13)

        self.lineEdit_17 = QLineEdit(self.widget1)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.verticalLayout_7.addWidget(self.lineEdit_17)

        self.lineEdit_18 = QLineEdit(self.widget1)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.verticalLayout_7.addWidget(self.lineEdit_18)


        self.horizontalLayout_12.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_14 = QLabel(self.widget1)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_8.addWidget(self.label_14)

        self.lineEdit_19 = QLineEdit(self.widget1)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.verticalLayout_8.addWidget(self.lineEdit_19)

        self.lineEdit_20 = QLineEdit(self.widget1)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.verticalLayout_8.addWidget(self.lineEdit_20)


        self.horizontalLayout_12.addLayout(self.verticalLayout_8)


        self.gridLayout.addLayout(self.horizontalLayout_12, 1, 1, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_15 = QLabel(self.widget1)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_9.addWidget(self.label_15)

        self.lineEdit_21 = QLineEdit(self.widget1)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.verticalLayout_9.addWidget(self.lineEdit_21)


        self.horizontalLayout_13.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_16 = QLabel(self.widget1)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_10.addWidget(self.label_16)

        self.lineEdit_22 = QLineEdit(self.widget1)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.verticalLayout_10.addWidget(self.lineEdit_22)


        self.horizontalLayout_13.addLayout(self.verticalLayout_10)


        self.gridLayout.addLayout(self.horizontalLayout_13, 2, 1, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.rm, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Form", u"Rotary Mechanism", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7535\u673a\u578b\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rm), QCoreApplication.translate("Form", u"rotary mechanism", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Tab 2", None))
    # retranslateUi

