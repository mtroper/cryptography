
#Helper function used in Caesar and Vigenere
#Arguments: string, integer, integer
#Returns: character
def encrypt_helper(asciiValue, offset):
 #Using modulus to loop back to A if neccesary
        characterValue = (asciiValue + offset) % (ord('Z') + 1)
        if (asciiValue + offset) > ord('Z'):
            #If I loop back to A then I need to add the remainder to A
            characterValue += ord('A')
        return chr(characterValue)

def decrypt_helper(asciiValue, offset):
    #Checking if I need to loop back to Z
    if (asciiValue - offset) < ord('A'):
        #If I do, I use modulus to find the difference and go backwards from z
        characterValue = ord('Z')-((ord('A')-1) % (asciiValue - offset))
    else:
        characterValue = asciiValue - offset
    return chr(characterValue)

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encryptedWord = ""
    for c in plaintext:
       #filling encryptedWord with my helper method
       encryptedWord += encrypt_helper(ord(c), offset)
    return encryptedWord

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    decryptedWord = ""
    for c in ciphertext:
        #Filling decryptedWord with the decypt_helper
        decryptedWord += decrypt_helper(ord(c),offset)
    return decryptedWord

#Helper function used for Vigenere
#Arguments: integer, string
#Returns: string
def change_key_length(length, keyword):
    #Filling the key with the amount of times the plaintext fits
    key = int(length/len(keyword)) * keyword
    remainder = length%len(keyword)
    #If there is a remainder or the key is longer than plaintext
    if remainder:
        key += keyword[:remainder]
    return key

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    encryptedWord = ""
    #Modifying the length of the key to fit the plaintext
    key = change_key_length(len(plaintext),keyword)
    for i in range(len(plaintext)):
        #filling encryptedWord with my helper method
        encryptedWord += encrypt_helper(ord(plaintext[i]), ord(key[i]) - ord('A'))
    return encryptedWord

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    decryptedWord = ""
    #Modifying the length of the key to fit the plaintext
    key = change_key_length(len(ciphertext),keyword)
    for i in range(len(ciphertext)):
        #Filling decryptedWord with the decypt_helper
        decryptedWord += decrypt_helper(ord(ciphertext[i]),ord(key[i])-ord('A'))
    return decryptedWord

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
    print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))

if __name__ == "__main__":
    main()
