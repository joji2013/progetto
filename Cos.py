scor=0
import random
for i in range(10):
    scelta =input ("cosa scegli? ")
    bot=random.randint(1,3)
    if bot == 1:
        print("carta")
    elif bot == 2:
        print("forbici")
    elif bot == 3:
        print("sasso")
    if scelta == "carta" and bot == 3:
        print("hai vinto")
        scor=scor+1
    elif scelta =="forbici"and bot ==1:
        print ("hai vinto")
        scor=scor+1
    elif scelta =="sasso"and bot ==2:
        print ("hai vinto")
        scor=scor+1
    elif scelta =="forbici"and bot ==3:
        print ("hai perso")
    elif scelta =="sasso"and bot ==1:
        print ("hai perso")
    elif scelta =="carta"and bot ==2:
        print ("hai perso")
    else:
        print ("parola inesistente hai perso")

print(scor)
