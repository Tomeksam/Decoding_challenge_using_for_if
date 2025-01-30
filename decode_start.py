
alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"
message = ""
with open("secret.txt") as f:
    for line in f: # read it line by line
        n_vowels = 0
        for c in line:
            if c in vowel:
                n_vowels += 1
        message += alphabet[n_vowels]

print(message)