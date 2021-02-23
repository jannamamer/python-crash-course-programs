prompt = "Please enter the pizza toppings you want. Enter 'quit' once done. "

while True:
    topping = input(prompt)

    if topping.lower() == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")
