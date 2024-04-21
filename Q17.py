word = input("Type word here: ")
Vowel = ["A","a","E","e","I","i","O","o","U","u"]


count = 0
for i in range(len(word)):
    if word[i] in Vowel:
        count += 1
    else:
        count += 0


print(count)
        
