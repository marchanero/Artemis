# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patient_select.ui'
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
        Dialog.resize(513, 212)
        Dialog.setMinimumSize(QtCore.QSize(513, 212))
        Dialog.setMaximumSize(QtCore.QSize(513, 212))
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_4.setMinimumSize(QtCore.QSize(121, 161))
        self.groupBox_4.setMaximumSize(QtCore.QSize(136, 201))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.patient_image_label = QtGui.QLabel(self.groupBox_4)
        self.patient_image_label.setMinimumSize(QtCore.QSize(101, 141))
        self.patient_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.patient_image_label.setObjectName(_fromUtf8("patient_image_label"))
        self.gridLayout_2.addWidget(self.patient_image_label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.patient_id_label = QtGui.QLineEdit(self.groupBox_2)
        self.patient_id_label.setReadOnly(True)
        self.patient_id_label.setObjectName(_fromUtf8("patient_id_label"))
        self.horizontalLayout.addWidget(self.patient_id_label)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.new_patient_button = QtGui.QPushButton(self.groupBox_2)
        self.new_patient_button.setObjectName(_fromUtf8("new_patient_button"))
        self.verticalLayout.addWidget(self.new_patient_button)
        self.load_patient_button = QtGui.QPushButton(self.groupBox_2)
        self.load_patient_button.setObjectName(_fromUtf8("load_patient_button"))
        self.verticalLayout.addWidget(self.load_patient_button)
        self.view_data_patient_button = QtGui.QPushButton(self.groupBox_2)
        self.view_data_patient_button.setObjectName(_fromUtf8("view_data_patient_button"))
        self.verticalLayout.addWidget(self.view_data_patient_button)
        self.save_patient_button = QtGui.QPushButton(self.groupBox_2)
        self.save_patient_button.setObjectName(_fromUtf8("save_patient_button"))
        self.verticalLayout.addWidget(self.save_patient_button)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Patient", None))
        self.patient_image_label.setText(_translate("Dialog", "TextLabel", None))
        self.label_8.setText(_translate("Dialog", "Patient id: ", None))
        self.new_patient_button.setText(_translate("Dialog", "New patient", None))
        self.load_patient_button.setText(_translate("Dialog", "Load Patient", None))
        self.view_data_patient_button.setText(_translate("Dialog", "View data", None))
        self.save_patient_button.setText(_translate("Dialog", "Save", None))

