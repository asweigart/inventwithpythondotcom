# Import the random module for its randint() function.
import ____

# Create string constants that for each type of character:
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '1234567890'
SPECIAL = '~!@#$%^&*()_+'

# Create a string that has all of these strings combined:
ALL_CHARS = LOWER_LETTERS + ____ + ____ + ____

def generatePassword(length):
    # 12 is the minimum length for passwords:
    if length ____ 12:
        length = ____

    # Create a password variable that starts as an empty list:
    password = []
    # Add a random character from the lowercase, uppercase, digits, and
    # punctuation character strings:
    password.append(LOWER_LETTERS[random.randint(0, 25)])
    password.____(UPPER_LETTERS[random.randint(0, ____)])
    password.____(NUMBERS[random.randint(0, ____)])
    password.____(SPECIAL[random.randint(0, ____)])

    # Keep adding random characters from the combined string until the
    # password meets the length:
    while len(password) < ____:
        password.append(ALL_CHARS[random.randint(____, 74)])

    # Randomly shuffle the password list:
    random.shuffle(____)

    # Join all the strings in the password list into one string to return:
    return ''.join(____)
