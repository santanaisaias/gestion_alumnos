
lista_alumnos = []
lista_notas = []

while True:
    print("1. nuevo alumno a la lista")
    print("2. Agregar nota a alumno")
    print("3. Mostrar notas alumnos")
    print("4. Calcular promedio alumnos")
    print("5. Mostrar lista de aprobación")
    print("6. Salir del programa")
    print ("ya chao")

    opcion = input("Ingrese una opción a ejecutar: ")

    if opcion == "1":
        nombre = input("Ingrese nombre del alumno nuevo: ").upper()
        lista_alumnos.append(nombre)
        lista_notas.append([])
        print(f"Se ingresó alumno {nombre} correctamente.")
    
    elif opcion == "2":
        nombre = input("Ingrese el nombre del alumno cuya nota va a ingresar: ").upper()
        if nombre in lista_alumnos:
            indice = lista_alumnos.index(nombre)
            N_notas =  int(input(f"Ingrese la cantidad de notas que desea añadir a {nombre}: "))
            for i in range(N_notas):
                nota = float(input(f"Ingrese nota {i+1}: "))
                lista_notas[indice].append(nota)
            print(f"Se han agregado las notas de {nombre} correctamente.")
        else:
            print("El estudiante ingresado no se encuentra en la lista.")
    elif opcion == "3":
        for nombre, notas in zip(lista_alumnos, lista_notas):
            print(f"{nombre}: {notas}")
    elif opcion == "4":
        for nombre, notas in zip(lista_alumnos, lista_notas):
            try:
                promedio = sum(notas)/len(notas)
                print(f"{nombre}: {promedio}")
            except ZeroDivisionError:
                print(f"{nombre}: SIN NOTAS")
        
    elif opcion == "5":
        for nombre, notas in zip(lista_alumnos, lista_notas):
            try:
                promedio = sum(notas)/len(notas)
                if promedio >= 4.0:
                    print(f"{nombre}: APROBADO")
                else:
                    print(f"{nombre}: REPROBADO")
            except ZeroDivisionError:
                print(f"{nombre}: SIN NOTAS")
        

    elif opcion == "6":
        print("Hasta luego!")
        break
    else:
        print("Su opción no es válida.")
