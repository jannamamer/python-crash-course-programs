pizzas = ['four cheese', 'super supreme', 'spam with stuffed crust']
friend_pizzas = pizzas[:]

pizzas.append('garlic shrimp')
friend_pizzas.append('pizza bianca')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
