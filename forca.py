import random

def imprime_mensagem_perdedor(palavra_chave):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_chave))
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


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def joga_forca():


    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_chave = palavras[numero].upper()

    letras_acertada = []


    for letra in palavra_chave:
        letras_acertada.append("_")

    enforcou = False
    acertou = False
    erros = 0 
    
    print(letras_acertada)

    while(not enforcou and not acertou):

        print("Jogando ...")

        chute = input("Digite a palavra: ") 
        chute = chute.strip().upper()
        index = 0

        if(chute in palavra_chave):
            for letra in palavra_chave:
                if(chute == letra):
                    letras_acertada[index] = letra
                    print(letras_acertada)
                index = index + 1
        else:
            print(letras_acertada)
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_"  not in letras_acertada
        letras_faltando = str(letras_acertada.count("_"))
        print("\nAinda faltam acertar {} letras".format(letras_faltando))

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_chave)


    print("\nFim do jogo")

if(__name__ == "__main__"):
   joga_forca()

        