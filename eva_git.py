alumnos = []

while True:
    print("1. Agregar alumno")
    print("2. Listar alumnos")  
    print("3. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        alumnos.append(input("Nombre: "))
    elif opcion == "2":
        for a in alumnos:
            print(alumnos)
    elif opcion == "3":
        break
    else:
        print("Opción no válida.")
