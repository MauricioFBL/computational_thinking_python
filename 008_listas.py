#             LISTAS
# Secuencia de cualquier objeto
# Son mutables
# Eficientes en memoria
# range(comienzo,fin, pasos)
lista = [1,2,3]
print(lista[1:])
# Agregar elemento
lista.append(4)
print(lista)
# Modificar elemento de lista
lista[0] = 'a'
print(lista)
# eliminar el ultimo elemento de lista
lista.pop()
print(lista)
for element in lista:
    print(element)
    
a = [1,2,3]
b = a
print(a)
print(b)
c = [a,b]
print(c)
a.append(5)
print(a)
print(c)
# Clonacion
a = [1,2,3]
print(id(a))
b = a
print(id(b))
c = list(a)
(print(id(c)))
d = a[::]
# List comprehension aplicar operraciones todos los valores de una lista
lista = list(range(100))
print(lista)
double = [i * 3 for i in lista]
print(double)
pares = [i for i in lista  if i % 2 == 0]
print(pares)
                    # METODOS DE LAS LISTAS

# lista.extend(iterable) #extiende la lista con valores dentro de un iterable como un range()
# lista.insert(i, ‘valor’) #Agrega un valor en la posición i y recorre todos los demás. No borra nada.
# lista.pop(i) #Elimina valor en la posición i de la lista.
# lista.remove(‘valor’) #Elimina el primer elemento con ese valor.
# lista.clear() #Borra elementos en la lista.
# lista.index(‘valor’) #Retorna posición del primer elemento con el valor.
# lista.index(‘valor’, start, end) #Retorna posición del elemento con el valor dentro de los elementos desde posición start hasta posición end)
# lista.count(‘valor’) #Cuenta cuántas veces esta ese valor en la lista.
# lista.sort() #Ordena los elementos de mayor a menor.
# lista.sort(reverse = True) #Ordena los elementos de menor a mayor.
# lista.reverse() #Invierte los elementos
# lista.copy() #Genera una copia de la lista. También útil para clonar listas.
