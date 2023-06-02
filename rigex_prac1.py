# Write a regular expression to validate a password that meets the following
# At least 8 characters long
# Contains at least one uppercase letter, one lowercase letter, and one digit

import re

pswd = input("Enter your password: ")
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!#%*?&]{8,}$"

# compiling regex
match_re = re.compile(reg)

# searching regex
res = re.search(match_re, pswd)

# validating conditions
if res:
    print("Valid Password")
else:
    print("Invalid Password")

print(" t")


shahrzadjafari95/CW10.git
