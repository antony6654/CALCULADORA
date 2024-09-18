import flet as ft

def calc_suma(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1+num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Eror ingresa valores correctos"
        
def calc_resta(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1-num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Eror ingresa valores correctos"
        
def calc_mult(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1*num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Eror ingresa valores correctos"
        
def calc_div(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1/num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Eror ingresa valores correctos"
        
def main(page:ft.Page):
    # Funciones de manejo de eventos
    def on_calc_suma(e):
        calc_suma(txtNum1, txtNum2. lblResultado)
        page.update()
    
    def on_calc_resta(e):
        calc_resta(txtNum1, txtNum2. lblResultado)
        page.update()
        
    def on_calc_multi(e):
        calc_mult(txtNum1, txtNum2. lblResultado)
        page.update()
        
    def on_calc_div(e):
        calc_div(txtNum1, txtNum2. lblResultado)
        page.update()
        
    def limpiar(e):
        txtNum1.value = ""
        txtNum2.value = ""
        lblResultado.value = "Resultado: "
        page.update()
        


ft.app(main)
