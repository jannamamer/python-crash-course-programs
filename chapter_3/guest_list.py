guests = ["cat", "kyle", "byron"]
for g in guests:
    print(f"You're invited {g.title()}!")

print(f"I'm inviting {len(guests)} people to dinner.")

cant_come = "byron"
print(f"{cant_come.title()} can't come to the dinner.")

guests.remove(cant_come)
guests.append("irene")

for g in guests:
    print(f"You're invited {g.title()}!")

print("I've found a bigger dinner table")

guests.insert(0, "cecille")
guests.insert(1, "cathy")
guests.append("plo")

for g in guests:
    print(f"You're invited {g.title()}!")

print("I'm sorry but I can only invite two people for the dinner.")

i = 6
while i > 2:
    message = f"I'm sorry {guests.pop().title()}, I can only invite two people"
    message += " to dinner"
    print(message)
    i -= 1

for g in guests:
    print(f"You're still invited {g.title()}!")

i = 0
while i < 2:
    del guests[0]
    i += 1

print(guests)
