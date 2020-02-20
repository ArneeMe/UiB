import hashlib

password = "ADA9999"  # User inputs password with the form UUUdddd
hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Function from hashlib, hashes the password w/sha256
upper_case_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

for a in upper_case_letter:
    for b in upper_case_letter:
        for c in upper_case_letter:
            for d in numbers:
                for e in numbers:
                    for f in numbers:
                        for g in numbers:
                            if hashlib.sha256((a+b+c+d+e+f+g).encode()).hexdigest() == hashed_password:
                                print("Password is " + a+b+c+d+e+f+g)
                                exit()
