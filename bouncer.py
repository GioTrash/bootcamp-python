age = input("how old are you: ")
if age != "":
    if int(age) >= 18 and int(age)< 21:
        print("You can enter but need a wristband")

    elif int(age) >=21:
        print("You are good to enter and to drink")

    else:
        print("Come back when you're older :(")

else:
    print("Please enter a value")