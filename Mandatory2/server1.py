import hashlib

publicGenerator = 2
publicPrime = 187
secretKey_A = 15
counter = 0
encryptedHTML = ""

def findPublickKey_A():
    global publicKey_A
    publicKey_A = (publicGenerator ** secretKey_A) % publicPrime

def findPublickKey_B():
    global publicKey_B
    publicKey_B = ((publicGenerator ** 27) % publicPrime)  # Where 27 is Bob's secret key

findPublickKey_A()
findPublickKey_B()

sharedKey = (publicKey_B**secretKey_A) % publicPrime
privateKey = hashlib.sha256(str(sharedKey).encode()).hexdigest()

document = open("index.html", "r")
documentString = ""
for x in document:
    documentString += x
documentBytes = documentString.encode()

#print(documentBytes)

#plaintext = rc4Xor(sharedKey, bytes.fromhex())
