def favorite_book(title):
    """Display favorite book"""
    print(f"One of my favorite books is {title.title()}.")


active = True
while active:
    title = input("What's your favorite book? ")
    favorite_book(title)
    proceed = input("Do you want to continue? (y/n) ")

    if proceed == 'n':
        active = False
