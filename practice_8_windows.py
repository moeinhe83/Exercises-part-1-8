# Practice_7

# Library
from os import system as sys
from termcolor2 import colored
from pyfiglet import figlet_format

# Clear Terminal
sys('cls')

# Intro
print(colored(figlet_format("Exercises Part 1"), color='cyan'))
print(colored('=====================================================================', color='red'))
print(colored('Question Number ===> 8', color='blue'))
print(colored('// Be Sure To Read The README File To See The Question //', color='blue'))
print('                                            ')

# Practice_8
number1 = int(input('Enter Number1: '))
number2 = int(input('Enter Number2: '))
number3 = int(input('Enter Number3: '))

# IF 
if number1 == number2 or number2 == number3 or number1 == number3:
    print('SUM ===> ZERO')

else:
    print(f'{number1}+{number2}+{number3} ===> {number1+number2+number3}')

# Finish
# Create By Moein Heshmati
