from string import digits, punctuation, ascii_letters
import itertools
import win32com.client as client
from datetime import datetime
import time

# password is 'aA'
# pip install pywin32 - it used to open win files

symbols = digits + punctuation + ascii_letters
print(symbols)


def brute_excel_doc():
    print("---- Hello Friend ----")
    try:
        password_length = input("Write the length of password (ex: 3 - 7): ")
        password_length = [int(item) for item in password_length.split('-')]


    except:
        print('Check your input!')

    print("If the password included only numbers, insert: 1 \n"
          "If the password included only letters, insert: 2 \n"
          "If the password included numbers and letters, insert: 3 \n"
          "If the password included numbers, letters and symbols, insert: 4 \n")

    try:
        choice = int(input(": "))
        if choice == 1:
            possible_symbols = digits
        elif choice == 2:
            possible_symbols = ascii_letters
        elif choice == 3:
            possible_symbols = digits + ascii_letters
        elif choice == 4:
            possible_symbols = digits + ascii_letters + punctuation
        else:
            possible_symbols = "Really??"
        # print(possible_symbols)
    except:
        print("Something is wrong!!!")

    start_timestamp = time.time()
    print(f"Started al - {datetime.utcfromtimestamp(time.time()).strftime('%H:%M:%S')}")
    count = 0

    for password_length in range(password_length[0], password_length[1] + 1):
        for password in itertools.product(possible_symbols, repeat=password_length):
            password = "".join(password)
            # print(password)

            opened_doc = client.Dispatch("Excel.Application")
            count += 1
            # ond de excel file ad send password to it as param,
            try:
                opened_doc.Workbooks.Open(
                    r"C:\Users\Contabil\Python_Portfolio_Projects\Finding_forgotten_password_for_Excel_file\Book1.xlsx",
                    False,
                    True,
                    None,
                    password
                )

                time.sleep(0.1)
                print(f"Finished al - {datetime.utcfromtimestamp(time.time()).strftime('%H:%M:%S')}")
                print(f"Password cracking time - {time.time() - start_timestamp}")
                return f"Attempt #{count} Password is: {password}"
            except:
                print(f"{count} Incorrect {password}")
                pass


def main():
    print(brute_excel_doc())


if __name__ == '__main__':
    main()
