# importing re library

import re


def main():
    passwd = input('enter password:')

    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,12}$"

    # compiling regex

    pat = re.compile(reg)

    # searching regex

    mat = re.search(pat, passwd)

    # validating conditions

    if mat:

        print("Password is valid.")

    else:

        print("Password invalid !!")

    # Driver Code


if __name__ == '__main__':
    main() 