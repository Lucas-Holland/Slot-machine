import random
from time import sleep

items = ["\033[35m♬\033[m",
         "\033[33m☺\033[m",
         "\033[34m☎\033[m",
         "\033[36m☂\033[m",
         "\033[31m♥\033[m",
         "\033[32m$\033[m"]

IA = []
IB = []
IC = []
ID = []
IE = []
IF = []
escolhaa = []


def porcentagemA (letra, x):
    while len(IA) < x:
        IA.append("♬")


def porcentagemB (letra, x):
    while len(IB) < x:
        IB.append("☺")


def porcentagemC (letra, x):
    while len(IC) < x:
        IC.append("☎")


def porcentagemD(letra, x):
    while len(ID) < x:
        ID.append("☂")


def porcentagemE (letra, x):
    while len(IE) < x:
        IE.append("♥")

def porcentagemF (letra, x):
    while len(IF) < x:
        IF.append("$")


    # PORCENTAGEM // QUANTO MAIOR > MAIS FACIL

porcentagemA(IA, 4)
porcentagemB(IB, 6)
porcentagemC(IC, 8)
porcentagemD(ID, 10)
porcentagemE(IE, 15)
porcentagemF(IF, 20)


    # UNI AS LETRAS SEM ESPACOS PARA FAZER A ESCOLHA

def uni(letra):
    for i in letra:
        escolhaa.append(i)


uni(IA)
uni(IB)
uni(IC)
uni(ID)
uni(IE)
uni(IF)

#CARTEIRA
cash = 0
dinheiro = 1200
aposta1000 = 1000
aposta100 = 100
aposta50 = 50

anteriorwins = 0
total_wins = 0
loses = 0
total_loses = 0


# MENSAGEM INICIAL

print("     \033[35m$ \033[31m$ \033[33m$ \033[34mMÁQUINA CAÇA-NÍQUEL \033[32m$ \033[31m$ \033[34m$\033[m\n")
count = 0


# INICIA O PROGRAMA

while True:
    continuar = input(" > Deseja Jogar? R: ").upper()
    if continuar in "AHAMSIMMCLAROQUEROBORAUHUM":
        while True:
            esc_aposta = input("\033[31mAPOSTAR 1000 [\033[m0\033[31m]   "
                               "\033[32mAPOSTAR  100 [\033[m1\033[32m]\033[m   "
                               "\033[33mAPOSTAR  10 [\033[m2\033[33m]\033[m   "
                               "\033[34mALL IN [\033[m3\033[34m]\033[m\n"
                               " > ")
            if esc_aposta == "3":
                break
            if esc_aposta == "0" and dinheiro >= 1000:
                dinheiro -= 1000
                break
            if esc_aposta == "1" and dinheiro >= 100:
                dinheiro -= 100
                break
            if esc_aposta == "2" and dinheiro >= 10:
                dinheiro -= 10
                break
            else:
                print("Erro. Moedas:", dinheiro)
        count += 1
        c = 0
        final = []

        print(escolhaa)

        # ADICIONA ITENS PARA AUMENTAR AS CHANCES DE VITORIA

        if loses > 4 and loses <= 8:
            porcentagemD(ID, 10)
            porcentagemE(IE, 15)
            uni(ID)
            uni(IE)


        # RETIRA ITENS PARA COMO NO INICIO

        if loses > 8:
            porcentagemE(IE, 20)
            uni(IE)


        # SORTEIA OS ITENS:

        while c < 3:
            p = random.choice(escolhaa)
            if c == 0:
                final.append(p)

            if c == 1 and p != final[0]:
                final.append(p)

            if c == 1 and p == final[0]:
                final.append(p)

            if c == 2 and p != final[1]:
                final.append(p)

            if c == 2 and p == final[1]:
                final.append(p)

            c += 1

        print("")
        print("        CAÇA-NÍQUEL")
        print("          ", end=" ")
        sleep(1)
        for i in final:
            if i == "♬":
                print('\033[35m♬\033[m', end=" ")
                sleep(1)
            if i == "☺":
                print('\033[33m☺\033[m', end=" ")
                sleep(1)
            if i == "☎":
                print('\033[34m☎\033[m', end=" ")
                sleep(1)
            if i == "☂":
                print('\033[36m☂\033[m', end=" ")
                sleep(1)
            if i == "♥":
                print('\033[31m♥\033[m', end=" ")
                sleep(1)
            if i == "$":
                print('\033[32m$\033[m', end=" ")
                sleep(1)

        print("\n")
        i = 0

        if esc_aposta == "0":
            a = 1000
        if esc_aposta == "1":
            a = 100
        if esc_aposta == "2":
            a = 10
        if esc_aposta == "3":
            a = dinheiro
            dinheiro -= dinheiro
        while True:
            while i < len(final):
                if final[i] == "$":
                    dinheiro += a * 10
                i += 1
            if final[0] == final[1] and final[1] == final[2]:
                print("\033[32m            WINNER\033[m")

                anteriorwins = total_wins
                if anteriorwins == total_wins and count > 5:
                    escolhaa.clear()
                    porcentagemA(IA, 4)
                    porcentagemB(IB, 6)
                    porcentagemC(IC, 8)
                    porcentagemD(ID, 10)
                    porcentagemE(IE, 15)
                    porcentagemF(IF, 2)
                    uni(IA)
                    uni(IB)
                    uni(IC)
                    uni(ID)
                    uni(IE)
                    uni(IF)

                total_wins += 1
                loses = 0
                if total_loses <= 1 and total_loses != 0:
                    print("Voce perdeu, ", total_loses, " vez.")
                else:
                    print("Voce perdeu, ", total_loses, " vezes.")
                print("Perdas seguidas: ", loses)
                if total_wins <= 1:
                    print("Voce venceu, ", total_wins, " vez.")
                else:
                    print("Voce venceu, ", total_wins, " vezes.")

                if final[0] == "♬":
                    dinheiro += (a * 50)
                if final[0] == "☺":
                    dinheiro += (a * 20)
                if final[0] == "☎":
                    dinheiro += (a * 10)
                if final[0] == "☂":
                    dinheiro += (a * 5)
                if final[0] == "♥":
                    dinheiro += (a * 2)
                break
            elif final[0] == "$" or final[1] == "$" or final[2] == "$":
                print("\033[32m           WINNER\033[m")

                anteriorwins = total_wins
                if anteriorwins == total_wins and count > 5:
                    escolhaa.clear()
                    porcentagemA(IA, 4)
                    porcentagemB(IB, 6)
                    porcentagemC(IC, 8)
                    porcentagemD(ID, 10)
                    porcentagemE(IE, 15)
                    porcentagemF(IF, 2)
                    uni(IA)
                    uni(IB)
                    uni(IC)
                    uni(ID)
                    uni(IE)
                    uni(IF)

                total_wins += 1
                loses = 0
                if total_loses <= 1 and total_loses != 0:
                    print("Voce perdeu, ", total_loses, " vez.")
                else:
                    print("Voce perdeu, ", total_loses, " vezes.")
                print("Perdas seguidas: ", loses)
                if total_wins <= 1:
                    print("Voce venceu, ", total_wins, " vez.")
                else:
                    print("Voce venceu, ", total_wins, " vezes.")
                break
            else:
                print("\033[31m          LOSER\033[m")

                loses += 1
                total_loses += 1
                if total_loses <= 1 and total_loses != 0:
                    print("Voce perdeu, ", total_loses, " vez.")
                else:
                    print("Voce perdeu, ", total_loses, " vezes.")
                print("Perdas seguidas: ", loses)
                if total_wins <= 1:
                    print("Voce venceu, ", total_wins, " vez.")
                else:
                    print("Voce venceu, ", total_wins, " vezes.")
                break

        if dinheiro <= 9:
            print("\nSuas moedas acabaram!")
            print("\nObrigado por jogar!")
            break
    else:
        print("OK. Muito obrigado!")
        break
    print("\n"
          " Sua carteira ainda contém ", dinheiro, "moedas.")




