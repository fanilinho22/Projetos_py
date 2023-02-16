

numerosFodas = []
def Numeros(n1,n2,n3):
    result1 = n3
    result2 = n1 * n2 
    resultF = result2/result1
    numerosFodas.append(resultF)
    print('X é : ',resultF)
    
def  Num1():
    return print('x   N1 <--- \n- = -\nN2   N3')
    
def Num2():
    return print('x   N1\n- = -\nN2<--   N3')
    
def Num3():
    return print('x   N1\n- = -\nN2   N3 <---')
    
Num1()
N1 = int(input('primeiro:'))
numerosFodas.append(N1)
Num2()
N2 = int(input('segundo:'))
numerosFodas.append(N2)
Num3()
N3 = int(input('terceiro:'))
numerosFodas.append(N3)

Numeros(N1,N2,N3)
print(numerosFodas)

