import random
import time

last = False
lastlast = False


def main(age):
    global last, lastlast

    if age == "1":
        mainRandInt = random.randint(0, 14)
        cont = lines[mainRandInt].replace(":", " ").lower().split()
        randInt = random.randint(1, 3)
    elif age == "2":
        mainRandInt = random.randint(15, len(lines) - 1)
        cont = lines[mainRandInt].replace(":", " ").lower().split()
        randInt = random.randint(1, 3)
    else:
        mainRandInt = random.randint(0, len(lines) - 1)
        cont = lines[mainRandInt].replace(":", " ").lower().split()
        randInt = random.randint(1, 3)               

    if mainRandInt == last or mainRandInt == lastlast:
        mainRandInt += 1
        if mainRandInt == lastlast or mainRandInt == last:                                      
            mainRandInt += 1

    if randInt == 1:
        print("Autor: ??? Narodnost:", cont[1], "Dilo:", cont[2].replace("/", " "), "Dej:", cont[3].replace("/", " "))
        odpoved = input()
        if odpoved == str(cont[0].replace("/", " ").lower()):
            print("spravne")
        else:
            print("špatně:", str(cont[0].replace("/", " ").lower()))
    elif randInt == 2:
        print("Autor:", cont[0].replace("/", " "), "Narodnost:", cont[1], "Dilo: ???", "Dej:", cont[3].replace("/", " "))
        odpoved = input()
        if odpoved == str(cont[2].replace("/", " ")):
            print("spravne")
        else:
            print("špatně:", str(cont[2].replace("/", " ")))
    elif randInt == 3:
        print("Autor:", cont[0].replace("/", " "), "Narodnost:", cont[1], "Dilo:", cont[2].replace("/", " "), "Dej: ???")
        odpoved = input()
        if odpoved:
            print(str(cont[3].replace("/", " ")))

    lastlast = last
    last = mainRandInt
    return last, lastlast

 



def hardMain(age):
    global last, lastlast

    if age == "1":
        mainRandInt = random.randint(0, 14)
        cont = lines[mainRandInt].replace(":", " ").lower().split()
        randInt = random.randint(1, 3)
    elif age == "2":
        mainRandInt = random.randint(15, len(lines) - 1)
        cont = lines[mainRandInt].replace(":", " ").lower().split()
        randInt = random.randint(1, 3)
    else:
        mainRandInt = random.randint(0, len(lines) - 1)
        cont = lines[mainRandInt].replace(":", " ").lower().split()
        randInt = random.randint(1, 3)

    if mainRandInt == last or mainRandInt == lastlast:
        mainRandInt += 1
        if mainRandInt == lastlast or mainRandInt == last:                                      
            mainRandInt += 1

    if randInt == 1:
        print("Autor: ??? Narodnost: ??? Dilo: ??? Dej:", cont[3].replace("/", " "))
        odpoved1 = input("Autor: ")
        odpoved2 = input("Narodnost: ")
        odpoved3 = input("Dilo: ")
        if odpoved1 == str(cont[0].replace("/", " ")) and odpoved2 == str([1]) and odpoved3 == str(cont[2].replace("/", " ")):
            print("spravne")
        else:
            print("špatně:", cont[0].replace("/", " "), cont[1], cont[2].replace("/", " "), cont[3].replace("/", " "))
    elif randInt == 2:
        print("Autor: ??? Narodnost: ??? Dilo:", cont[2].replace("/", " "), "Dej: ???")
        odpoved4 = input("Autor: ")
        odpoved5 = input("Narodnost: ")
        odpoved6 = input("Dej: ")
        if odpoved4 == str(cont[0].replace("/", " ")) and odpoved5 == str(cont[1]) and odpoved6:
            print(cont[3].replace("/", " "))
            time.sleep(1)
            print("spravne")
        else:
            print("špatně:", cont[0].replace("/", " "), cont[1], cont[2].replace("/", " "), cont[3].replace("/", " "))
    elif randInt == 3:
        print("Autor:", cont[0].replace("/", " "), "Narodnost: ??? Dilo: ??? Dej: ???")
        odpoved7 = input("Narodnost: ")
        odpoved8 = input("Dilo: ")
        odpoved9 = input("Dej: ")
        if odpoved7 == str(cont[1]) and odpoved8 == str(cont[2].replace("/", " ")) and odpoved9:
            print(cont[3].replace("/", " "))
            time.sleep(1)
            print("spravne")
        else:
            print("špatně:", cont[0].replace("/", " "), cont[1], cont[2].replace("/", " "), cont[3].replace("/", " "))

    lastlast = last
    last = mainRandInt
    return last, lastlast



def pololetka():
    global last, lastlast

    with open("C:/Users/evapr/Desktop/libraries/polo.txt", 'r') as file:
        lines = file.readlines()

    mainRandInt = random.randint(0, len(lines))

    if mainRandInt == 21 or mainRandInt == 23 or mainRandInt == 25:
        mainRandInt = mainRandInt - 1
    if mainRandInt == 20 or mainRandInt == 22 or mainRandInt == 24:
        cont = lines[mainRandInt].replace(":", " ").replace("/", " ").lower().split()
        cont2 = lines[mainRandInt + 1].replace(":", " ").replace("/", " ").lower().split()
        joinedStr = " ".join(cont)
        joinedStr2 = " ".join(cont2)
    else:
        cont = lines[mainRandInt].replace(":", " ").lower().split()
    randInt = random.randint(1, 3)

    if mainRandInt == last or mainRandInt == lastlast:
        mainRandInt += 1
        if mainRandInt == lastlast or mainRandInt == last:                                      
            mainRandInt += 1

    if mainRandInt <= 19:
        if randInt == 1:
            print("Autor: ??? Narodnost: ??? Dilo: ??? Dej:", cont[3].replace("/", " "))
            odpoved1 = input("Autor: ")
            odpoved2 = input("Narodnost: ")
            odpoved3 = input("Dilo: ")
            if odpoved1 == str(cont[0].replace("/", " ")) and odpoved2 == str([1]) and odpoved3 == str(cont[2].replace("/", " ")):
                print("spravne")
            else:
                print("špatně:", cont[0].replace("/", " "), cont[1], cont[2].replace("/", " "), cont[3].replace("/", " "))
        elif randInt == 2:
            print("Autor: ??? Narodnost: ??? Dilo:", cont[2].replace("/", " "), "Dej: ???")
            odpoved4 = input("Autor: ")
            odpoved5 = input("Narodnost: ")
            odpoved6 = input("Dej: ")
            if odpoved4 == str(cont[0].replace("/", " ")) and odpoved5 == str(cont[1]) and odpoved6:
                print(cont[3].replace("/", " "))
                time.sleep(1)
                print("spravne")
            else:
                print("špatně:", cont[0].replace("/", " "), cont[1], cont[2].replace("/", " "), cont[3].replace("/", " "))
        elif randInt == 3:
            print("Autor:", cont[0].replace("/", " "), "Narodnost: ??? Dilo: ??? Dej: ???")
            odpoved7 = input("Narodnost: ")
            odpoved8 = input("Dilo: ")
            odpoved9 = input("Dej: ")
            if odpoved7 == str(cont[1]) and odpoved8 == str(cont[2].replace("/", " ")) and odpoved9:
                print(cont[3].replace("/", " "))
                time.sleep(1)
                print("spravne")
            else:
                print("špatně:", cont[0].replace("/", " "), cont[1], cont[2].replace("/", " "), cont[3].replace("/", " "))

    elif mainRandInt == 20 or mainRandInt == 22 or mainRandInt == 24:
        points = 0
        print(joinedStr)
        time.sleep(1)
        print(joinedStr2)
        poloodpoved1 = input("prvni: ")
        poloodpoved2 = input("druhy: ")
        poloodpoved3 = input("treti: ")
        poloodpoved4 = input("ctvrty: ")

        if mainRandInt == 20:
            if poloodpoved1 == "1":
                points += 1
            if poloodpoved2 == "2":
                points += 1
            if poloodpoved3 == "4":
                points += 1
            if  poloodpoved4 == "6":
                points += 1
            if points == 4:
                print("spravne")
            else:
                print("spatne. pocet spracnych odpovedy -", points)
        elif mainRandInt == 22:
            if poloodpoved1 == "2":
                points += 1
            if poloodpoved2 == "3":
                points += 1
            if poloodpoved3 == "7":
                points += 1
            if  poloodpoved4 == "8":
                points += 1
            if points == 4:
                print("spravne")
            else:
                print("spatne. pocet spracnych odpovedy -", points)
        elif mainRandInt == 24:
            if poloodpoved1 == "3":
                points += 1
            if poloodpoved2 == "4":
                points += 1
            if poloodpoved3 == "5":
                points += 1
            if  poloodpoved4 == "7":
                points += 1
            if points == 4:
                print("spravne")
            else:
                print("spatne. pocet spracnych odpovedy -", points)

    elif mainRandInt > 24:
        print(cont[0].replace("/", " "))
        respuenta = input()
        if mainRandInt % 2 == 1:
            if respuenta.lower() == "ano":
                print("spravne")
            else:
                print("spatne - je to pravda")
        elif mainRandInt % 2 == 0:
            if respuenta.lower() == "ne":
                print("spravne")
            else:
                print("spatne - ", cont[1].replace("/", " "))
            

    lastlast = last
    last = mainRandInt
    return last, lastlast



        
def poloLoop():
    while True:
        time.sleep(0.5)
        odpoved = input("další otázka? (y/n)")
        if odpoved == "y":
            last, lastlast = pololetka()
        elif odpoved == "n":
            break
        else:
            print("špatně zadaná odpověď")


mode = False
x = 0
print("vyberte obdobi: pololetka - 0, renesance - 1, baroko - 2, vsechno - 3")
antwort = input()
if antwort != "0" and antwort != "1" and antwort != "2" and antwort != "3":
    print("špatně zadaná odpoveď - automaticky přepnuto na možnost 3")
    antwort = 3

with open("C:/Users/evapr/Desktop/libraries/renesance.txt", 'r') as file:
    lines = file.readlines()
    if antwort != "0":
        print("vyberte obtiznost: (lehka/ tezka)")
        answer = input()
    if antwort == "0":
        x = 1
        pololetka()
        poloLoop()
    elif answer == "lehka":
        mode = 1
        main(antwort)
    elif answer == "tezka":
        mode = 2
        hardMain(antwort)
    else:
        print("error - špatně zadaná odpověď. automaticky vybrana lehka obtiznost")
        mode = 1
        time.sleep(2)
        main(antwort)



while True:
    if x == 1:
        break
    time.sleep(0.5)
    odpoved = input("další otázka? (y/n)")
    if odpoved == "y" and mode == 1:
       last, lastlast = main(antwort)
    elif odpoved == "y" and mode == 2:
        last, lastlast = hardMain(antwort)
    elif odpoved == "n":
        break
    else:
        print("špatně zadaná odpověď")