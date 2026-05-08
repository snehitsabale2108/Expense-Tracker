import csv
import os
from datetime import datetime
from tabulate import tabulate

def create_file():
    if not os.path.exists("expense.csv"):
        with open("expense.csv","w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date","Amount","Category","Note"])


def add_expense():
    amount = input("Enter Amount: ")
    category = input("Enter the category (like Food, Travelling, eBills...): ")
    note = input("Enter the Note (Optional): ")
    date = datetime.now().strftime("%y-%m-%d")

    with open("expense.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])
    print("Expense added Sucessfully")

def view_expense():
    if not os.path.exists("expense.csv"):
        print("No Expense Found")
        return
    with open("expense.csv","r") as file:
        reader = csv.reader(file)
        data = list(reader)

        print(tabulate(data[1:], headers=data[0], tablefmt="grid"))
        for row in reader:
            print(row)

def total_spent():
    if not os.path.exists("expense.csv"):
        print("No Expense Found")
        return

    total = 0
    with open("expense.csv","r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                if row[1] != "":
                    total = total + float(row[1])
            except ValueError:
                print("Skipping invalid row: ", row)

        print("Total Spent: ", total)

def delete_expense():
    if not os.path.exists("expense.csv"):
        print("No Expense Found")
        return

    rows = []
    with open("expense.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("No expenses to delete")
        return

    print("\n------ Expenses ------")
    for i in range(1, len(rows)):
        print(f"{i}. {rows[i]}")

    try:
        choice = int(input("Enter expense number to delete: "))
        if choice < 1 or choice >= len(rows):
            print("Invalid choice")
            return

        deleted = rows.pop(choice)

        with open("expense.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Deleted Successfully:", deleted)

    except ValueError:
        print("Enter a valid number")

def main():
    create_file()
    while True:
        print("------------EXPENSE TRACKER------------")
        print("\n 1. Add Expense")
        print("\n 2. View Expense")
        print("\n 3. Total Spent")
        print("\n 4. Delete Expense")
        print("\n 5. Exit")
        print("---------------------------------------")

        c = input("Enter your Choice (1-4): ")
        if c == "1":
            add_expense()
        elif c == "2":
            view_expense()
        elif c == "3":
            total_spent()
        elif c == "4":
            delete_expense()
        elif c == "5":
            print("Bye")
            break
        else:
            print("Invalid Choice")


if __name__=="__main__":
    main()
