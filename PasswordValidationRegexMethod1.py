
# TODO: Start using shebang statement

# importing re library

import re


def main():
    # TODO: It would be better to create a separate function for password_validation

    # TODO: use getpass instead of input(), it does not echo the typed password
    # https://docs.python.org/2/library/getpass.html
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

        # TODO: instead, you should've printed the valid password criteria. Makes more easy for user to get it correct next time
        # ie password should contain `at least one capital letter and so on`
        print("Password invalid !!")

    # Driver Code


if __name__ == '__main__':
    main() 
