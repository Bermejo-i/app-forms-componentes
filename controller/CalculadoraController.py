
from PyQt5 import QtWidgets, uic
from service import CalculadoraService

class CalculadoraController:

    def __init__(self) -> None:
       app = QtWidgets.QApplication([])
       self.ventana = uic.loadUi("view/frmcalculadora.ui")
       self.ventana.btncalcular.clicked.connect(self.onclickbtncalcular)
       self.ventana.show()
       app.exec()

    
    def onclickbtncalcular(self):   
        resultado=0
        operacion=""
        try:
            num1=int(self.ventana.TXTNUMERO1.text())
            num2=int(self.ventana.TXTNR2.text())
            if self.ventana.RBSUMA.isChecked():
                resultado=CalculadoraService.suma(num1,num2)
                operacion="Suma"
            elif self.ventana.RBRESTA.isChecked():
                resultado=CalculadoraService.resta(num1,num2)
                operacion="Resta"
            elif self.ventana.RBMULTIPLICA.isChecked():
                resultado=CalculadoraService.multiplicacion(num1,num2)
                operacion="Multiplicacion"
            elif self.ventana.RBDIVIDE.isChecked():
                resultado=CalculadoraService.divide(num1,num2)
                operacion="Division"
            else:
                resultado=0
                operacion="Elegir operacion"
        except:
            operacion="Ingresar valores numericos"
        finally:
            self.ventana.LBLRESULTADO.setText(operacion+" = "+str(resultado))