# Prompt user for texts

texts = input("Input: ")

# List of vowel
vowel = ["a", "e", "i", "o", "u"]


for v in (("a", ""), ("e", ""), ("i",""), ("o",""), ("u",""),("A", ""), ("E", ""), ("I",""), ("O",""), ("U","")):
    texts = texts.replace(*v)
print(texts)