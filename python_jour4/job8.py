Type =  "fruits"
Saison = "hiver"


def TS():
    if Type == "fruits" and Saison == "hiver":
        print("orange, mandarine et kiwi")
    elif Type == "fruit" and Saison == "été":
        print("Poire, fraise, cassis")
    elif Type == "légume" and Saison == "hiver":
        print("carotte, topinambour, endive")
    elif Type == "légume" and Saison == "été":
        print("artichaut, aubergine,navet")

TS()

Type = "légume"

TS()

Saison = "été"

TS()

Type = "fruit"

TS()