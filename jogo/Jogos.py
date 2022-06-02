import Forca
import Adivinhacao

def escolhe_jogo():
    print("****************************")
    print("Escolhe o seu jogo")
    print("****************************")


    print("(1) Forca  (2)Adivinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogo da Forca")
        Forca.jogar()
    elif(jogo == 2):
        print("Jogo de Adivinhação")
        Adivinhacao.jogar()

    print("Fim do jogo")

if(__name__ == "__main__"):
    escolhe_jogo()