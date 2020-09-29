import random
import math

#Helper function used to ecnrypt in Caesar and Vigenere
#Arguments: integer, integer
#Returns: character
def encrypt_helper(asciiValue, offset):
 #Using modulus to loop back to A if neccesary
        characterValue = (asciiValue + offset) % (ord('Z') + 1)
        if (asciiValue + offset) > ord('Z'):
            #If I loop back to A then I need to add the remainder to A
            characterValue += ord('A')
        return chr(characterValue)

#Helper function used to decrypt in Caesar and Vigenere
#Arguments: integer, integer
#Returns: character
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
        #If the character is uppercase A-Z
        if ord(c) >= ord("A") and ord(c) <= ord("Z"):
            #filling encryptedWord with my helper method
            encryptedWord += encrypt_helper(ord(c), offset)
        else:
            encryptedWord += c
    return encryptedWord

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    decryptedWord = ""
    for c in ciphertext:
         #If the character is uppercase A-Z
        if ord(c) >= ord("A") and ord(c) <= ord("Z"):
            #Filling decryptedWord with the decypt_helper
            decryptedWord += decrypt_helper(ord(c),offset)
        else:
            decryptedWord += c
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
    W = [1]
    for i in range (n-len(W)):
        #Making the superincreasing sequence
        W.append(random.randint(sum(W)+1, 2*sum(W)))
    #Turning it to a tuple
    W = tuple(W)
    #Q is essentially the next number in the superincreasing sequence
    Q = random.randint(sum(W)+1, 2*sum(W))
    R = 0
    #Finding an R such that its gcd with Q is 1
    while math.gcd(R,Q) != 1:
        R = random.randint(2, Q-1)
    return (W,Q,R)

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: B - a length-n tuple of integers
def create_public_key(private_key):
    B = []
    for i in range(len(private_key[0])):
        #Filling a tuple with the superincreasing sequence * R % Q
        B.append((private_key[2]*private_key[0][i])%private_key[1])
    return tuple(B)

# Arguments: string, tuple B
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    encryptedMessage = []
    for c in plaintext:
       M = []
       C = 0
       #Turning each character of the message into binary
       binary = bin(ord(c))[2:].zfill(8)
       M = [char for char in str(binary)]
       for i in range(len(M)):
           #Summing the multiplication of each digit in the binary by the corresponding index of the public key
           C += (int(M[i]) * public_key[i])
       encryptedMessage.append(C)
    return encryptedMessage

# Arguments: list of integers, private key (W, Q, R) with W a tuple.
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    S = 1
    decryptedMessage = ""
    #Finding an S such that R * S % Q is 1
    while((private_key[2] * S) % private_key[1] != 1):
        S += 1
    for C in ciphertext:
        #Multiplying by S then mod Q because it becomes 1
        #This leaves us with C1 just being equal to the sum of the multiplcation of the superincreasing sequence and the character in binary
        C1 = (S*C) % private_key[1]
        binaryValues = []
        for i in range(len(private_key[0])):
            #Since the sequence is superincreasing we can determine exactly which numbers are used in it and their corresponding binary
            #If the number is smaller than or equal to the sum it must be included since the sum of everything before it is smaller
            if(private_key[0][len(private_key[0]) - i-1] <= C1):
                binaryValues.append(1)
                C1 -= private_key[0][len(private_key[0]) - i-1]
            else:
                #If the number is larger than the sum it's impossible for it to fit
                binaryValues.append(0)
        #Since we looped from small to big when we shouldve went big to small we must reverse
        binaryValues.reverse()
        binary = ''.join(map(str, binaryValues))
        #Turn binary back to ASCII then back to the actual characters
        decryptedMessage += chr(int(binary,2))
    return decryptedMessage

def main():
    prin("Hello World")

if __name__ == "__main__":
    main()
