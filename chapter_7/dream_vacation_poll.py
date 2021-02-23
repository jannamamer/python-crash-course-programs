input_name = "What is your name? "
question = "If you could visit one place in the world, where would you go? "
exit = "Would you like to continue with the poll? (y/n)"
responses = {}
poll_active = True

while poll_active:
    name = input(input_name)
    dream_vacation = input(question)

    responses[name] = dream_vacation

    proceed = input(exit)

    while proceed not in ['n', 'y']:
        proceed = input(exit)

    if proceed == 'n':
        poll_active = False

print("\nPoll result:")
for name, dream_vacation in responses.items():
    print(f"{name.title()} would like to go to {dream_vacation.title()}!")
