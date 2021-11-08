#Ejercicio 5 ENTREGAR
def Buscar_valor_letra_romana(Letra_Romano):
    Valor = 0

    if Letra_Romano == 'M':
        Valor = 1000
    elif Letra_Romano == 'D':
        Valor = 500
    elif Letra_Romano == 'C':
        Valor = 100
    elif Letra_Romano == 'L':
        Valor = 50
    elif Letra_Romano == 'X':
        Valor = 10
    elif Letra_Romano == 'V':
        Valor = 5
    elif Letra_Romano == 'I':
        Valor = 1

    return Valor

def Convert_de_numero_romano_a_numeros_normales(Cadena_Romano):
    Val_letra_1 = 0
    Val_letra_2 = 0
    indice = 2

    if(len(Cadena_Romano) == 0):
        return Val_letra_1
    else:
        Val_letra_1 = Buscar_valor_letra_romana(Cadena_Romano[-1])

        if(len(Cadena_Romano) > 1):
            Val_letra_2 = Buscar_valor_letra_romana(Cadena_Romano[-2])
        else:
            indice = 1

        if(Val_letra_1 > Val_letra_2):
            Val_letra_1 -= Val_letra_2
        else:
            Val_letra_1 += Val_letra_2
        
        return Val_letra_1 + Convert_de_numero_romano_a_numeros_normales(Cadena_Romano[:-indice])
        
#Ejercicio 8 ENTREGAR
def Numero_decimal_a_binario(Numero_decimal):
    if((Numero_decimal == 0) or (Numero_decimal == 1)):
        return str(Numero_decimal)
    else:
        return Numero_decimal_a_binario((Numero_decimal//2)) + str(Numero_decimal%2)

#Ejercicio 22 ENTREGAR
def Prob_Mochila_Jedi(mochila):

    if ((len(mochila) == 0) or (mochila[-1] == 'Sable')):
        return len(mochila)
    else:
        return Prob_Mochila_Jedi(mochila[:-1])

def problema_jedi():
    mochilajedi = ['algo', 'algo', 'algo', 'algo', 'algo', 'algo']
    mochilajedi2 = ['algo', 'algo', 'algo', 'algo', 'algo', 'Sable']
    mochilajedi3 = ['algo', 'Sable', 'algo', 'algo', 'algo', 'algo']
    mochilajedi4 = ['Sable', 'algo', 'algo', 'algo', 'algo', 'algo']

    pos_sable = Prob_Mochila_Jedi(mochilajedi)

    if(pos_sable == 0):
        print('El sable no esta en la mochila')
    else:
        print('El sable esta en la mochila', '\n Objetos Sacados: ', len(mochilajedi) - pos_sable)


