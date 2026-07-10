def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            opt = int(input("Ingrese su opcion: "))
            if 1 <= opt <= 6:
                return opt
            else:
                print("Error, tiene que estar dentro de los parametros")
        except ValueError:
            print("Error, debe ser un numero entero")
def validar_codigo(valor):
    return valor.strip() != ""
def validar_nombre(valor):
    return valor.strip() != ""
def validar_tipo(valor):
    return valor.strip() != ""
def valirdar_color_principal(valor):
    return valor.strip() != ""
def validar_tamano(valor):
    if "S" or "M" or "L" in valor:
        return True
    else:
        return False
def validar_incluye_tarjeta(valor):
    if "s" or "n" in valor:
        return True
    else:
        return False
def validar_temporada(valor):
    return valor.strip() != ""
def validar_precio(valor):
    return valor > 0
def validar_unidades(valor):
    return valor >= 0
def unidades_tipo(arreglo_f,bodega):
    if not arreglo_f and bodega:
        print("Error, aun no tiene un arreglo agregado")
        return []
    tipo_arreglo = input("Ingrese el tipo de arreglo a consultar: ").lower().strip()
    total = 0
    for arreglo in arreglo_f:
        if tipo_arreglo in arreglo["tipo"].lower():
            for in_bodega in bodega:
                if arreglo["codigo"] == in_bodega["codigo"]:
                    bodega["unidades"] += total
            print(total)
def busqueda_precio(bodega):
    try:
        minimo = int(input("Ingrese el precio minimo de su rango: "))
        maximo = int(input("Ingrese el precio maximo de su rango: "))
    except ValueError:
        print("Error, ingrese un numero entero")
    else:
        precios = []
        for i in bodega:
            if minimo >= i["precio"] <= maximo and i["unidades"] != 0:
                nuevo_precios = {
                "nombre": i["nombre"],
                "codigo": i["codigo"]
                }
                precios.append(nuevo_precios)
                print(precios)
def buscar_codigo(arreglo_f,bodega):
    if not arreglo_f and bodega:
        print("Error, aun no agrega ningun arreglo")
        return[]
    busqueda = input("Ingrese el codigo a buscar: ").strip().lower()
    indices_encontrados = []
    for posicion,i in enumerate(bodega):
        if busqueda in i["codigo"]:
            indices_encontrados.append(posicion)
            return indices_encontrados,busqueda
        else:
            return False
def actualizar_precio(arreglo_f,bodega):
    esta_codigo = buscar_codigo(arreglo_f,bodega)
    if esta_codigo:
        try:
            nuevo_precio = int(input("Ingrese el nuevo precio: "))
        except ValueError:
            print("Error, ingrese un numero entero")
        else:
            for i in bodega:
                if esta_codigo in i["codigo"]:
                    bodega["precio"] = nuevo_precio 
def agregar_arreglo(arreglo_f,bodega):
    codigo = input("Ingrese el codigo de su arreglo: ").strip().lower()
    if not validar_codigo(codigo):
        print("Error, tiene que agregar algo y no solo espacios en blanco")
        return
    nombre = input("Ingrese el nombre del arreglo floral: ")
    if not validar_nombre(nombre):
        print("Error, tiene que agregar algo y no solo espacios en blanco")
        return
    tipo = input("Ingrese el tipo de arreglo que usted quiere: ").lower().strip()
    if not validar_tipo(tipo):
        print("Error, tiene que agregar algo y no solo espacios en blanco")
        return
    color_principal = input("Ingrese el color principal de su arreglo: ")
    if not valirdar_color_principal(color_principal):
        print("Error, tiene que agregar algo y no solo espacios en blanco")
        return
    tamano = input("Ingrese el tamaño de su arreglo (puede ser S, M o L): ")
    if not validar_tamano(tamano):
        print("Error, tiene que agregar algo y no solo espacios en blanco. ademas solo se valida S, M o L")
        return
    incluye_tarjeta = input("Ingrese si quiere que incluya tarjeta su arreglo (s/n): ")
    if not validar_incluye_tarjeta(incluye_tarjeta):
        print("Error, tiene que agregar algo y no solo espacios en blanco. tambien solo se valida s o n")
        return
    temporada = input("Ingrese temporada: ")
    if not validar_temporada(temporada):
        print("Error, tiene que agregar algo y no solo espacios en blanco")
        return
    try:
        precio = int(input("Ingrese precio: "))
        if not validar_precio(precio):
            print("Error, Ingrese un numero mayor a 0")
            return
        unidades = int(input("Ingrese unidades: "))
        if not validar_unidades(unidades):
            print("Error, ingrese un numero mayor o igual a 0")
            return
    except ValueError:
        print("Error, ingrese un numero entero")
    else:
        nuevo_arreglo = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "color_principal":color_principal,
        "tamaño" : tamano,
        "incluye_tarjeta" : incluye_tarjeta,
        "temporada" : temporada
        }
        nueva_bodega = {
        "codigo": codigo,
        "precio": precio,
        "unidades": unidades
        }
        arreglo_f.append(nuevo_arreglo)
        bodega.append(nueva_bodega)
        print("Arreglo agregado")
def eliminar_arreglo(arreglo_f,bodega):
    indices = buscar_codigo(arreglo_f, bodega)
    if not indices:
        return
    if len(indices) == 1:

        arreglo_f.pop(indices[0])
        bodega.pop(indices[0])
        print("arreglo eliminado")