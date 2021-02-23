def city_country(city, country):
    message = f'"{city.title()}, {country.title()}"'
    return message


country = city_country('santiago', 'chile')
print(country)

country = city_country('wellington', 'new zealand')
print(country)

country = city_country('manila', 'philippines')
print(country)
