import random
def g_p(l):
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    password = ""
    for i in range(l):
        character = random.choice(characters)
        password += character
    return password
l = int(input("Enter the desired length of the password: "))
password = g_p(l)
print("The generated password is:", password)