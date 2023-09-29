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

def calculator():
    while True:
        user_input = input('select the operator you want to choose " +,-,*,/" :')
        if user_input in ['+','-','*','/']:
            a= int(input('enter the 1st number : '))
            b= int(input('enter the 2nd number : '))
            if user_input == '+':
                print(a,'+',b ,'=' ,a+b)
            if user_input == '-':
                print(a,'-',b, '=',a-b)
            elif user_input == '*':
                print(a,'*',b,'=',a*b)
            elif user_input == '/':
                print(a,'/',b,'=',a/b)
        else:
            print('You enter space or illegal value')
        repeat =  input('want to calculate again? (y/n)  : ')
        if repeat == 'n':
            break
calculator()

