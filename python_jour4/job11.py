
total = int(input("veuillez entrez le nombre de minutes "))
heure = total // 60  
minutes = total % 60  


def heures_minutes():
    print(f" il y a {heure}  heures et {minutes} minutes")


heures_minutes()