words = {
    'dictionary': 'A collection of key-value pairs.',
    'tuple': 'An immutable list.',
    'list comprehension': 'Combines the for loop and the creation of new'
    'elements into one line, and automatically appends each new element.',
    'PEP 8': 'Instructs Python programmers on how to style their code.',
    'none': 'A special value meant to indicate the absense of a value.',
    'set': 'A collection in which each item must be unique.',
    'sorted()': "Lets you display your list in a particular order but doesn't"
    "affect the actual order of the list",
    '': "",
    '': "",
    '': ""
}

for key, value in words.items():
    print(f"{key.title()}: {value}\n")
