import adivinhacao
import forca
def escolhe_jogo():
    print("Qual jogo deseja joga?")
    print("1 - adivinhacao  //  2 - forca")

    jogo = int(input("Digite o jogo que deseja: "))

    if(jogo == 1):
        print("Inicializando adivinhacao")
        adivinhacao.joga_adivinhacao()
    elif(jogo == 2):
        print("Inicializando forca")
        forca.joga_forca()

if(__name__== "__main__"):
    escolhe_jogo()
