import sys

sys.argv.pop(0)

for word in sys.argv:
    wordLen = len(word)
    palindrom = True
    for i in range(wordLen//2):
        #minus one because wordLen isnt last index but it is length all word
        if word[i] != word[(wordLen-1)-i]:
            palindrom = False
            break
    
    if palindrom:
        print(word, " > is palindrome.")
    else:
        print(word, " > isnt palindrome.")