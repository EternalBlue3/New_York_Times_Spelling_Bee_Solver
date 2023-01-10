import time

middle = input("Enter the middle letter: ").upper()
other_letters = input("Enter the other letters: ").upper()

missing = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ") - set(other_letters + middle)

starttime = time.time()
with open('wordlist.txt', 'r') as f:
    wordlist = {x.strip() for x in f}

valid_words = wordlist & {word for word in wordlist if middle in word and not missing.intersection(word)}

for x in valid_words:
    print(x)
print("Time Taken:",time.time()-starttime)