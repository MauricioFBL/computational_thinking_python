#             TUPLA
# Las tuplas son objetos inmutables 
# pueden cualquier tipo de objetos
# devuelven cualquier tipo de valor en una funcion
tupla = ()
type(tuple)
tupla = (1,'2',True)
my_tuple = (1,)
print(my_tuple)
my_tuple2 = (2,3,4)
print(my_tuple2)
my_tuple += my_tuple2
print(my_tuple)
x,y,z = my_tuple2
print(x,'__',y,'__',z,'__')

def coordenadas():
    return (5,4)
coordenadas = coordenadas()
x,y coordenadas()