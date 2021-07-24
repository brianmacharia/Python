import  random
import string

def split(word):
    return [char for char in word]

all_strings = split(string.printable)
digits = all_strings[0:9]
lowerCase = all_strings[10:36]
upperCase = all_strings[36:62]
syms = all_strings[62:94]

def randomLower(lowerCase):
    return random.choices(lowerCase, k=2)

def randomUpper(upperCase):
    return random.choices(upperCase, k=2)
def randomDigits(digits):
    return random.choices(digits, k=2)
def randomSyms(syms):
    return random.choices(syms, k=2)

temp = randomSyms(syms) + randomDigits(digits) + randomLower(lowerCase) + randomUpper(upperCase)

random.shuffle(temp)
password = "".join(temp)
print(password)