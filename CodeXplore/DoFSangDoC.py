def FsangC():
    do_C = int(input("Please enter C :"))
    if do_C:
        do_F = 9 * do_C / 5 + 32

        print(f"{do_C} C is converted to {do_F} F")


def main():
    FsangC()


if __name__ == "__main__":
    main()
