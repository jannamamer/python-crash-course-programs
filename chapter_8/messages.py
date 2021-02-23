short_messages = [
    "Hi, how are you?",
    "Thank you!",
    "You're welcome!",
    "I'm on my way!"
]

sent_messages = []


def send_messages(short_messages, sent_messages):
    while short_messages:
        current_message = short_messages.pop()
        print(current_message)

        sent_messages.append(current_message)


send_messages(short_messages[:], sent_messages)
print(short_messages)
print(sent_messages)
