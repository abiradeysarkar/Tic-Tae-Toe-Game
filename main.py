import utility
from mysqlDB import Database


def takeChoice():
    print("Menu :")
    print("1. History")
    print("2. Play game")
    print("3. Exit")
    return input("Please enter choice (1/2/3):")


choice = takeChoice()
while choice != "3":
    if choice == "1":
        database = Database()
        conn = database.connect()
        database.doQuery(conn)

    elif choice == "2":
        utility.game()
    elif choice == "3":
        exit

    choice = takeChoice()
