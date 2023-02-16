import random


def numero():
    value = random.randint(0, 100)
    
    r = int(input("Qual o seu chute de 0 a 100? "))
    maior_menor(r,value)
    while r != value:
        r = int(input("Chute novamente de 0 a 100? "))
        maior_menor(r,value)
        
def maior_menor(r,value):
    if value > r:
        print("O numero é maior!")
    elif value < r:
        print("O numero é menor!")
    elif r == value:
        print("Correto!!!")
        
def final():
    ccc = True
    while ccc == True:
        print("-="*10)
        bbb = input("Voce gostaria de joga novamente? [Y] [N]")
        if bbb == "y" or "Y":
            numero()
        else:
            print("Obrigado por jogar!!")
            ccc = False
numero()
final()
