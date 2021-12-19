#!/usr/bin/env python3
# Created By: Jedidiah
# Date: Dec 14, 2021
# This program to check if year is a leap year or not

def main():
    year_as_String = input("Enter the year: ")
    try:
        year_as_int = int(year_as_String)
        if (year_as_String % 4) == 0:
            if (year_as_String % 100) == 0:
                if (year_as_String % 400) == 0:
                    print("{0} is a leap year".format(year_as_String))
                else:
                    print("{0} is not a leap year".format(year_as_String))
            else:
                print("{0} is a leap year".format(year_as_String))
        else:
            print("{0} is not a leap year".format(year_as_String))
    except Exception:
        print("This input was invalid")
    finally:
        print("Thank you for your participation.")


if __name__ == "__main__":
    main()
