# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patient_data_altaBDD.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(588, 212)
        Dialog.setMinimumSize(QtCore.QSize(588, 212))
        Dialog.setMaximumSize(QtCore.QSize(588, 212))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 571, 200))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(555, 200))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 121, 161))
        self.groupBox_3.setMinimumSize(QtCore.QSize(121, 161))
        self.groupBox_3.setMaximumSize(QtCore.QSize(121, 161))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.patient_image_label = QtGui.QLabel(self.groupBox_3)
        self.patient_image_label.setGeometry(QtCore.QRect(10, 20, 121, 171))
        self.patient_image_label.setObjectName(_fromUtf8("patient_image_label"))
        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(151, 22, 411, 161))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.patient_tex = QtGui.QLineEdit(self.widget)
        self.patient_tex.setMinimumSize(QtCore.QSize(200, 0))
        self.patient_tex.setObjectName(_fromUtf8("patient_tex"))
        self.gridLayout.addWidget(self.patient_tex, 0, 2, 1, 2)
        self.female_patient_radioButton = QtGui.QRadioButton(self.widget)
        self.female_patient_radioButton.setObjectName(_fromUtf8("female_patient_radioButton"))
        self.gridLayout.addWidget(self.female_patient_radioButton, 4, 3, 1, 1)
        self.age_patient_text_2 = QtGui.QLineEdit(self.widget)
        self.age_patient_text_2.setMinimumSize(QtCore.QSize(200, 0))
        self.age_patient_text_2.setObjectName(_fromUtf8("age_patient_text_2"))
        self.gridLayout.addWidget(self.age_patient_text_2, 2, 2, 1, 2)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.male_patient_radioButton = QtGui.QRadioButton(self.widget)
        self.male_patient_radioButton.setObjectName(_fromUtf8("male_patient_radioButton"))
        self.gridLayout.addWidget(self.male_patient_radioButton, 4, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.name_patient_text = QtGui.QLineEdit(self.widget)
        self.name_patient_text.setMinimumSize(QtCore.QSize(200, 0))
        self.name_patient_text.setObjectName(_fromUtf8("name_patient_text"))
        self.gridLayout.addWidget(self.name_patient_text, 1, 2, 1, 2)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 3, 2, 1, 2)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 5, 3, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 5, 2, 1, 1)
        self.groupBox_3.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "Patient", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Photo", None))
        self.patient_image_label.setText(_translate("Dialog", "TextLabel", None))
        self.female_patient_radioButton.setText(_translate("Dialog", "Female", None))
        self.label_5.setText(_translate("Dialog", "Age", None))
        self.male_patient_radioButton.setText(_translate("Dialog", "Male", None))
        self.label_7.setText(_translate("Dialog", "Gender", None))
        self.label_4.setText(_translate("Dialog", "Patient Id", None))
        self.label_8.setText(_translate("Dialog", "Disease prevalence", None))
        self.label_6.setText(_translate("Dialog", "Educational level", None))
        self.pushButton.setText(_translate("Dialog", "Save", None))
        self.pushButton_2.setText(_translate("Dialog", "Reset", None))

