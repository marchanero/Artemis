# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'therapist_select.ui'
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
        Dialog.resize(634, 217)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 611, 201))
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
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.therapist_image_label = QtGui.QLabel(self.groupBox_4)
        self.therapist_image_label.setGeometry(QtCore.QRect(0, 15, 121, 151))
        self.therapist_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.therapist_image_label.setObjectName(_fromUtf8("therapist_image_label"))
        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.therapist_id_text = QtGui.QLineEdit(self.groupBox_2)
        self.therapist_id_text.setMinimumSize(QtCore.QSize(120, 0))
        self.therapist_id_text.setObjectName(_fromUtf8("therapist_id_text"))
        self.horizontalLayout.addWidget(self.therapist_id_text)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.save_therapist_button = QtGui.QPushButton(self.groupBox_2)
        self.save_therapist_button.setMinimumSize(QtCore.QSize(100, 0))
        self.save_therapist_button.setObjectName(_fromUtf8("save_therapist_button"))
        self.verticalLayout.addWidget(self.save_therapist_button)
        self.load_therapist_button = QtGui.QPushButton(self.groupBox_2)
        self.load_therapist_button.setMinimumSize(QtCore.QSize(100, 0))
        self.load_therapist_button.setObjectName(_fromUtf8("load_therapist_button"))
        self.verticalLayout.addWidget(self.load_therapist_button)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Therapist", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Photo", None))
        self.therapist_image_label.setText(_translate("Dialog", "TextLabel", None))
        self.label_8.setText(_translate("Dialog", "Therapist id", None))
        self.save_therapist_button.setText(_translate("Dialog", "Save", None))
        self.load_therapist_button.setText(_translate("Dialog", "Load", None))

