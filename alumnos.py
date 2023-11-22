def alumnos():

    alumnos = []

    respuesta = True

    while respuesta:

        alumno = []

        alumno.append(input("Ingrese el numero del alumno:\n"))
        alumno.append(float(input("ingrese la primera nota:\n")))
        alumno.append(float(input("ingrese la segunda nota:\n")))
        alumno.append(float(input("ingrese la tercera nota:\n")))

        alumnos.append(alumno)

        respuesta = input("¿Desea ingresar otro alumno?\nIngrese s para si.\nIngrese cualquier cosa para no.\n")
        if respuesta == "s":
            respuesta = True
        else:
            respuesta = False



    if len(alumnos) > 0:
        print("Listado de las notas e los alumnos")
        print("Nombre[]Nota1\tNota2\tNota3")
        for alumno in alumnos:
            print(alumno[0]+"\t"+str(alumno[1])+"\t\t"+str(alumno[2])+"\t\t"+str(alumno[3]))

    if len(alumnos) > 0:
        print("\nListado de las notas e los alumnos")
        print("Nombre\tPromedio")
        for alumno in alumnos:
            promedio = (alumno[1]+alumno[2]+alumno[3])/3
            print(alumno[0]+"\t" +str(round(promedio,1)))


