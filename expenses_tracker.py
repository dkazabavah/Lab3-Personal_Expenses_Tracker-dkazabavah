#!/usr/bin/env python5

import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self, balance_file="balance.txt"):
        self.balance_file = balance_file
        self.balance = self.load_balance()

  
    def load_balance(self):
        """Load balance from file, or create one if missing."""
        if not os.path.exists(self.balance_file):
            with open(self.balance_file, "w") as f:
                f.write("0")
            return 0
        with open(self.balance_file, "r") as f:
            return float(f.read().strip())

    def save_balance(self):
        """Save updated balance."""
        with open(self.balance_file, "w") as f:
            f.write(str(self.balance))

    def calculate_total_expenses(self):
        """Sum all expenses from all expense files."""
        total = 0
        for file in os.listdir():
            if file.startswith("expenses_") and file.endswith(".txt"):
                with open(file, "r") as f:
                    for line in f:
                        parts = line.strip().split("|")
                        if len(parts) >= 4:
                            try:
                                amount = float(parts[3])
                                total += amount
                            except ValueError:
                                continue
        return total

   
    def check_balance(self):
        print("\n CHECK REMAINING BALANCE")
        total_expenses = self.calculate_total_expenses()
        available_balance = self.balance

        print(f"\n BALANCE REPORT")
        print(f"--------------------------------------")
        print(f"Initial / Current Balance: {self.balance}")
        print(f"Total Expenses to Date:    {total_expenses}")
        print(f"Available Balance:         {available_balance}")
        print(f"--------------------------------------")

        choice = input("\nDo you want to add money to your balance? (y/n): ").lower()
        if choice == "y":
            try:
                amount = float(input("Enter amount to add: "))
                if amount > 0:
                    self.balance += amount
                    self.save_balance()
                    print(f" Balance updated! New balance: {self.balance}")
                else:
                    print(" Please enter a positive amount.")
            except ValueError:
                print(" Invalid amount entered.")

    
    def add_expense(self):
        print("\n ADD NEW EXPENSE")
        print(f" Available Balance: {self.balance}")

        date = input("Enter date (YYYY-MM-DD): ")
        if not date:
            print(" Date cannot be empty.")
            return

        file_name = f"expenses_{date}.txt"
        item = input("Enter item name: ")
        try:
            amount = float(input("Enter amount spent: "))
        except ValueError:
            print(" Invalid amount. Try again.")
            return

        print(f"\nConfirm Entry:")
        print(f"Date: {date}")
        print(f"Item: {item}")
        print(f"Amount: {amount}")
        confirm = input("Save this expense? (y/n): ").lower()

        if confirm != "y":
            print(" Cancelled.")
            return

        if amount > self.balance:
            print(" Insufficient balance! Cannot save expense.")
            return

       
        expense_id = 1
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                expense_id = len(f.readlines()) + 1

        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        
        with open(file_name, "a") as f:
            f.write(f"{expense_id} | {current_time} | {item} | {amount}\n")

        
        self.balance -= amount
        self.save_balance()

        print(f" Expense saved! Remaining balance: {self.balance}")

    
    def view_expenses(self):
        while True:
            print("\n VIEW EXPENSES MENU")
            print("1. Search by Item Name")
            print("2. Search by Amount")
            print("3. Back to Main Menu")

            choice = input("Choose an option (1-3): ")

            if choice == "1":
                self.search_by_item()
            elif choice == "2":
                self.search_by_amount()
            elif choice == "3":
                break
            else:
                print(" Invalid option, try again.")

    def search_by_item(self):
        keyword = input("Enter item name to search: ").lower()
        found = False
        print("\n Search Results:")
        for file in os.listdir():
            if file.startswith("expenses_") and file.endswith(".txt"):
                with open(file, "r") as f:
                    for line in f:
                        parts = line.strip().split("|")
                        if len(parts) >= 3 and keyword in parts[2].lower():
                            print(f"{file}: {line.strip()}")
                            found = True
        if not found:
            print(" No matching item found.")

    def search_by_amount(self):
        try:
            target_amount = float(input("Enter amount to search: "))
        except ValueError:
            print(" Invalid amount.")
            return

        found = False
        print("\n Search Results:")
        for file in os.listdir():
            if file.startswith("expenses_") and file.endswith(".txt"):
                with open(file, "r") as f:
                    for line in f:
                        parts = line.strip().split("|")
                        if len(parts) >= 4:
                            try:
                                amount = float(parts[3])
                                if amount == target_amount:
                                    print(f"{file}: {line.strip()}")
                                    found = True
                            except ValueError:
                                continue
        if not found:
            print(" No expenses found for that amount.")

    
    def main_menu(self):
        while True:
            print("\n====== PERSONAL EXPENSE TRACKER ======")
            print("1. Check Remaining Balance")
            print("2. View Expenses")
            print("3. Add New Expense")
            print("4. Exit")

            choice = input("Choose an option (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.add_expense()
            elif choice == "4":
                print(" Exiting... All data saved. Goodbye!")
                break
            else:
                print(" Invalid option. Try again.")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.main_menu()

