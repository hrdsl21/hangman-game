import random

#lista haseł
lista = ['góra', 'koń', 'dom', 'pies', 'Arek']

#liczba żyć
lifs = 6 
#generator hasła
random_password = random.choice(lista)
list_gen = list(random_password)


print("Rozpoczynasz gre w wisielca")

#Generator _____
for i in range(len(random_password)):
    list_gen[i] = "_"


while lifs > 0:
    print(f"Pozostało ci {lifs} zyc ")
    print("")
    print(f"hasło : {list_gen}")
    print("")

    answer = input("Podaj pierwsza liter dla słowa z listy ")
    if answer in random_password:
        #sprawdzamy czy i podmieniamy znaki na _
        for i in range(len(random_password)):
            if (random_password[i]) == answer:
                list_gen[i] = answer
                print(list_gen)
            #sprawdzenie czy wygrałes   
            if list_gen == list(random_password):
                print("")
                print(f"Pozostało ci {lifs} zyc ")
                print("")
                print(f"hasło :  {random_password}")
                print("")
                print('wygrywasz')
                exit()
    else:
        lifs -= 1 
        if lifs == 0:
            print('Teraz oddasz życie na szubienicy')
            print('Try again')
        


    



            

