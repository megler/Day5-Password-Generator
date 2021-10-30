# passwordGenerator.py
#
# Python Bootcamp Day 5 - Password Generator
# Usage:
#      Make passwords of varying strength
#
# Marceia Egler Sept 27, 2021



#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#I did this Angela's way using multiple for loops, but with a randomized password.
pass_list = []
password = ''

for char in range(1, nr_letters + 1):
  pass_list += random.choice(letters)

for char in range(1, nr_symbols + 1):
  pass_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  pass_list += random.choice(numbers)

random.shuffle(pass_list)

for char in pass_list:
  password += char

print(f'Your new password is: {password}')


#I did this skipping the for loops but accomplishing the same thing in 6 lines of code.

#create a list of random letters, symbols and numbers using random.sample()
pass_gen = random.sample(letters, nr_letters) + random.sample(symbols, nr_symbols) + random.sample(numbers, nr_numbers)

#shuffle the list
random.shuffle(pass_gen)

#turn the shuffled list into a string
password = ''.join(pass_gen)

#print the string
print(f'Your new password is: {password}')
