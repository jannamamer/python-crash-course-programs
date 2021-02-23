favorite_numbers = {
    'joanna': [11, 2],
    'janna': [13, 211],
    'christine': [10, 20],
    'mamer': [7, 30],
    'jimuel': [2, 9]
}

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"\n{name.title()}'s favorite number is ", end='')
    else:
        print(f"\n{name.title()}'s favorite numbers are:",)

    for number in numbers:
        print(number)
