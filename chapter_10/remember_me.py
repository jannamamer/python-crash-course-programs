import json


def greet_user():
    """Greet the user by name."""
    filename = 'username.json'
    username = get_stored_username(filename)

    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(filename)
        print(f"We'll remember you when you come back, {username}!")


def get_stored_username(filename):
    """Get stored username if available."""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username(filename):
    """Prompt for a new username."""
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


greet_user()
