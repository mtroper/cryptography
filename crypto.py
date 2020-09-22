
# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encryptedWord = ""
    for c in plaintext:
        #Using modulus to loop back to A if neccesary
        characterValue = (ord(c) + offset) % (ord('Z') + 1)
        if (ord(c) + offset) > ord('Z'):
            #If I loop back to A then I need to add the remainder to A
            characterValue += ord('A')
        encryptedWord += chr(characterValue)
    return encryptedWord

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    decryptedWord = ""
    for c in ciphertext:
        #Checking if I need to loop back to Z
        if (ord(c) - offset) < ord('A'):
            #If I do, I use modulus to find the difference and go backwards from z
            characterValue = ord('Z')-((ord('A')-1) % (ord(c) - offset))
        else:
            characterValue = ord(c) - offset
        decryptedWord += chr(characterValue)
    return decryptedWord

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    pass

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    pass

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    print(decrypt_caesar("SBWKRQ",3))

if __name__ == "__main__":
    main()
