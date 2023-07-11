import numpy as np
import datetime

#globales

tabla = np.array([[' ', ' ', ' ',' '],[' ', ' ', ' ',' '], [' ', ' ', ' ',' '],[' ', ' ', ' ',' '],[' ', ' ', ' ',' '],[' ', ' ', ' ',' '],[' ', ' ', ' ',' '],[' ', ' ', ' ',' '],[' ', ' ', ' ',' '],[' ', ' ', ' ',' ']])
depto_seleccionados = []
clientes = []

def mostrar_deptos():
    print("    A.   B.    C.   D.   ")
    for i in range(len(tabla)):
        fila = len(tabla) - i
        print("{}.".format(fila), end=' ')
        for j in range(len(tabla[0])):
            print("{}  |".format(tabla[i][j]), end=' ')
        print()
        print("  -----------------------")

#mostrar los deptos disponibles
def mostrar_deptos_disponibles():
    print("Departamentos Disponibles: ")
    mostrar_deptos()

#compra de depto
def comprar_departamento():
    mostrar_deptos_disponibles()
    columna = input("Ingrese el tipo de departamento (A-D): ")
    fila = int(input("Ingrese el piso del departamento (1-10):  "))
    
    columnas_validas = ['A', 'B', 'C', 'D']
    if fila < 1 or fila > len(tabla) or columna not in columnas_validas:
        print("Coordenadas inválidas. Inténtelo de nuevo.")
        return
    
    columna_index = columnas_validas.index(columna)
    fila_index = len(tabla) - fila
    
    if tabla[fila_index][columna_index] == ' ':
        confirmacion = int(input("Desea confirmar la selección y comprar departamento? 1. SI - 2. NO: "))
        if confirmacion == 1:
            depto = {
                'fila': fila,
                'columna': columna,
            }
            depto_seleccionados.append(depto)
            tabla[fila_index][columna_index] = 'X'
                    
            ver_detalle = int(input("Desea ver los detalles del departamento seleccionado? 1. SI - 2. NO: "))
            if ver_detalle == 1:
                mostrar_detalle_depto()
                
            print("Por favor ingrese su RUT sin puntos ni dígito verificador")
            rut = input("Ingrese su RUT: ")
            cliente = {
                'rut': rut,
            }
            clientes.append(cliente)
            print("Departamento Comprado exitosamente.")
        else:
            print("Compra de Departamento cancelada.")
    else:
        print("No está disponible.")

#muestra los detalles del depto
def mostrar_detalle_depto():
    if depto_seleccionados:
        for depto in depto_seleccionados:
            print("Departamento seleccionado: Piso {}, Tipo {}".format(depto['fila'], depto['columna']))
            print("Detalles del depto:")
            precio = obtener_precio_lote(depto['columna'])
            print("Precio: {} UF".format(precio))
            print()
    else:
        print("No se han seleccionado departamentos.")

#se optiene el precio del depto
def obtener_precio_lote(columna):
    precios_departamento = [3800, 3000, 2800, 3500]
    tipos_departamento = ['A', 'B', 'C', 'D']
    tipo_departamento = columna
    precio = precios_departamento[tipos_departamento.index(tipo_departamento)]
    return precio

#muetsra los clientes
def mostrar_clientes():
    if clientes:
        print("Clientes:")
        for cliente in clientes:
            print("RUT: {}".format(cliente['rut']))
            print()
    else:
        print("No hay clientes registrados.")

#muestra ventas Totales 
def Mostrar_ventas_totales():
    ventas_totales = {}
    total_cantidad = 0
    total_monto = 0
    for depto in depto_seleccionados:
        tipo = depto['columna']
        precio = obtener_precio_lote(tipo)
        
        if tipo in ventas_totales:
            ventas_totales[tipo]['cantidad'] += 1
            ventas_totales[tipo]['total'] += precio
        else:
            ventas_totales[tipo] = {'cantidad': 1, 'total': precio}

        total_cantidad += 1
        total_monto += precio
    
    print("=== Ventas Totales ===")
    print("Tipo | Cantidad | Total")
    print("----------------------|----------|-------")
    for tipo, ventas in ventas_totales.items():
        cantidad = ventas['cantidad']
        total = ventas['total']
        print("{} | {} | {}".format(tipo, cantidad, total))
    print("----------------------|----------|-------")
    print("Total                | {} | {}".format(total_cantidad, total_monto))

#opcion salida
def salir():
    fecha = datetime.datetime.now()
    print("Andres Guarumo")
    print(F"Fecha Actual: {fecha}")
    return
    
#menu principal 
def Menu_CasaFeliz():
    while True:
        print("=== MENÚ CASA FELIZ ===")
        print("1. Comprar Departamento")
        print("2. Mostrar Departamentos Disponibles")
        print("3. Ver Listado de Compradores")
        print("4. Mostrar Ganancias Totales")
        print("5. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                comprar_departamento()
            elif opcion == 2:
                mostrar_deptos_disponibles()
            elif opcion == 3:
                mostrar_clientes()
            elif opcion == 4:
                Mostrar_ventas_totales()
            elif opcion == 5:
                salir()
                break
            else:
                print("Opción inválida. Inténtelo de nuevo.")
        except:
            print("Opción inválida. Inténtelo de nuevo.")

Menu_CasaFeliz()

