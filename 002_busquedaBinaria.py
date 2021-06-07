def main():
    objetivo = (int(input('Seleccione un numero: ')))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo)/2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'alto {alto},bajo {bajo},respuesta {respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo)/2

    print(f'La raiz cuadrada de {objetivo}  es {respuesta}')


if __name__ == '__main__':
    main()
