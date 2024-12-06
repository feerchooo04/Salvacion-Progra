from Validaciones import Utiles 

def Diccionario(): 
    return {'Inventario': inInventario,
            'MatrizDatos': iniMatriz,
            'ArchivoBIN': archivoBin,
            'Archivo': Utiles['AbrirArchivo']
    }

def inInventario(inventario, filas): #return
    if (len(inventario) == 0 and (filas > 0)):
        for i in range(filas - 1):
            inventario.append("0")

def iniMatriz(matriz, filas, columnas): #return
    if (len(matriz) == 0 and (filas > 0) and (columnas > 0)):
        for i in range(filas - 1):
            matriz.append([0] * (columnas - 1))
    return matriz

def archivoBin(Inventario.bin, 'rb'):
    archivo = Utiles['AbrirArchivo']
    if (archivo == None):
        return print("El archivo no existe")
    else:
        print("El archivo abrio")

Proceso = Diccionario()
