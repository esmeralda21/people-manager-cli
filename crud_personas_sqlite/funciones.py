def recorrer_lista_diccionario(lista_diccionario):
<<<<<<< HEAD
    """
    This function iterates through the list of dictionaries extracted from the database and displays it in an ordered manner.
    """
=======
>>>>>>> bb8d0dc (Agrega funciones de personas y persistencia en JSON)
    print("Aca esta la lista de diccionarios")
    for persona in lista_diccionario:
        for clave, valor in persona.items():
            print(f"{clave} : {valor}")
        print("\n")

<<<<<<< HEAD

def mayor_edad(lista_diccionario):
    """This function displays all the data of the oldest person in the database
    """
=======
def mayor_edad(lista_diccionario):
>>>>>>> bb8d0dc (Agrega funciones de personas y persistencia en JSON)
    contador = 0
    persona_mayor = None
    for persona in lista_diccionario:
        if persona["edad"] > contador:
            contador = persona["edad"]
            persona_mayor = persona
    if contador > 0:
        return persona_mayor
    else:
        return None

<<<<<<< HEAD

def ordenar_tupla(basedepersonas):
    """This function organizes the database into dictionaries so that it can then be viewed in an organized manner.
    """
    personas_lista =[]
    for persona in basedepersonas:
        persona_diccionario = {
            "id": persona[0],
            "nombre": persona[1],
            "edad": persona[2],
            "ciudad": persona[3]
        }
        personas_lista.append(persona_diccionario)
    return personas_lista

def validar_rango(rango):
    """This function validates that the range of options is adequate
    """
    if rango.isnumeric():
=======
def buscar_persona(lista_diccionario, nombre_buscado):
    nombre =  None
    for persona in lista_diccionario:
        if persona["nombre"].lower() == nombre_buscado.lower():
            nombre = persona
            break

    return nombre



def validar_nombre(nombre):
    if nombre.isalpha():
>>>>>>> bb8d0dc (Agrega funciones de personas y persistencia en JSON)
        return True
    else:
        return False

<<<<<<< HEAD
def validar_nombre_o_ciudad(nombre):
    """ This function validates that the name or city consists only of letters, spaces, or hyphens.
    """
    muestra = 0
    for letra in nombre:
        if letra.isalpha() or letra.isspace() or letra == "-":
=======
def validar_edad(edad):
    if edad.isnumeric():
        return True
    else:
        return False

def validar_ciudad(ciudad):
    muestra = 0
    for letra in ciudad:
        if letra.isalpha() or letra.isspace():
>>>>>>> bb8d0dc (Agrega funciones de personas y persistencia en JSON)
            muestra = 1
        else:
            muestra = 0
            break
    if muestra == 1:
        return True
    else:
        return False


<<<<<<< HEAD
def validar_edad(edad):
    """This function validates that the age field is numeric and positive.
    """
    if edad.isnumeric():
        return True
    else:
        return False


def validar_id(id):
    """This function validates that the id or index is numeric and positive.
    """
    if id.isnumeric():
        return True
    else:
        return False


=======
def mayor_lista(lista):
    contador = lista[0]
    for numero in lista:
        if numero > contador:
            contador = numero
    return contador
>>>>>>> bb8d0dc (Agrega funciones de personas y persistencia en JSON)
