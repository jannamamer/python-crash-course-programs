favorite_places = {
    'janna': ['new zealand', 'new york'],
    'joanna': ['shoulders ni baby'],
    'baba': ['luggage']
}

for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{name.title()}'s favorite place is ", end='')
        for place in places:
            print(place.title())
    else:
        print(f"\n{name.title()}'s favorite places are:")
        for place in places:
            print(place.title())
