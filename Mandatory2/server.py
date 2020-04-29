import hashlib
publicGenerator = 2
publicPrime = 187
secretKey_A = 15
counter = 0


def rc4(text, key):
    zipped = zip(text, key)  # Zip forces text and key to be "combined"
    xor = [a ^ b for a, b in zipped]  # XOR command while looping trough the ZIP
    return bytes(xor)  # Returns the byte version of the function


def findPublickKey_A():
    global publicKey_A
    publicKey_A = (publicGenerator ** secretKey_A) % publicPrime
    # This information is sent to the client


def findPublickKey_B():
    # This information is received from the client
    global publicKey_B
    publicKey_B = ((publicGenerator ** 27) % publicPrime)  # Where 27 is Bob's secret key


findPublickKey_A()
findPublickKey_B()

sharedKey = (publicKey_B**secretKey_A) % publicPrime  # (a ^ b) ^ c  = (a ^ c ) ^ b
print("The shared key is = " + str(sharedKey))
sharedKeySHA = hashlib.sha256(str(sharedKey).encode()).hexdigest()  # Converts to string, then hashes
print("The SHA256 of the shared key is = " + sharedKeySHA)
byteSharedKey = str(sharedKeySHA).encode()
byteSharedKeyLength = byteSharedKey*100
index = open("index.html", "r")
file = ""
for x in index:
    file += x

byteFile = file.encode()

encryptedBytes = rc4(byteFile, byteSharedKeyLength)
encryptedHex = encryptedBytes.hex()
txt = open("Ciphertext-Q3.txt", "w")
txt.write(encryptedHex)
txt.close()

