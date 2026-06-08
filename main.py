import sqlite3

conexion = sqlite3.connect("personas.db") #llamamos a la base de datos
conexion.row_factory = sqlite3.Row #hacemos que lo que se trae de la base de datos se pueda trabajar como fila de datos
cursor = conexion.cursor()

cursor.execute("""  
CREATE TABLE IF NOT EXISTS personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    ciudad TEXT NOT NULL
)
""") #creamos la tabla si no existe

from funciones import validar_nombre_o_ciudad
from funciones import validar_edad
from funciones import ordenar_tupla
from funciones import recorrer_lista_diccionario
from funciones import validar_id # llamamos a las funciones necesarias para el proyecto

while True: # creamos el menu de opciones
    menu = input    ("1. Agregar persona\n"
                     "2. Ver lista completa de personas\n"
                     "3. Cuantas personas existen\n"
                     "4. Buscar persona por nombre\n"
                     "5. Modificar persona\n"
                     "6. Eliminar persona\n"
                     "7. Salir\n"
                     "Que deseas hacer? \n").strip()
    if menu == "1": # funcion para agregar persona
        persona = {
            "nombre": "",
            "edad": 0,
            "ciudad": "",
        }
        while True:
            persona["nombre"] = input("Dime el nombre").strip()
            nombre = validar_nombre_o_ciudad(persona["nombre"]) #validamos que sea un nombre valido

            if nombre: #nombre valido

                cursor.execute("SELECT * FROM personas WHERE nombre = ?", (persona["nombre"],))
                persona_encontrada = cursor.fetchone()


                if persona_encontrada: #verificamos que el nombre ya no exista en la base de datos
                    print("de momento no aceptamos nombres repetidos")
                else:
                    break
            else: #nombre no es valido
                 print("tienes que indicarme un nombre valido")

        while True:
            persona["edad"] = input("Dime el edad").strip()
            validaredad = validar_edad(persona["edad"]) #validamos que la edad sea valida

            if validaredad: #edad valida
                persona["edad"] = int(persona["edad"])
                break
            else: #edad no valida
                print("tienes que indicarme un edad valido")

        while True:
            persona["ciudad"] = input("Dime el ciudad").strip()
            validarciud = validar_nombre_o_ciudad(persona["ciudad"]) #validamos que la ciudad sea valida

            if validarciud: #ciudad alidad
                break
            else: #ciudad no valida
                print("tienes que indicarme un ciudad valido")

        cursor.execute(
            "INSERT INTO personas (nombre, edad, ciudad) VALUES (?, ?, ?)",
            (persona["nombre"], persona["edad"], persona["ciudad"]) #insertamos los nuevos datos en la bd
        )
        conexion.commit()
        print("Datos guardados con exito")

    elif menu == "2": #ver la lista completa de la BD
        cursor.execute("SELECT * FROM personas")
        nombre_personas = cursor.fetchall()
        if  len(nombre_personas) == 0: #la base de datos esta vacia
            print("No hay personas")
        else: # se ordena y muestra todos los datos
            lista_ordenada = ordenar_tupla(nombre_personas)
            recorrer_lista_diccionario(lista_ordenada)

    elif menu == "3": #cantidad de datos que tiene la BD
        cursor.execute("SELECT id FROM personas")
        cantidad_personas = cursor.fetchall()
        print (f"La base tiene un total de {len(cantidad_personas)} personas ")

    elif menu == "4": #buscar usuario por nombre
        nombre = input("Dime el nombre que quieres buscar:").strip()

        if validar_nombre_o_ciudad(nombre): #validamos que sea un nombre valido
            cursor.execute("SELECT * FROM personas WHERE nombre = ?", (nombre,))
            persona_encontrada = cursor.fetchone()

            if persona_encontrada: #se encontro la persona y se muestra
                print("persona encontrada:\n")
                print(f"id: {persona_encontrada['id']}")
                print(f"nombre: {persona_encontrada['nombre']}")
                print(f"edad: {persona_encontrada['edad']}")
                print(f"ciudad: {persona_encontrada['ciudad']}\n")
            else: #la persona no existe con ese nombre en la BD
                print("persona no encontrada")

        else: #el nombre no es valido
            print("tienes que indicarme un nombre valido, volvemos al menu")


    elif menu == "5": #modificar algun dato de BD

        conoce_validad = input("conoces el ID de la persona que quieres modificar?\n"
                            "1. SI\n"
                            "2. NO\n").strip()
        if conoce_validad == "1": #el usuario conoce el ID que desea buscar

            persona_id = input("Ingrese el ID del persona que quieres modificar:").strip()
            id_persona = validar_id(persona_id) #el id es valido, numerico y positivo

            if id_persona: #id valido
                persona_id= int(persona_id)
                cursor.execute("SELECT * FROM personas WHERE ID = ?", (persona_id,))
                ID_encontrada = cursor.fetchone()

                if ID_encontrada: #el id fue encontrado en la BD

                    print("ficha encontrada:\n") #se muestran los datos encontrados segun el ID

                    print(f"id: {ID_encontrada['id']}")
                    print(f"nombre: {ID_encontrada['nombre']}")
                    print(f"edad: {ID_encontrada['edad']}")
                    print(f"ciudad: {ID_encontrada['ciudad']}\n")

                    valor_modificado = input ("Cual campo desea modificar?\n" #pregunta que datos quiere modificar el usuario
                          "1: Nombre\n"
                          "2: edad\n"
                          "3: ciudad\n")
                    if valor_modificado == "1": #modificar nombre
                        nuevo_nombre = input("Dime el nuevo nombre:").strip()
                        validarnombre = validar_nombre_o_ciudad(nuevo_nombre) #valida que el nombre a modificar sea valido

                        if validarnombre: #nombre valido
                            cursor.execute("UPDATE personas SET nombre = ? WHERE id = ?", (nuevo_nombre, persona_id))
                            conexion.commit() #modifica el nombre del ID que indico el usuario
                        else: #nombre no valido
                            print("Ingrese un nombre valido")

                    elif valor_modificado == "2": #modificar edad
                        nuevo_edad = input("Dime la nueva edad:").strip()
                        validaredad = validar_edad(nuevo_edad) #valida que la edad a modificar sea valida

                        if validaredad: #edad valida
                            nuevo_edad = int(nuevo_edad)

                            cursor.execute("UPDATE personas SET edad = ? WHERE id = ?", (nuevo_edad, persona_id))
                            conexion.commit() #modifica la edad del ID que indico el usuario

                        else: #edad no valida
                            print("tienes que indicarme un edad valido")


                    elif valor_modificado == "3": #modificar ciudad
                        nuevo_ciudad = input("Dime el nuevo ciudad:").strip()
                        validarciud = validar_nombre_o_ciudad(nuevo_ciudad) #valida que la ciudad a modificar sea valida

                        if validarciud: #ciudad valida
                            cursor.execute("UPDATE personas SET ciudad = ? WHERE id = ?", (nuevo_ciudad, persona_id))
                            conexion.commit() #modifica la edad del ID que indico el usuario

                        else:#ciudad no valida
                            print("tienes que indicarme un ciudad valido")
                    else: #la opcion a modificar no existe
                        print("esa opcion no existe")
                        continue
                    print("ficha actualizada:\n")

                    cursor.execute("SELECT * FROM personas WHERE ID = ?", (id_persona,))
                    ID_encontrada2 = cursor.fetchone() #buscamos la ficha con los datos actualizados


                    print(f"id: {ID_encontrada2['id']}")
                    print(f"nombre: {ID_encontrada2['nombre']}")
                    print(f"edad: {ID_encontrada2['edad']}")
                    print(f"ciudad: {ID_encontrada2['ciudad']}\n")
                else: #el ID que indico el usuario no se encontro
                    print("No se encontro el ID")
            else: # el usuario coloco algun ID que no numerico ni positivo
                print("Ingrese una opcion valida")

        elif conoce_validad == "2": #el usuario no conoce el ID que desea modificar
            print ("Pidele al administrador el ID")
        else: #el usuario no selecciono una opcion valida
            print("Ingrese una opcion valida")
    elif menu == "6": #eliminar fila de la BD
        conoce_validad = input("conoces el ID de la persona que quieres eliminar?\n"
                               "1. SI\n"
                               "2. NO\n").strip()
        if conoce_validad == "1": #valida si el usuario conoce el ID que desea eliminar

            persona_id = input("Ingrese el ID del persona que quieres eliminar:").strip()
            id_persona = validar_id(persona_id) #valida que el ID sea valido

            if id_persona: #el id es valido

                cursor.execute("SELECT * FROM personas WHERE ID = ?", (persona_id,))
                ID_encontrada2 = cursor.fetchone()

                if ID_encontrada2: #el ID se encontro y se muestran los datos
                    print(f"Estas seguro que quieres eliminar a:\n")

                    print(f"id: {ID_encontrada2['id']}")
                    print(f"nombre: {ID_encontrada2['nombre']}")
                    print(f"edad: {ID_encontrada2['edad']}")
                    print(f"ciudad: {ID_encontrada2['ciudad']}\n")

                    verificacion = input(
                                "1. SI\n"
                                "2. NO\n").strip()

                    if verificacion == "1": #el usuario confirma que si quiere eliminar esos datos
                        cursor.execute("DELETE FROM personas WHERE ID = ?", (persona_id,))
                        conexion.commit()

                        print("información eliminada\n")
                    elif verificacion == "2": #el usuario cambia de opinion y no quiere cambiar los datos
                        continue
                    else: #el usuario indico una opcion no valida
                        print("Ingrese una opcion valida")
                else:
                    print("No se encontro el ID")
            else:
                print("No se encontro el ID")
        elif conoce_validad == "2": #el usuario no conoce el ID que desea eliminar
            print ("Pidele al administrador el ID")
        else: #el usuario indico una opcion no valida
            print("Ingrese una opcion valida")
    elif menu == "7": #salir del programa
        print("Vuelve pronto\n")
        break
    else: #usuario indica una opcion no valida
        print("Ingrese una opcion valida")







conexion.commit()

conexion.close()