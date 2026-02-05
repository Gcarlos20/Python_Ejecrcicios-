# (x,y) = 3x 2al cuadrado  - 2xy + y  2 al cuadrado 
 
def calcular_fucuncion(x,y):
    x = int(input("ingrese el valor de X"))
    y = int(input("ingrese el valor de Y"))
    resultado = 3 * (x**2) - 2 *x*y**2
    return resultado
def saludar():
    print("programa para calcular la funcion 3x^2 - 2xy + y^2")

saludar()
print ("el resultado es ", calcular_fucuncion(2,3))

