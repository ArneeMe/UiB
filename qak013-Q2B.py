import hashlib
import time

ja = ()
all_possibilities = ["U", "U", "U", "d", "d", "d", "d"]
hashed_string = ()
lowerCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
end = ()


def secure_this_password(password):  # Hashes the password which we are going to find
    global hashed_string
    hashed_string = hashlib.sha256(password.encode()).hexdigest()  # Function from hashlib, hashes the password sha256


secure_this_password("ABC1234")  # User inputs password


def check_hash():  # Function that checks if the hashed random word equals the hash of the password
    global hashed_string, end
    string = "".join(all_possibilities)  # Makes the array of letters and digits into one string
    if hashlib.sha256(string.encode()).hexdigest() == hashed_string:  # Hashes and compares
        end = time.time()
        total_time = end - start
        print("Great, you've found the password! It is: " + string)  # If it is the same print out and exit the script
        print(round(total_time, 2))
        exit()


start = time.time()  # Timer


for a in lowerCaseLetters:  # Multiple loops that runs through all the possibilities
    all_possibilities[0] = a
    print("You have come so far on the first letter: " + a)  # Information to see how far the script have come
    check_hash()  # All the steps check if you have found the password
    for b in lowerCaseLetters:
        all_possibilities[1] = b
        check_hash()
        for c in lowerCaseLetters:
            all_possibilities[2] = c
            check_hash()
            for d in numbers:
                all_possibilities[3] = d
                check_hash()
                for e in numbers:
                    all_possibilities[4] = e
                    check_hash()
                    for f in numbers:
                        all_possibilities[5] = f
                        check_hash()
                        for g in numbers:
                            all_possibilities[6] = g
                            check_hash()