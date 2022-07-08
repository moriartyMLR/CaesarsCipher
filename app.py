#Project One: Caesar Cipher

def caesar_cipher(message, steps):
    #ascii value number
    old = 0
    #loop through string/message, store ascii num and add steps
    for l in message:
        old = ord(l)
        for i in range(steps):
            if old == 122:
                old = 97
            old += 1
        print(chr(old), end="")
    print("")


caesar_cipher('baape', 2)