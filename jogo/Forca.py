import random

def jogar():  

    print("****************************")
    print("Bem vindo ao jogo da Forca")
    print("****************************\n")


    print("Adivinhe a Fruta\n")
    
    #add chamada de arquivo
    arquivo = open(r"C:\Users\vinic\Documents\MeusProjetos\Jogo-em-Python\jogo\palavras.txt","r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    
    #add aleatoriedade na chamada
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    #add "_" para cada caracter da fruta
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    enforcou = False
    acertou = False
    erros = 0


    print(letras_acertadas)
    
    #loop de tentativas
    while(not enforcou and not acertou):

            chute = input("Qual letra?")
            chute = chute.strip().upper()
            
            if(chute in palavra_secreta):
    
                index = 0
                for letra in palavra_secreta:
                    if(chute == letra):
                        letras_acertadas[index] = letra
                    index += 1
            else:
                erros += 1 
            enforcou = erros == 6
            acertou = "_" not in letras_acertadas
            print(letras_acertadas)

    if(acertou):
        print(imprime_mensagem_vencedor)
    else:
        print(imprime_mensagem_perdedor)
            


if(__name__ == "__main__"):
    jogar()

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")