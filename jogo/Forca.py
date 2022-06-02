def jogar():
    import random

    print("****************************")
    print("Bem vindo ao jogo da Forca")
    print("****************************\n")


    print("Adivinhe a Fruta\n")

    #pegando as frutas dentro de palavras
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
    
    #Loop de tentativa
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
        print("Você Ganhou!")
    else:
        print("Você morreu!")
            


if(__name__ == "__main__"):
    jogar()