# Logical operators: and, or, not

print("Welcome to the roller coaster")
height = int(input("what is your height in cm?"))
bill = 0


if height >= 120:  # remember to put the colon after the if statement
    print("You can ride the roller coaster")
    age = int(input('What is your age?'))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <=55:
        print('Everything is going to be ok. Have a free ride on us!')
        bill = 0
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input('Do you want a photo taken? Y or N')
    if wants_photo == "Y":
        bill += 3


    print(f"your final bill is ${bill}")

else:  # <-- remember to put the colon after
    print("Sorry, you have to grow taller before you can ride.")