#! /usr/bin/env python3

# Import OS and clear screen
import os
os.system("clear")

# Import required modules
from haveibeenpwnd import check_password
import getpass



yourPassword = getpass.getpass("What password do you want to use? ")

meow = check_password(yourPassword)



pwn_count = meow["count"]


if pwn_count > 0:
    print(f"This password has been pwned {pwn_count} times. Better use different one.")
else:
    print("Can't find any known pwnage for this password.")
