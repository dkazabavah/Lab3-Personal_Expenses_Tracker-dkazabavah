Expense Tracker System Overview
This system manages personal finances using two main components: a Python Application for daily tracking and a Shell Script for archival.

1. Python Expense Tracker 
This is the main application you use to manage your money.

Key Features
Balance: The program reads and updates your current balance from the balance.txt file. You can add funds (like a deposit) when checking your balance.

Expenses:

Use option 3 to record spending.

It saves each expense to a file named after the date (e.g., expenses_YYYY-MM-DD.txt).

It automatically subtracts the amount from your stored balance.

It prevents you from recording an expense if the amount is greater than your current balance.

Search: Use option 2 to view and search expenses by Item Name or Amount.

Data Storage
The Python program manages these files:

balance.txt: Stores your single, current balance amount.

expenses_YYYY-MM-DD.txt: Stores all daily expense records using a pipe-separated format.

2. Shell Script Archive Manager (archive_manager.sh)
This script is used to organize and retrieve old expense files, keeping your main folder clean.

Functions
1. Archive File:

Moves an old daily expense file (like expenses_*.txt) to a dated backup folder.

It creates the folder structure archives/YYYY-MM-DD/ and logs the action in archive_log.txt.

2. Search Archive:

Prompts you for a specific date (YYYY-MM-DD).

It then lists and displays the contents of all files that were archived on that specific date.
