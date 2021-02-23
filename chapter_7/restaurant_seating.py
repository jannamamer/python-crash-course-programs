prompt = "Welcome to Joja! \n"
prompt += "How many are you? "

no_of_people = input(prompt)
no_of_people = int(no_of_people)

prompt = "Your name please. "

name = input(prompt)

if no_of_people > 8:
    print(f"Sorry {name.title()}, but you have to wait for a table to free up."
          )
else:
    print(f"{name.title()}, you're table is ready!")
