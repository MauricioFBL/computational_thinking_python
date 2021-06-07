#             DICCIONARIOS
# HASH NAPS
# Son similares alas listas, pero usan llaves en lugar de indices
# No hay un orden interno
# son mutables
# son iterables
# range(comienzo,fin, pasos)
diccionario = {
    'Daniel': 24,
    'Erika': 32,
    'Jaime': 50,
}
print(diccionario['Daniel'])
# Get element by Key
print(diccionario.get('Daniel'))
# Get element by key or return a given value if not exist the key
print(diccionario.get('Juan',30))
# Get element by key or return a given value if not exist the key
print(diccionario.get('Daniel',30))
# Give new value by the key
diccionario['Jaime'] = 70
print(diccionario)
# Add new element 
diccionario['Pedro'] = 50
print(diccionario)
diccionario.update({'Alejandra':38})
print(diccionario)
# Dlete element by key¿
del diccionario['Jaime']
print(diccionario)
# Delete the las item
diccionario.popitem()
print(diccionario)
# Copy dictionary
diccionario2 = diccionario.copy()
print('diccionario')
print(diccionario)
print('ubicacion diccionario',id(diccionario))
print('diccionario2')
print('ubicacion diccionario 2',diccionario2)
print(id(diccionario2))
# Pointer at the same dictionary
a = diccionario
print(id(diccionario))
print(id(a))
# Delete all items in a dictionary
diccionario2.clear()
print(a)
# Get keys of dictionary in a list
print('Get keys of dictionary')
x = diccionario.keys()
print(x)
# Get keys of dictionary
print('Get valuess of dictionary')
x = diccionario.values()
print(x)
# Get items of dictionary
x = diccionario.items()
print(x)
# loop dictionary by key
for key in diccionario.keys():
    print(key)
# loop dictionary by value
for value in diccionario.values():
    print(value)
# loop dictionary by value and key
for key, value in diccionario.items():
    print(key, value)

print('Daniel' in diccionario)
print('Tom' in diccionario)

# Length of dictionary
print(len(diccionario))
#              Dictionary Comprehension
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# This is the general template for dictionary comprehension in Python:
# dict_variable = {key:value for (key,value) in dictonary.items()}
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)
dict1_keys = {k*2:v for (k,v) in dict1.items()}
print(dict1_keys)
numbers = range(10)
new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}
print(new_dict_comp)
# Initialize `fahrenheit` dictionary 
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
print(fahrenheit)
#Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))
print(celsius)
#Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))
print(celsius_dict)







