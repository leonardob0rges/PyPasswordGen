#!/usr/bin/env python3
import random
import time
    
lower_letters = 'abcdefghijklmnopqrstuvwxyz'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
math_operators = '+-*/<>'
symbols = "!@#%&()`{}[]^~:;.,\|/_"
currencies='$£¢'
all_chars = lower_letters + upper_letters + numbers + symbols + currencies

def createPassword():
    length = int(input('[*] How much password length you want: '))
    print('Generating password')
    for i in range(3):
        print('.')
        time.sleep(0.2)
    password = ''.join(random.sample(all_chars,length))
    print('\nYour password: ',password)

createPassword()
