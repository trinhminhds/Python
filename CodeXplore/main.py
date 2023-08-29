from MainName import UseName, printF


def main():
    emails = ["trinhngocminh@gmail", "trinhngocduy@gmail.com", "trinhngochai@gmail.com"]
    for email in emails:
        usename, doname = UseName(email)
        printF(usename, doname)


if __name__ == "__main__":
    main()
