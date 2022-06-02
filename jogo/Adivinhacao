def jogar():
    import random

    print("****************************")
    print("Bem vindo ao jogo de adivinhação")
    print("****************************")


    numero_secreto = random.randrange(1,11)
    total_de_tentativas = 0
    rodada = 1
    pontos = 10

    print("Qual  nível de dificilpade")
    print("(1)Fácil (2)Médio (3)Difícil")


    nivel = int(input("Define um nível: "))
    
    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3


    while(rodada <= total_de_tentativas):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        chute_acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto
        if(chute_acertou):
            print("Você acertou!")
            break
        else:
            if(chute_maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(chute_menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos -= 1
        rodada += 1

    print("Total de pontos: {}".format(pontos))

if(__name__ == "__main__"):
    jogar()