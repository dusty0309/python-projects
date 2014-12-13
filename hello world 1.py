import random


print('what is your name?')
name = input('>')
print('Hello', name)
print('Welcome to the magic 8 ball!')


answers = [
    'Yes',
    'No',
    'OF COURSE',
    'X_X I died X_X ',
    'Go away',
    'U are wierd ~_~'
]

print('Please type your question for me')


while True:
    question = input('>')
    answer = random.choice(answers)
    print(answer)

