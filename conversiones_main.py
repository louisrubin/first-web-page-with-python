""" ARCHIVO CONVERTIDOR DE BASE b2 -> b10, A LAS DEMAS BASES """
import os
import re
cls = lambda: os.system("cls")   # lambda sirve para crear funciones pequeñas y "anónimas", actúa como un "def"

def ifs_menu(numero, base_origen, base_a_convertir):
    numero = numero.upper()

    if base_origen == base_a_convertir:
        print (" [",numero,"] EN BASE ", base_origen, " =  [",numero,"] EN BASE ",base_a_convertir)
        print()


    elif base_a_convertir == 10:

        if base_origen > 10 and base_origen <= 16:   # si el num ingr. está entre 11 y 16, usa "hexa_a_decimal()"
            decimal = hexa_a_decimal(numero, base_origen)
        else:
            entero = string_a_entero(numero)        # saca el guion del negativo para retornarlo como entero
            decimal = baseX_a_b10(entero, base_origen)

        numero.upper()
        print (" [",numero,"] EN BASE ", base_origen, " =  [",decimal,"] EN BASE ",base_a_convertir)
        print()
        # return


    elif base_a_convertir >= 11 and base_a_convertir <= 16:

        if base_origen <= 10:
            entero = string_a_entero(numero)
            decimal = baseX_a_b10(entero, base_origen)
            hexa = decimal_a_hexa(decimal, base_a_convertir)
        else:
            decimal = hexa_a_decimal(numero, base_origen)
            hexa = decimal_a_hexa(decimal, base_a_convertir)

        numero.upper()   # UPPERCASE
        print (" [",numero,"] EN BASE ", base_origen, " =  [",hexa,"] EN BASE ",base_a_convertir)
        print()

    elif base_a_convertir > 1 and base_a_convertir < 10:

        if base_origen >= 11:
            decimal = hexa_a_decimal(numero, base_origen)
            convertido = decimal_a_baseX(decimal, base_a_convertir)
        else:
            entero = string_a_entero(numero)
            decimal = baseX_a_b10(entero, base_origen)
            convertido = decimal_a_baseX(decimal, base_a_convertir)

        numero.upper()
        print (" [",numero,"] EN BASE ", base_origen, " =  [",convertido,"] EN BASE ",base_a_convertir)
        print()

    else: 
        print(" - 'ERROR 404 - 087' -\n")
        print()


def baseX_a_b10(numero_ingresado, base_origen):
    """ conversor de X base  a DECIMAL """
    posicion = 0
    decimal = 0
    negativo = False

    # Invertir la cadena porque debemos recorrerla de derecha a izquierda       

    if numero_ingresado < 0:
        negativo = True
        numero_ingresado *= -1   # si el num ingresado es negativo, lo convierte a positivo para poder operar

    numero_ingresado = str(numero_ingresado)[::-1]

    for digito in numero_ingresado:
        # Elevar X a la posición actual
        multiplicador = int(base_origen**posicion)
        decimal += int(digito) * multiplicador
        posicion += 1
    
    if negativo:
        return (decimal) * -1
    else:
        return decimal

def decimal_a_baseX(decimal_ingresado, base_a_convertir):    
        """ convertidor de base decimal a cualquier otra base """
        negativo = False
        
        if decimal_ingresado < 0:       
            negativo = True
            decimal_ingresado *= -1     # si el num ingresado es negativo, lo convierte a positivo para poder operar

        """ aqui almacenamos el resultado como cadena """
        cadena = ""

        """ mientras se pueda dividir... """
        while decimal_ingresado > 0:
            residuo = int(decimal_ingresado % base_a_convertir)    # el residuo es lo que se va almacenando (unos y ceros)
                        
            decimal_ingresado = int(decimal_ingresado / base_a_convertir)
            # va dividiendo el num ingresado para despues dividirlo y sacar el siguiente residuo
            cadena = str(residuo) + cadena
            resultado = int(cadena)

        if negativo:
            return (resultado) * -1
        else:
            return resultado


def decimal_a_hexa(decimal, base_a_convertir):
    """ funcion DECIMAL A HEXADECIMAL """
    equivalencias = {}
    negativo = False
    hex = ""

    # aca se crea el diccionario con los valores de ABC...
    for x in range(0, base_a_convertir - 10):
        equivalencias[ x + 10 ] = chr(ord('A') + x)

    if decimal < 0:
        negativo = True
        decimal *= -1
    
    while decimal > 0:
        residuo = decimal % base_a_convertir

        if residuo in equivalencias: 
            caracter_hex = equivalencias[residuo]
        else:
            caracter_hex = str(residuo)
        decimal = int(decimal / base_a_convertir)
        hex += caracter_hex

    if negativo:
        return "-" + hex   # str  
    else:
        return hex

def hexa_a_decimal(valor, base_origen):
    """ funcion como su nombre lo indica, hexadecimal a decimal
        fuente: https://www.geeksforgeeks.org/program-for-hexadecimal-to-decimal/
        """

    valor = valor.upper()
    negativo = if_hexa_is_negative(valor)

    length = len(valor)

    base = 1
    decimal = 0

    for x in range(length -1, -1, -1):
        if valor[x] >= '0' and valor[x] <= '9':
            decimal += (ord(valor[x]) -48) * base
        
            base = base * base_origen

        elif valor[x] >= 'A' and valor[x] <= 'F':
            decimal += (ord(valor[x]) -55) * base

            base = base * base_origen
            
    if negativo:
        return decimal * -1
    else:
        return decimal

def string_a_entero(cadena):
    """ funcion para quitar el caracter "-" del negativo de una CADENA de numeros y retornarlo como entero """
    negativo = if_hexa_is_negative(cadena)      # si la cadena ingresada tiene '-' o sea negativo

    if negativo:
        cadena = cadena.replace("-", "")        # quita el '-' y lo vuelve entero
        return int(cadena) * -1
    else:
        return int(cadena)

def if_hexa_is_negative(cadena):
    negativo = False
    for x in re.finditer("-", cadena):        # re.finditer (cadena o caracter a buscar, cadena en donde buscar)
        if x:                  
            negativo = True         # si en el FOR encuentra el caracter buscado retorna True y rompe el ciclo
            break
    return negativo






if __name__ == '__main__':
    we = hexa_a_decimal(valor= '-ff', base_origen=16)
    print(we)
    print(type(we))




"""
numero = "232"
base_origen = 16


print(string_a_entero(numero))  # (decimal, base_a_convertir)
print(type(string_a_entero(numero)))    """
