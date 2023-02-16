from random import randint

itens = ("Pedra","Papel","Tesoura")
computador = randint(0,2)

print("""Suas proximas jogados:
[0] Pedra
[1] Papel
[2] Tesoura""")

jogada = int(input("Qual sera sua opiçao: "))
print("-=" * 11)

if jogada < 3:
    print(f"Jogada do computador: {itens[computador]} ")
    print(f"Sua jogada: {itens[jogada]}")
    print("-" * 5)
    
    if computador == 0:
        if jogada == 0:
            print ("Empate!")
             
        elif jogada == 1:
            print("Jogador ganhou!!")
             
        elif jogada == 2:
            print("Jogador perdeu!!")
             
        else:
            print("jogada invalida!!!")
            
    
    elif computador == 1:
        if jogada == 0:
            print("Jogador perdeu!!")
             
        elif jogada == 1:
            print("Empate!")
             
        elif jogada == 2:
            print("Jogador ganhou!!!")
             
        else:
            print("jogada invalida!!!")
            
    
    elif computador == 2:
        if jogada == 0:
            print("Jogador ganhou!!")
             
        elif jogada == 1:
            print("Jogador perdeu!!")
             
        elif jogada == 2:
            print("Empate!!!")
             
        else:
            ("Jogada invalida!!!")
            
    else:
        print("jogada invalida!!!!")

else:
    print("Jogada invalida!!!")

    print("-=" * 11)
    print("GG, WP espero poder jogar com voce novamente!!")
    pass


