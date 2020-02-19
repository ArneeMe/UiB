import hashlib

password = "HeiHei"
hashed_password = hashlib.sha256(password.encode()).hexdigest()
all_possibilities = []
upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"


