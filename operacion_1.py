from operacion_1 import menu,leer_opcion,agregar_arreglo,unidades_tipo,busqueda_precio,actualizar_precio,eliminar_arreglo
arreglo_f = []
bodega = [] 
salida_menu = False
while not salida_menu:
    menu()
    opt = leer_opcion()
    if opt == 1:
        unidades_tipo(arreglo_f,bodega)
    elif opt == 2:
        busqueda_precio(bodega)
    elif opt == 3:
        actualizar_precio(arreglo_f,bodega)
    elif opt == 4:
        agregar_arreglo(arreglo_f,bodega)
    elif opt == 5:
        eliminar_arreglo(arreglo_f,bodega)
    elif opt == 6:
        salida_menu = True
    else:
        print("Error, ingrese un valor dentro de los parametros")