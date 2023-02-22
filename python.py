import random

#lista haseł
lista = ['Mountain', 'horse', 'house', 'dog', 'hamster']

#liczba żyć
lifs = 6 
#generator hasła
random_password = random.choice(lista)
list_gen = list(random_password)
print(list_gen)

print("You start the hangman game")

#Generator _____
for i in range(len(random_password)):
    list_gen[i] = "_"


while lifs > 0:
    print(f"You have left {lifs} lifs ")
    print("")
    print(f"Password : {list_gen}")
    print("")

    answer = input("Enter the first letter for a word from the list")
    if answer in random_password:
        #sprawdzamy czy i podmieniamy znaki na _
        for i in range(len(random_password)):
            if (random_password[i]) == answer:
                list_gen[i] = answer
                print(list_gen)
            #sprawdzenie czy wygrałes   
            if list_gen == list(random_password):
                print("")
                print(f"You have left {lifs} lifs \n\nPassword :{random_password}\n\nYOU WIN")
                exit()
    else:
        lifs -= 1 
        if lifs == 0:
            print('Now you will give your life on the gallows')
            print('Try again')
        


    



            

