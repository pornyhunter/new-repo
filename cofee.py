

name = input(" What is your name ? \n")

menu = ("coffee , green tea, juice")

if name == "Alen":
    answer = input(" Hey " + name + " are you evil \n")

    if answer == "yes":
        print("Sorry, You are not welcone here ..!")
        exit()
    elif answer == "no":
        print("Hello " + name +  " Welcome, Come on in")

else:
    print("Hello " + name + " Please come in \n")
order = input(" \nThis is our menu : \n" + menu + " \n\n What would you like to have? \n")

if order == "falloda":
    price = 16
elif order == "coffee":
    price = 8 
elif order == "green tea": 
    temp = input(" Do you want it hot or cold ? \n")
    if temp == "hot":
        price = 12
    elif temp == "cold":
        price = 14
elif order =="juice":
    price = 10
else:
    print(" Sorry we don't currently have that....")

quantity = input("How many " + order + " do you like? \n  ")

Result = price * int(quantity)
print("Thank you, your " + order + " is on its way and " + "your total price is:      $" + str(Result))

exit()