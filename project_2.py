#password generator

import random

letters =['a','b','c','d','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = [ '!','@','#','$','%','^','&','*','(',')','<','>','?','/','|' ]

n_letters = int(input("how many letter you want in your password ?\n"))
n_numbers = int(input("how many numbers you want in your password ?\n"))
n_symbols = int(input("how many symbols you want in your password ?\n"))

password = ""

for i in range(1,n_letters+1) :
    lett = random.choice(letters)
    password = password + lett

for i in range(1,n_numbers+1) :
    num = random.choice(numbers)
    password = password + num

for i in range(1,n_symbols+1) :
    symb = random.choice(symbols)
    password = password + symb

passw = list(password)

random.shuffle(passw)

_password = ""

for i in passw:
    _password += i

print(_password)    