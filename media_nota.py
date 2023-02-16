import time

x = input("primeira nota: ")
print('Carregando...')
time.sleep(1)
y = input("segunda nota: ")
print('Carregando...')
time.sleep(1)
z = input("terceira nota: ")    
print('Carregando...')
time.sleep(1)

total1 = float(x)
total2 = float(y)
total3 = float(z)
    
def calculaMedia(n1, n2,n3):
    operacao = ((n1+n2+n3)/3)
    print (f"Media da sua prova deu:",operacao)
        
    if operacao < 7:
        print ('Reprovou! ')
    elif operacao > 10:
        print('Aprovado!')
    else:
        print('nota maxia!')
 
calculaMedia(total1,total2,total3)


