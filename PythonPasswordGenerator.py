import string
import secrets


def generatePWD():
    """
    Generates and returns a password with at least one uppercase, one digit,
    and one punctuation character.

    Returns False if any of the input provided by the user is not valid.
    """

    # try-except to catch a ValueError in case the user enters input that is
    # not a number
    try:
        # Gets password length from the user
        charsStr = input("Password length? [8] ")

        # Sets default password length to 8 or uses the user's input
        charsInt = 8 if charsStr.strip() == "" else int(charsStr)

        # Checks if user's password length is 8 or greater
        if charsInt < 8:
            print("Password length can't be less than 8")
            return False
        else:
            # Password character set
            pwdCharSet = string.ascii_letters + string.digits +\
                string.punctuation

            # Loop to ensure password contains at least one uppercase, one
            # digit, and one punctuation character
            while True:
                # Generates random password
                pwd = ''.join(secrets.choice(pwdCharSet)
                              for i in range(charsInt))

                # Break out of the loop if the password contains at least one
                # uppercase, one digit, and one punctuation character
                if (
                    any(i for i in pwd if i in string.ascii_uppercase)
                    and any(i for i in pwd if i in string.digits)
                    and any(i for i in pwd if i in string.punctuation)
                ):
                    print(pwd)
                    break

            return pwd
    except ValueError:
        print("Enter a valid number that is 8 or greater")
        return False


if __name__ == "__main__":
    generatePWD()
