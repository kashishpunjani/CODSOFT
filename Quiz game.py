#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kashi
#
# Created:     29-09-2023
# Copyright:   (c) kashi 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

Question = ('1. who is founder of python? : ',
            '2. python was released in which year? :',
            '3. python is which type of language? : ',
            '4. which symbol is use to print comments? : ',
            '5. what is correct file extension for python file? : ',
            )
Option = (('A. James Gosling','B. Bjarne Stroustrup','C. Guido Van Rossum','D. Dennis Ritchie'),
            ('A. 1991','B. 1971','C. 1968','D. 1999'),
            ('A. Low-Level language','B.High-level Language ','C. Middle-Level-Language'),
            ('a. --','B. /*','C. //','D. #'),
            ('A. .py','B. .pyt','C. .pt','D. .pyth'))
question_number = 0
score = 0
guesses = []
Answer = ('C','A','B','D','A')

for question in Question:
    print(question)

    for option in Option[question_number]:
        print(option)

    gues = input('enter you choice (A,B,C,D) : ').upper()
    guesses.append(gues)
    if gues == Answer[question_number]:
        score += 1
        print('Correct')
    else:
        print('InCorrect')
        print(Answer[question_number], 'is the correct answer')

    question_number += 1

print('--------------------------------------------------------------------')
print('                            ****Result****                          ')
print('--------------------------------------------------------------------')
print('answer ', end='')
for answer in Answer:
    print(answer, end=' ')
print()

print('gues   ', end='')
for gues in guesses:
    print(gues, end=' ')
print()

score = int(score / len(Question) * 100)
print(f'your score is {score}%')


feedback = input('want to give feedback? (yes/no)  : ')
if feedback == 'yes':
    x = input('Please enter your feedback! ')
else:
    print('')

