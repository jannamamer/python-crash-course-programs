sandwich_orders = [
    'tuna',
    'spam',
    'cheese',
    'pastrami',
    'pastrami',
    'pastrami']
finished_sandwiches = []

print("We've run out of pastrami!")

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    if sandwich == 'pastrami':
        continue

    print(f"I made your {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print("\nList of sandwiches I made:")
for finished_sandwich in finished_sandwiches:
    print(f"\t{finished_sandwich.title()} sandwich")
