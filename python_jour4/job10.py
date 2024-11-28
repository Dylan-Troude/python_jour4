a = int(input("écrivez un chiffre: "))

def pair():
    if a % 2 == 0 and a >= 0:
        print("c'est un nombre paire")
    elif a % 2 != 0 and a >= 0:
        print("ce n'est pas un nombre paire")
    else:
        print("ce n'est pas un nombre positif")

pair()