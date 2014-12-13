print('''
Welcome to my AWESOME quiz about random stuff!!:D
''')
print('''
What is 9 + 10?
''')

answer = input('>')

if answer == '19':
    print('Nope try again next time')
elif answer == '21':
    print('yay you got it right!')
else:
    print('Incorrect')
