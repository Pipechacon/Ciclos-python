import os 

bandera = True
while bandera:
    print("MENU DE CICLOS")
    print("1. NUMERO DEL 1 AL 10")
    print("2. NUMERO HASTA QUE EL USUARIO QUIERA")
    print("3. NUMERO INICIAL Y FINAL")
    print("4. SALIR")

    opc = int(input("Seleccione una opción: "))

    if opc == 1:
        print("SECUENCIA DEL 1 AL 10")
        for i in range(1, 11):
            print(i)
    elif opc == 2:
        print("NUMERO HASTA QUE EL USUARIO QUIERA")
        numeros = []

        while True:
            num = input("Introduzca un número (o 'q' para salir): ")
            if num.lower() == 'q':
                break
            numeros.append(int(num))
        
        print("Los números ingresados son:", numeros)

    elif opc == 3:
        print("NUMERO INICIAL Y FINAL")
        inicio = int(input("intruzca el primer numero: "))
        fin = int(input("intruzca segundo numero "))

        for i in range(inicio, fin + 1):
            print(i)

    elif opc == 4:
        print("CHAO GRACIAS")
        bandera = False 
