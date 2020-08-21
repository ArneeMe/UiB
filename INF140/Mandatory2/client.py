import hashlib
publicGenerator = 2
publicPrime = 187
secretKey_B = 27
counter = 0
binaryDecryptedHTML = ""


def rc4(text, key):
    zipped = zip(text, key)  # Zip forces text and key to be "combined"
    xor = [a ^ b for a, b in zipped]  # XOR command while looping trough the ZIP
    return bytes(xor)  # Returns the byte version of the function

def findPublickKey_B():
    global publicKey_B
    publicKey_B = (publicGenerator ** secretKey_B) % publicPrime


def findPublickKey_A():
    global publicKey_A
    publicKey_A = ((publicGenerator ** 15) % publicPrime)  # Where 15 is Alice's secret key


findPublickKey_A()
findPublickKey_B()

sharedKey_2 = (publicKey_A**secretKey_B) % publicPrime
print("The shared key is = " + str(sharedKey_2))
sharedKey_2SHA = hashlib.sha256(str(sharedKey_2).encode()).hexdigest()
print("The SHA256 of the shared key is = " + sharedKey_2SHA)
byteSharedKey = str(sharedKey_2SHA).encode()
byteSharedKeyLength = byteSharedKey*100

txt = open("Ciphertext-Q3.txt", "r")
hexFile = ""
for x in txt:
    hexFile += x
txt.close()

encryptedBytes2 = bytes.fromhex(hexFile)
textBytes2 = rc4(encryptedBytes2, byteSharedKeyLength)
plainText2 = textBytes2.decode()

index1 = open("index1.html", "w")
index1.write(plainText2)
index1.close()

