#Project One: Caesar Cipher
class CaesarCipher:
    def encrypter(message, steps):
        #ascii value number and "encrypted" message placeholder
        old = 0
        encrypted = ""
        #loop through string/message, store ascii num and add shifts
        for l in message:
            old = ord(l)
            for i in range(steps):
                if old == 122:
                    old = 97
                old += 1
             #update new message placeholder
            encrypted = encrypted + chr(old)
        print(f"Encrypted message using {steps} shifts: {encrypted}")

    def decrypter(message, steps):
        #ascii value number and "decrypted" message placeholder
        old = 0
        decrypted = ""
        #loop through string/message, store ascii num and add shifts to it's value
        for l in message:
            old = ord(l)
            for i in range(steps):
                if old == 97:
                    old = 122
                old -= 1
            #update new message placeholder
            decrypted = decrypted + chr(old)
        print(f"Decrypted message using {steps} shifts: {decrypted}")

def main():
    while True:
        u_input = input("Would You Like to (E)ncrypt, (D)ecrypt, or (Q)uit: ").lower()
        if u_input == "q":
            quit()
        elif u_input == "e":
            try:
                CaesarCipher.encrypter(str(input("Enter your message to be encrypted: ")), int(input("Shift letters by: ")))
            except:
                print("Please enter a number for shifts")
        elif u_input == "d":
            try:
                CaesarCipher.decrypter(str(input("Enter your message to be decrypted: ")), int(input("Shift letters by: ")))
            except:
                print("Please enter a number for shifts")
        elif u_input != "e" or "d":
            print("Select 'e', 'd', or 'q' please")

main()