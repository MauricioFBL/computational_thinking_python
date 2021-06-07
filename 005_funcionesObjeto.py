def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
        print(resultado)


# Funciones en estructuras de datos
# Las funciones también se pueden incluir en diversas estructuras que las permiten almacenar. 
# Por ejemplo, una lista puede guardar diversas funciones a aplicar o un diccionario las puede almacenar como valores.

def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))
    print('el resultado es: ',resultado)
    return resultado
    


def run():
    print('Operaciones con funciones como objeto')
    nums = [2,4,6]
    aplicar_operacion(multiplicar_por_dos,nums)
    
    # Funciones lambda en una expresión es utilizando el keyword lambda. lambda tiene la siguiente sintaxis: 
    # lambda <vars>: <expresion>.
    sumar = lambda x, y: x + y
    print(sumar(5,12))
    print(aplicar_operaciones(-17))
