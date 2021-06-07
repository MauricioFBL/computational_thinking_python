#             RANGOS
# Secuencia de enteros
# Son inmutables
# Eficientes en memoria
#  range(comienzo,fin, pasos)

a = range(2,10,3)
print(type(a))
print(a)
for i in a:
    print(i)

id(range)

for num in range(0,100,3):
    print(num)


for num in range(1,100,2):
    print(num)