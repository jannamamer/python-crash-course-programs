number = input("Please enter a number, we'll check if it's a multiple of 10. ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is multiple of 10.")
else:
    print(f"{number} is not multiple of 10.")
