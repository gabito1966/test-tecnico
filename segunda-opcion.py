'''
    puedeFormarSuma en el nombre de la funcion para verificar si se puede
    formar un numero especifico mediante la suma de 2 elementos de nuestro
    array
    '''

def puedeFormarSuma(nums, required_sum):
    '''
    recibe 2 argumentos, nums que son los numeros enteros que estan dentro del
    array y required_sum que es el numero requerido que queremos formar
    '''

    vistos = set()
    #Se utiliza el conjunto vistos para almacenar los numeros leidos

    for number in nums:
        #iteracion de cada numero en nums

        complement = required_sum - number
        '''
        calculo del complemento, para cada numero se hace la resta entre
        el numero requerido y el numero leido
        '''

        if complement in vistos:
            '''
            Se hace la verificacion de si el numero complementario está
            incluido dentro de los numeros vistos
            '''

            return True
            #Si el numero complementario esta incluido nos retorna True
            

        vistos.add(number)
        # Se agrega el numero a los numeros vistos
    return False
    # Si el numero complementario no esta incluido nos retorna False


#Ejemplo 1
nums1 = [1, 4, 3, 9]
required_sum1 = 8
print(puedeFormarSuma(nums1, required_sum1))  # Salida: False

#Ejemplo 2
nums2 = [1, 2, 4, 4]
required_sum2 = 8
print(puedeFormarSuma(nums2, required_sum2))  # Salida: True