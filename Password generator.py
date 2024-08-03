alphabetList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numberList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbolList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "/", "?", "~", "`"]

print("Welcome to SILVERMAX password generator")
letters=int(input("How many letters do you want?\n"))
symbol=int(input("How many symbols do you want?\n"))
numbers=int(input("How many numbers do you want?\n"))

import random

password = []
for _ in range(letters):
    password.append(random.choice(alphabetList))

for _ in range(symbol):
    password.append(random.choice(symbolList))

for _ in range(numbers):
    password.append(random.choice(numberList))

random.shuffle(password)
final_password="".join(password)
print(f"Your New Password is: {final_password}")