#Project One: Caesar Cipher

def caesar_cipher(message):
    #ascii value number
    old = 0
    #loop through string/message, store ascii num and add steps
    for l in message:
        old = ord(l)
        for i in range(3):
            if old == 122:
                old = 0
                continue
            old += 1
        print(chr(old))


caesar_cipher('bax')