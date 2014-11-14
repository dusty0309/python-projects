import random

print('Welcome to the Magic Eight Ball!')
print('Please type your question for me')

while True:
    question = input('> ')
    answers = ['Yes.', 'No.', 'Maybe.', 'Curly brackets are cool.',
               'Definitely.', 'Why are you asking me?', 'sure.',
               'I can not tell.', 'If you want to.',
               'Sorry try again later.', 'Outlook not so good.',
               'Signs point to yes.', 'Can not predict now.',
               'I am sleeping go away!',
               'Of course!',
               'Hun go ask somebody else!']
    answer = random.choice(answers)
    print(answer)




