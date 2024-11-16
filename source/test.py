#!/usr/bin/env python3
 
from pwn import *
import random
import string

# Configuration
HOST = '127.0.0.1'
PORT = 11111

def generate_random_guess(length):
    # Generate a random string of the given length
    return ''.join(random.choices(string.ascii_uppercase, k=length))

def test():
    # Connect to the remote service
    print(f"Connecting to {HOST}:{PORT}...")
    p = remote(HOST, PORT)

    # Receive the program's initial output
    try:
        banner = p.recvline().decode().strip()
        print(f"Banner: {banner}")
    except EOFError:
        print("Error: Did not receive expected output from the target.")
        p.close()
        exit(1)
    
    # Generate a random password guess and send it
    random_guess = generate_random_guess(8)
    print(f"Sending random guess: {random_guess}")
    p.sendline(random_guess)
    
    # Receive the response from the program
    try:
        result = p.recvall().decode().strip()
        print(f"Result: {result}")
    except EOFError:
        print("Error: Could not receive response from the target.")
        p.close()
        exit(1)

    # Determine the test outcome
    if "BOOM" in result:
        print("Test Passed: Bomb exploded as expected with incorrect input.")
        exit(0)
    elif "Congratulations" in result:
        print("Test Failed: Bomb defused with incorrect input!")
        exit(1)
    else:
        print("Test Failed: Unexpected behavior.")
        exit(1)

if __name__ == "__main__":
    test()
