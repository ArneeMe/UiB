import hashlib
publicGenerator = 2
publicPrime = 187
secretKey_B = 27
counter = 0
binaryDecryptedHTML = ""


def findPublickKey_B():
    global publicKey_B
    publicKey_B = (publicGenerator ** secretKey_B) % publicPrime


def findPublickKey_A():
    global publicKey_A
    publicKey_A = ((publicGenerator ** 15) % publicPrime)  # Where 15 is Alice's secret key


findPublickKey_A()
findPublickKey_B()

sharedKey_2 = (publicKey_A**secretKey_B) % publicPrime
encryptedKey = hashlib.sha256(str(sharedKey_2).encode()).hexdigest()
binaryEncryptedKey = ''.join(format(ord(x), 'b') for x in encryptedKey)
binaryEncryptedKeyCorrectLength = 1000 * binaryEncryptedKey


encryptedFile = open("Ciphertext-Q3.txt", "r")
for x in encryptedFile.read():
    if x == binaryEncryptedKeyCorrectLength[counter]:
        binaryVariable = 0
    else:
        binaryVariable = 1
    binaryDecryptedHTML = binaryDecryptedHTML + str(binaryVariable)
    counter += 1


# Here should you convert binary back to normal text and you will receive the original answer.


print("The shared secret key is = " + str(sharedKey_2) + ". The SHA256 value of this is = " + str(encryptedKey))
