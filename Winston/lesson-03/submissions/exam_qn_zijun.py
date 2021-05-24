import random

name = input('Please enter your name: ')
print(f'\nHello {name},')
print('Here are 10 questions. Key in \'help\' for a hint and \'end\' to stop your test.\n')

i = 1
correct = 0
wrongTotal = 0

while i < 12:

    if i == 11:
        if wrongTotal == 0:
            print(f'You have completed all questions with 0 wrong answer!')
            print(f'You are the pride and joy of every asian parents, {name}! \n')
            break
        elif wrongTotal == 1:
            print(f'You have completed all questions with 1 wrong answer!')
            print(f'Almost perfect! Good job, {name}! \n')
            break
        else:
            print(f'You have completed all questions with {wrongTotal} wrong answers!')
            print(f'Practice more! You can do it, {name}! \n')
            break

    firstRandom = random.randint(1,100)
    secondRandom = random.randint(1,100)


    #print((firstRandom + secondRandom))        #if need to check
    answer = input(f'Question {i}: {firstRandom} + {secondRandom} = ')

    while answer != str(firstRandom + secondRandom):
        if answer == 'end':
            break
        elif answer == 'help':
            print('\nIt is close to', str(firstRandom + secondRandom - 1))
            answer = input(f'Try again: {firstRandom} + {secondRandom} = ')
        else:
            wrongTotal = wrongTotal + 1
            answer = input(f'Please try again: {firstRandom} + {secondRandom} = ')

    if answer == 'end':
        if correct == 0:
            print(f'\n{name}! Why didn\'t you finish one?!')
            print('Hope to see you finish one next round!\n')
        elif correct == 1:
            if wrongTotal == 0 or wrongTotal == 1:
                print(f'\nYou have completed 1 question with {wrongTotal} wrong answer!')
                print(f'One is better than nothing. See you next time {name}!\n')
            else:
                print(f'\nYou have completed 1 question with {wrongTotal} wrong answers!')
                print(f'Where is your A in Asian, {name}?!\n')
        else:
            if wrongTotal == 0:
                print(f'\nYou have completed {correct} questions with 0 wrong answer!')
                print(f'You are the pride and joy of every asian parents, {name}! \n')
            elif wrongTotal == 1:
                print(f'\nYou have completed {correct} questions with 1 wrong answer!')
                print(f'Almost perfect! Good job, {name}! \n')
            else:
                print(f'\nYou have completed {correct} questions with {wrongTotal} wrong answers!')
                print(f'Practice more! You can do it, {name}! \n')
        break

    print('Correct!\n')

    correct = correct + 1
    i = i + 1
