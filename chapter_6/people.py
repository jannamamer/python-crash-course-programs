person_0 = {
    'first name': 'joanna christine',
    'last name': 'manez',
    'profession': 'security consultant',
    'age': '25',
    'city': 'wellington'
}

person_1 = {
    'first name': 'janna mamer',
    'last name': 'dela cruz',
    'profession': 'developer',
    'age': '27',
    'city': 'wellington'
}

person_2 = {
    'first name': 'catherine',
    'last name': 'cura',
    'profession': 'security engineer',
    'age': '26',
    'city': 'auckland'
}

people = [person_0, person_1, person_2]

for person in people:
    print("\n")
    for k, v in person.items():
        print(f"{k.title()}: {v.title()}")
