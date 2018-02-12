import pyqtgraph as pg
import PyQt4
import numpy as np
import random
import main_designer
import therapist_select,patient_data,patient_data_altaBDD,patient_select,patient_database_load
import sys
import os
from PyQt4 import QtGui
from PyQt4 import QtCore
from  PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import QSize
from PyQt4.QtGui import QMainWindow, QLabel, QGridLayout,QWidget, QDialog, QMessageBox

pg.setConfigOption('background','w')
pg.setConfigOption('foreground','k')

Id_therapist="N/A"
Id_patient="N/A"
####################################################################################################################
#Datos entre formularios
####################################################################################################################

####################################################################################################################
#Creacion de la  ventana de seleccion del terapeuta
####################################################################################################################
class seleccion_del_terapeuta(QtGui.QDialog, therapist_select.Ui_Dialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.carga_imagenes()

        #boton para la apertura de cada una de las ventanas

        self.save_therapist_button.clicked.connect(self.SegundaVentana_paciente)

    def SegundaVentana_paciente(self):

        self.close()
        window = seleccion_paciente(self)
        window.show()



    def carga_imagenes(self):
        pixmap_therapist = QPixmap('doctor_small.png')
        pixmap_therapist = pixmap_therapist.scaled(self.therapist_image_label.width(),
                                                   self.therapist_image_label.height())
        self.therapist_image_label.setPixmap(pixmap_therapist)




class seleccion_paciente(QtGui.QDialog, patient_select.Ui_Dialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.carga_imagenes_paciente()
        self.load_patient_button.clicked.connect(self.ventana_carga_paceinte)
        self.save_patient_button.clicked.connect(self.TerceraVentana)

    def ventana_carga_paceinte(self):
        self.close()
        window = load_patient_database(self)
        window.show()

    def TerceraVentana(self):
        self.close()
        window = MyMainWindow(self)
        window.show()

    def carga_imagenes_paciente(self):
        pixmap_patient = QPixmap('patient_small.png')
        pixmap_patient = pixmap_patient.scaled(self.patient_image_label.width(),
                                               self.patient_image_label.height())
        self.patient_image_label.setPixmap(pixmap_patient)



class load_patient_database(QtGui.QDialog, patient_database_load.Ui_Dialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.load_patient_button.clicked.connect(self.Ventana_paciente_retorno)

    def Ventana_paciente_retorno(self):
        self.close()
        window = seleccion_paciente(self)
        window.show()






####################################################################################################################
#Creacion de la ventana principal para guardar los datos
####################################################################################################################
class MyMainWindow(QtGui.QMainWindow, main_designer.Ui_MainWindow):
    def __init__(self, parent=None):
        #super(MyMainWindow, self).__init__()
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.SYS_value.setStyleSheet("Background: white")
        self.SYS_value.setText("Mensaje del sistema")

        status_pulsera=1
        self.color_semaforo(status_pulsera)

####################################################################################################################
#Barra de estado en la parte inferior de la ventana principal
####################################################################################################################

        self.statusBar.showMessage(Id_therapist.center(130," "))


####################################################################################################################
# Semaforo colores de activacion.
####################################################################################################################

    def color_semaforo(self,status):

        if (status==1):
            self.rojo_widget.setStyleSheet("background:rgb(255, 30, 30)")
            self.verde_widget.setStyleSheet("background:rgb(160,160,160)")
            self.amarillo_widget.setStyleSheet("background:rgb(160,160,160)")
        if (status==2):
            self.rojo_widget.setStyleSheet("background-color:rgb(160,160,160)")
            self.verde_widget.setStyleSheet("background-color:rgb(160,160,160)")
            self.amarillo_widget.setStyleSheet("background-color:rgb(240, 240, 0)")
        if (status==3):
            self.rojo_widget.setStyleSheet("background-color:rgb(160,160,160)")
            self.verde_widget.setStyleSheet("background-color:rgb(0, 204, 0)")
            self.amarillo_widget.setStyleSheet("background-color:rgb(160,160,160)")










if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #ui = MyMainWindow()
    #ui=seleccion_paciente()
    ui = seleccion_del_terapeuta()
    ui.show()

    sys.exit(app.exec_())