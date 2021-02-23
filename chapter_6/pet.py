pet_0 = {
    'kind': 'dog',
    'owner': 'janna'
}

pet_1 = {
    'kind': 'cat',
    'owner': 'cat'
}

pets = [pet_0, pet_1]

for pet in pets:
    for k, v in pet.items():
        print(f"{k.title()}: {v.title()}")
    print("\n")
