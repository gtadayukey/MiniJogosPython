import random
from time import sleep

# Jogo da Forca
print("\n\n")
print("<<< Bem-Vindo a Forca do Gui >>>\n")

while True:
    
    # Interface 
    
    sleep(1)

    print("Escolha a dificuldade")
    
    sleep(1)
    
    print("1 -> Facil:")
    print("2 -> Medio:")
    print("3 -> Dificil")
    
    sleep(1)
    
    escolha = input("Escolha: ")
    print("\n\n\n\n")
    
    # Array das palavras
    
    facil = ["carro","vento","vinte","lento","latas","cesta","jegue"]
    medio = ["escolas","sentado","frustar","bananas","veiculo","vestido","amizade"]
    dificil = ["escolaridade","posteriormente","estruturados","intencionalmente","vestimentas","pragmatismo","faturamento"]
    
    nSorteado = random.randint(0,6)
    
    # Definindo Difilcudade e Palavra Sorteada
    
    if escolha == "1":
        vidas = 7
        palavra = facil[nSorteado]
        
    elif escolha == "2":
        vidas = 5
        palavra = medio[nSorteado]
        
    elif escolha == "3":
        vidas = 3
        palavra = dificil[nSorteado]
        
    else:
        print("Caracter Digitado Invalido.")
        print("\n\n\n\n")
        continue
        
    # Jogo    
    sleep(0.5)
        
    print("Iniciando Jogo..\n\n")
        
    sleep(2)
        
    letras = []
        
    while True:
        if vidas <= 0:
            print(f'Você Perdeu!! A palavra era {palavra}\n\n\n')
            break
        
        letraBase = input("Digite uma letra: ")
        
        if len(letraBase) > 1:
            print("Isso não vale !! Digite apenas uma letra.\n\n") 
            
            sleep(0.5)
            
            continue
            
        if letraBase in letras:
            print("Essa letra ja foi escolhida!\n\n")
            
            sleep(0.5)
            
            continue
            
        letras.append(letraBase)
            
        if letraBase in palavra:
            sleep(0.5)
            print(f'A letra "{letraBase}" EXISTE na palavra oculta :)')
        else:
            sleep(0.5)
            print(f'A letra "{letraBase}" NÃO EXISTE na palavra oculta :(')
            vidas -= 1
            
        ocultoTemporario = ""
        
        for letraOculta in palavra:
            if letraOculta in letras:
                ocultoTemporario += letraOculta
            else:
                ocultoTemporario += " _ "
        
        sleep(0.5)
        
        if ocultoTemporario == palavra:
            print(f'\n\n\nA palavra era {ocultoTemporario}')
            print("Você Venceu o Jogo!!\n\n\n")
            break
        else:
            print(f'\n{ocultoTemporario}\n') 
            print(f'Você ainda tem {vidas} vidas\n\n')
            
    # Rerun
    
    sleep(2)
    
    print("Deseja jogar novamente?")
    print("1 -> sim")
    print("2 -> não")
    rerun = input("Escolha: ")
       
    if rerun == "1":
        print("Programa Reiniciando.\n\n\n\n")
        pass
    else:
        print("Programa Finalizado.\n\n\n\n")
        break