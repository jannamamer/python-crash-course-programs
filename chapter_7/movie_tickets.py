while True:
    age = input("What age are you? (Enter 'quit' to exit.) ")

    if age.lower() == 'quit':
        break
    else:
        age = int(age)

        if age < 3:
            print("Your ticket is free.")
        elif age <= 12:
            print("Your ticket is $10.")
        elif age > 12:
            print("Your ticket is $15.")
