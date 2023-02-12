# Problem: https://www.hackerrank.com/challenges/staircase/problem
# Sua base e altura são iguais a N. Ele é desenhado usando #símbolos e espaços. A última linha não é precedida de espaços.
# Escreva um programa que imprima uma escada de tamanho N.
# Ex: N = 4:
#    #
#   ##
#  ###
# ####

def staircase(n):
    staircase = ""

    for index in range(n):
        if (index > 0):
            staircase += "\n"

        for aux in range(n):
            if (aux + 1 >= n - index):
                staircase += "#"
            else:
                staircase += " "

    return staircase
