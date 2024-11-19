import string
encryptedText = 'XRPCTCRGNEI'

alphabets = list(string.ascii_uppercase)

for i in range(26):
    decryptedText = ''
    for char in encryptedText:
        if char in alphabets:
            position = alphabets.index(char)
            decryptedText += alphabets[(position - i) % 26]
    print(decryptedText)

# the plaintext here is ICANENCRYPT :)

print(118613842%9091)