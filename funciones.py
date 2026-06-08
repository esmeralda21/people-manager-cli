def recorrer_lista_diccionario(lista_diccionario):
    """
    This function iterates through the list of dictionaries extracted from the database and displays it in an ordered manner.
    """
    print("Aca esta la lista de diccionarios")
    for persona in lista_diccionario:
        for clave, valor in persona.items():
            print(f"{clave} : {valor}")
        print("\n")


def mayor_edad(lista_diccionario):
    """This function displays all the data of the oldest person in the database
    """
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
        return True
    else:
        return False

def validar_nombre_o_ciudad(nombre):
    """ This function validates that the name or city consists only of letters, spaces, or hyphens.
    """
    muestra = 0
    for letra in nombre:
        if letra.isalpha() or letra.isspace() or letra == "-":
            muestra = 1
        else:
            muestra = 0
            break
    if muestra == 1:
        return True
    else:
        return False


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


