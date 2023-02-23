import random
import requests
import os

url = "https://random-word-api.herokuapp.com/word"
random_password = requests.get(url).json()[0]
lifs = 6 
list_gen = list(random_password)
list_gen = list("_"*len(random_password))

print("You start the hangman game")

while lifs > 0:
    os.system('cls')
    print(random_password, end="\n\n")
    print(f"You have left {lifs} lifs\n\n")
    print(f"Password : {list_gen}\n\n")

    answer = input("Enter the first letter for a word from the list: ")
    if answer in random_password:
        
        for i in range(len(random_password)):
            if (random_password[i]) == answer:
                list_gen[i] = answer
                print(list_gen)
              
            if list_gen == list(random_password):
                print(f"\nYou have left {lifs} lifs \n\nPassword :{random_password}\n\nYOU WIN")
                exit()
    else:
        lifs -= 1 
        if lifs == 0:
            print('Now you will give your life on the gallows\nTry again')        
    



            

