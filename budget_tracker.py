import csv
import os
from datetime import date

FILENAME = "budget.csv"
FIELDNAMES = ["date", "type", "category", "description", "amount"]


def load_transactions():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, newline="") as f:
        reader = csv.DictReader(f)
        transactions = []
        for row in reader:
            row["amount"] = float(row["amount"])
            transactions.append(row)
    return transactions


def save_transaction(transaction):
    file_exists = os.path.exists(FILENAME)
    with open(FILENAME, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if not file_exists:
            writer.writeheader()
        writer.writerow(transaction)


def add_transaction(t_type):
    print(f"\n  -- Add {t_type.capitalize()} --")

    category = input("  Category (e.g. Food, Rent, Salary): ").strip()
    description = input("  Description: ").strip()

    while True:
        try:
            amount = float(input("  Amount ($): ").strip())
            if amount <= 0:
                print("  Amount must be greater than 0.")
            else:
                break
        except ValueError:
            print("  Please enter a valid number.")

    transaction = {
        "date": str(date.today()),
        "type": t_type,
        "category": category,
        "description": description,
        "amount": round(amount, 2),
    }

    save_transaction(transaction)
    print(f"  ✓ {t_type.capitalize()} of ${amount:.2f} saved.")


def view_summary(transactions):
    if not transactions:
        print("\n  No transactions yet.")
        return

    total_income  = sum(t["amount"] for t in transactions if t["type"] == "income")
    total_expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance       = total_income - total_expense

    print("\n" + "=" * 50)
    print(f"  {'DATE':<12} {'TYPE':<10} {'CATEGORY':<12} {'AMOUNT':>8}  DESCRIPTION")
    print("-" * 50)

    for t in transactions:
        sign = "+" if t["type"] == "income" else "-"
        print(f"  {t['date']:<12} {t['type']:<10} {t['category']:<12} "
              f"{sign}${t['amount']:<7.2f}  {t['description']}")

    print("=" * 50)
    print(f"  Total Income  : +${total_income:.2f}")
    print(f"  Total Expenses: -${total_expense:.2f}")
    print(f"  Balance       :  ${balance:.2f}")
    print("=" * 50 + "\n")


def view_by_category(transactions):
    if not transactions:
        print("\n  No transactions yet.")
        return

    categories = {}
    for t in transactions:
        cat = t["category"]
        if cat not in categories:
            categories[cat] = 0
        categories[cat] += t["amount"] if t["type"] == "expense" else -t["amount"]

    print("\n  -- Spending by Category --")
    for cat, total in sorted(categories.items()):
        label = f"  {cat:<20}"
        if total > 0:
            print(f"{label} Spent:  ${total:.2f}")
        else:
            print(f"{label} Net income: +${abs(total):.2f}")
    print()


def main():
    print("=" * 50)
    print("           Budget Tracker")
    print("=" * 50)

    menu = """
  1. Add income
  2. Add expense
  3. View all transactions & summary
  4. View by category
  5. Quit
"""

    while True:
        print(menu)
        choice = input("  Choose an option (1-5): ").strip()

        if choice == "1":
            add_transaction("income")
        elif choice == "2":
            add_transaction("expense")
        elif choice == "3":
            transactions = load_transactions()
            view_summary(transactions)
        elif choice == "4":
            transactions = load_transactions()
            view_by_category(transactions)
        elif choice == "5":
            print("  Goodbye!")
            break
        else:
            print("  Invalid option. Please enter 1–5.")


if __name__ == "__main__":
    main()
