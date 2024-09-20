#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

def verificar_senha(password):
    upperChars, lowerChars, specialChars, digits, length = 0,0,0,0,0
    length = len(password)

#Verifica se a sennha possui menos de seis digitos

    if (length < 6): 
        print('A senha é cruta. Sua senha deve conter mais de 6 digitos')   #caso o tamanho seja valido, cairá na validação de Letra Maiuscula, Numeros e Caractere especial
    else:
        for i in range(0, length):
            if(password[i].isupper()):
                upperChars += 1
            elif(password[i].isnumeric()):
                digits += 1
            elif (password[i].islower()):
                lowerChars += 1
            else:
                specialChars += 1
                
    if (upperChars!= 0 and lowerChars != 0 and digits != 0 and specialChars != 0):
        if(length >= 10):
            print('Força de Senha Forte')
        else:
            print('Força de senha média')
    
    
    #Erros de senha e mensagens atribuidas a cada tipo de problema
    
    if(upperChars == 0):
        print('Senha Fraca! Sua senha deve conter no minimo uma letra maiuscula.')
    if(lowerChars == 0):
        print('Senha Fraca! Sua senha deve conter no minimo uma letra minuscula.')
    if(specialChars == 0):
        print('Senha Fraca! Sua senha deve conter no minimo um caractere especial')
    if(digits == 0):
        print('Senha Fraca! Sua senha deve conter no minimo um numero')

password = input('Digite sua nova senha: ')
verificar_senha(password)


