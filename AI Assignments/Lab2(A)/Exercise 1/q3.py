# (iii)The program must prompt the user for a username and password. The program should compare
# the password given by the user to a known password. If the password matches, the program should
# display “Welcome!” If it doesn’t match, the program should display “I don’t know you.
# Note: the password should not be case sensitive and it’s value is abc$123 or ABC$123

def login():
    username = input("Username: ")
    password = input("Password: ")

    known_password = "ABC$123"  # known password

    if password.lower() == known_password.lower():
        print("Welcome!")
    else:
        print("I don't know you.")

login()
