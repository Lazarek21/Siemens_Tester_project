import sys

for line in sys.stdin:
    plainText = line.rstrip()
    cipherText = ""
    for char in plainText:
        if ord(char) in range(65, 90):
            tmp = ord(char) - 65
            tmp += 23
            tmp %= 26 
            tmp += 65
            cipherText += chr(tmp)
        elif ord(char) in range(97, 122):
            tmp = ord(char) - 97
            tmp += 23
            tmp %= 26 
            tmp += 97
            cipherText += chr(tmp)
        else:
            cipherText += char
        
    print(cipherText)

