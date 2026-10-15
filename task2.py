
import csv
import os

FILE_NAME = "expenses.csv"


def add_expense(description, amount):
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writerow(["Description", "Amount"])

        writer.writerow([description, amount])

    print("Expense added successfully!")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found. Please add an expense first.")
        return

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    if not expenses:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")
    for expense in expenses:
        print(
            f"Item: {expense['Description']}, "
            f"Amount: Rs. {float(expense['Amount']):.2f}"
        )


def total_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found. Please add an expense first.")
        return

    total = 0.0

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            total += float(expense["Amount"])

    print(f"\nTotal Expenses: Rs. {total:.2f}")


def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            description = input("Enter expense description: ").strip()

            if not description:
                print("Description cannot be empty.")
                continue

            try:
                amount = float(input("Enter amount (Rs.): "))

                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue

                add_expense(description, amount)

            except ValueError:
                print("Please enter a valid numeric amount.")

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
