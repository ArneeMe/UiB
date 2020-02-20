import hashlib
import time

password = "ADA9999"  # User inputs password with the form UUUdddd
hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Function from hashlib, hashes the password w/sha256
upper_case_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
start = time.time()  # Start the clock!

for a in upper_case_letter:  # Loops to make sure we get evey possibilites there is
    print("You have come to this first-lettter : " + a)  # User-friendly information
    end = time.time()
    print(round((end-start), 2))
    for b in upper_case_letter:
        for c in upper_case_letter:
            for d in numbers:
                for e in numbers:
                    for f in numbers:
                        for g in numbers:
                            all_possibilities = (a+b+c+d+e+f+g)  # Puts all the different possibilities into 1 variable
                            hashed_all_possibilities = hashlib.sha256(all_possibilities.encode()).hexdigest()
                            if hashed_all_possibilities == hashed_password:  # Compares two hashes
                                # If true we are done, and need to stop the time, print the password and stop the loop.
                                end = time.time()  # Stop the clock
                                print("The password is  " + all_possibilities +
                                      ". The hash is: " + hashed_all_possibilities)
                                print(round((end-start), 2))
                                exit()  # Stops the script after we have found the password
