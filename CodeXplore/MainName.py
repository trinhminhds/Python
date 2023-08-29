def UseName(email):
    # trinhngocminh1999@gmail.com
    email_useName = email[0 : email.index("@")]
    email_doName = email[email.index("@") + 1 :]
    return [email_useName, email_doName]


def printF(email_useName, email_doName):
    print(f"UseName is {email_useName} ; DoName is {email_doName}")


def main():
    email = input("Please enter your email address: ").strip()
    email_useName, email_doName = UseName(email)
    printF(email_useName, email_doName)


if __name__ == "__main__":
    main()
