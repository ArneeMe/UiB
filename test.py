import hashlib
plaintext = 'hehhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh+jpijpii'
mykey = hashlib.sha256(''.encode()).digest()
textBytes = plaintext.encode()


def rc4(text, key):
    return bytes([_a ^ _b for _a, _b in zip(text, key)])


encryptedBytes = rc4(textBytes, mykey)
hexString = encryptedBytes.hex()

encryptedBytes2 = bytes.fromhex(hexString)
textBytes2 = rc4(encryptedBytes2, mykey)
plainText2 = textBytes2.decode()

print(plaintext, plainText2)
