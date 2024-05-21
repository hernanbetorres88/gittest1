def suma(a,b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "error: division por cero"
operacion= input("Introduce la operacion(+, -, *, /): ")
Num1 = float(input("introduce el primer numero: "))
Num2 = float(input("introduce el segundo numero; "))
if operacion =="+":
     print("resultado:",suma(Num1, Num2))
elif  operacion == "-":
    print("resultado:", resta(Num1, Num2))
elif operacion =="*":
    print("Resultado; ", multiplicacion(Num1, Num2))
elif operacion == "/":
    print("resultado: ",divison(Num1, Num2))
else:
    print("operacion no valida")
