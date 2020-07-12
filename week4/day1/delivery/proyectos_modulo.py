

# MODULO DE FUNCIONES EN ESTADO BRAINSTORMING 
'''            BRAINSTORMING              '''
###            braistorming               

# Generar archivo con la lista de la compra
def lista_compra ():
    print ("Jalou!:","\n", "Para añadir artículos a la lista escribe '1' ", "\n", "Para ver la lista escribe '2'")
    inicio = input("Elige una opción (1 o 2)") 
    if inicio == 1:
        anadir()
    else:
        print("La lista actualizada es:" , lista_imprimir)
    # Definicion de funciones basicas que son anadir e imprimir:
    def anadir ():
        nuevo = []
        art = input ("Añade tu articulo a la lista:")
        cant = int(input ("Escribe la cantidad"))
        nuevo.append (art)
        # nuevo = nuevo + ['cant','art']
        print ("se añade", cant, art , "al pedido")
        print (nuevo)
        if art !=0 :
            anadir ()
        else:
            guardar_archivo()

    with open('lista_compra.txt', 'a') as outfile:
        print(type(outfile))
        lista_imprimir = lista_imprimir + anadir





def aladino ():
    #Esta función realiza tres tareas y se autodestruye



def capitan_calzoncillos():
    # Esta funcion le dices cuantos dias te vas de viaje y devuelve una tabla de lunes a domingo con el total de calzoncillos.



def deus_est_machina ():
    # Esta función crea una copia de archivo con un ejecutable que se reproduce como un virus



def Tio_Gilito ():
    # Función para llenar de pasta mis bolsillos



def Daigual_lo_que_comas ():