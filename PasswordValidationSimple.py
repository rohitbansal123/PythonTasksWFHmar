# Password validation in Python
# using naive method(Simple method without regex)

# Function to validate the password

def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%', '_', '!']

    val = True

    if len(passwd) < 8:
        print('length should be at least 8')
        val = False

    if len(passwd) > 12:
        print('length should be not be greater than 12')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the special symbols')
        val = False

    if val:
        return val

    # Main method


def main():
    passwd = input('enter password: ')

    if (password_check(passwd)):
        print("Password Accepted")
    else:
        print("Password Not Accepted!!")

    # Driver Code


if __name__ == '__main__':
    main()