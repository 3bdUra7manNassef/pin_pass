import string
import random

number = list(string.digits)

while True:

    try:

        numbers_password = input("enter number to password: ")

        numbers_password = int(numbers_password)

        if numbers_password < 4:

            print("you need more number")

            numbers_password = input("enter number to password: ")

        else:

            numbers_password =int (input("enter number to password: "))

            random.shuffle(number)

            password = []

            Prospect = round(numbers_password*(100/100))

            for i in range(Prospect):

                password.append(number[i])

            password="".join(password[0:])

            print("your password----> " + password)

    except:

        print("error please try agin")

