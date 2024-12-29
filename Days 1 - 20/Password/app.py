import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

result = ""
passw = ""
n_letters = int(input("How many letters you want to be in your program?\n"))
n_numbers = int(input("How many numbers you want to be in your program?\n"))
n_symbols = int(input("How many symbols you want to be in your program?\n"))

for i in range(0, n_letters):
    passw += random.choice(letters)
for i in range(0, n_numbers):
    passw += random.choice(numbers)
for i in range(0, n_symbols):
    passw += random.choice(symbols)
for i in range (n_letters+n_numbers+n_symbols):
    result += random.choice(passw)
print(result)