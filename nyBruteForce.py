import hashlib
import time


password = "ABB1434"
hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Function from hashlib, hashes the password sha256
upper_case_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
alle_muligheter = ["U", "U", "U", "d", "d", "d", "d"]

start = time.time()

for a in upper_case_letter:
    alle_muligheter[0] = a
    for b in upper_case_letter:
        alle_muligheter[1] = b
        for c in upper_case_letter:
            alle_muligheter[2] = c
            for d in numbers:
                alle_muligheter[3] = d
                for e in numbers:
                    alle_muligheter[4] = e
                    for f in numbers:
                        alle_muligheter[5] = f
                        for g in numbers:
                            alle_muligheter[6] = g
                            hashed_alle_muligheter = hashlib.sha256("".join(alle_muligheter).encode()).hexdigest()
                            if hashed_alle_muligheter == hashed_password:
                                end = time.time()
                                total_time = end-start
                                print("Passordet er " + "".join(alle_muligheter))
                                print(total_time)
                                exit()
