cities = {
    'new york': {
        'country': 'usa',
        'population': '8.399M',
        'fact': 'city of dreams'
    },
    'wellington': {
        'country': 'new zealand',
        'population': '212,700',
        'fact': 'windy'
    },
    'queenstown': {
        'country': 'new zealand',
        'population': '15,650',
        'fact': 'resort town'
    }
}

for city, city_info in cities.items():
    print(f"\n{city.title()}")
    for key, val in city_info.items():
        if val.lower() == 'usa':
            print(f"\t{key.title()}: {val.upper()}")
        else:
            print(f"\t{key.title()}: {val.title()}")
