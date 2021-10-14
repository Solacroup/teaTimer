import re
from time import sleep

# proposer un choix à l'utilisateur
print("What kind of tea do you want to brew ? \n Black \n White \n Green \n Oolong \n Rooibos ")
# recueillir le choix de l'utilisateur
tea = input(": ")
# comparer l'entrée de l'utilisateur en ignorant les majuscules / minuscules
# l'utilisateur peut n'entrer que la première lettre du mot type de thé choisi
if re.search("^b(lack)?$", tea, re.IGNORECASE):
    # affichage du temps et de la température
    print("The temperature is 85°C and the brewing time 4 min")
    # boucle avec le temps d'infusion
    for i in range(240,0,-1):
        # affichage du temps d'infusion
        print(f"your tea has been brewing for {i} s")
        # seconde par seconde
        sleep(1)
        # quand le temps s'achève
        if i == 1:
            # on souhaite une bonne dégustation
            print("Enjoy your tea !")
elif re.search("^g(reen)?$", tea, re.IGNORECASE):
    print("The temperature is 75°C and the brewing time 3 min")
    for i in range(180, 0, -1):
        print(f"your tea has been brewing for {i} s")
        sleep(1)
        if i == 1:
            print("Enjoy your tea !")
elif re.search("^w(hite)?$", tea, re.IGNORECASE):
    print("The temperature is 85°C and the brewing time 7 min")
    for i in range(420, 0, -1):
        print(f"your tea has been brewing for {i} s")
        sleep(1)
        if i == 1:
            print("Enjoy your tea !")
elif re.search("^o(olong)?$", tea, re.IGNORECASE):
    print("The temperature is 85°C and the brewing time 5 min")
    for i in range(300, 0, -1):
        print(f"your tea has been brewing for {i} s")
        sleep(1)
        if i == 1:
            print("Enjoy your tea !")
elif re.search("^r(ooibos)?$", tea, re.IGNORECASE):
    print("The temperature is 95°C and the brewing time 6 min")
    for i in range(360, 0, -1):
        print(f"your tea has been brewing for {i} s")
        sleep(1)
        if i == 1:
            print("Enjoy your tea !")
