import random
def joga_adivinhacao():
    print("**********************************")
    print("*Bem vindo ao jogo de adivinhação*")
    print("**********************************")

    numero_secreto = random.randrange(1,101)

    chute = 0
    nivel = int(input("Digite o qual dificuldade deseja 1-facil/2-medio/3-Dificil: "))
    total_tentativas = 0
    pontos = 1000

    if(nivel == 1):
        total_tentativas = 9
    elif(nivel == 2):
        total_tentativas= 6
    elif(nivel == 3):
        total_tentativas = 3
    for rodada in range(1,total_tentativas + 1):
        print("rodada {}".format(rodada))
        print("Voce tem um total de {}".format(pontos))
        chute = int(input("Digite o numero que deseja chuta: "))
        if(numero_secreto == chute):
            print("O chute foi certo!")
            print("voce ganhou {} pontos !!".format(pontos))
            break
        else:
            if(numero_secreto > chute):
                print("O chute foi incorreto!!")
                print("O numero e maior que o chute!")

            else:
                print("O chute foi incorreto!!")
                print("O numero e menor que o chute!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim do jogo!")

if(__name__ == "__main__"):
    joga_adivinhacao()