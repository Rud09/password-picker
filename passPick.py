import random
import string

print('Welcome to Password Picker!!')

while True:
    adjectives = ['sleepy', 'slow', 'smelly','wet', 'fat', 'red','orange', 'yellow', 'green','blue', 'purple', 'fluffy','white', 'proud', 'brave']
    nouns = ['apple', 'dinosaur', 'ball','toaster', 'goat', 'dragon','hammer', 'duck', 'panda']

    adjective=random.choice(adjectives)
    noun=random.choice(nouns)
    number=random.randrange(0,100)
    char=random.choice(string.punctuation)
    password = adjective + noun + str(number) + char

    print('Your new password is : %s' % password)
    response = input('Would you like another password? Type y or n: ')
    if response=='n':
        break