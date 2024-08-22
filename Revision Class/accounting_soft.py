import datetime
import tkinter as tk
from tkinter import messagebox

# Define the backend accounting system
class Transaction:
    def __init__(self, date, description, amount, transaction_type):
        self.date = date
        self.description = description
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.date} | {self.transaction_type} | {self.description} | {self.amount}"

class Account:
    def __init__(self, name):
        self.name = name
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        balance = 0
        for transaction in self.transactions:
            if transaction.transaction_type in ['Receipt', 'Sales']:
                balance += transaction.amount
            elif transaction.transaction_type in ['Payment', 'Journal']:
                balance -= transaction.amount
        return balance

    def __str__(self):
        return f"Account: {self.name}, Balance: {self.get_balance()}"

class AccountingSystem:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_name):
        if account_name not in self.accounts:
            self.accounts[account_name] = Account(account_name)

    def add_transaction(self, account_name, date, description, amount, transaction_type):
        if account_name in self.accounts:
            transaction = Transaction(date, description, amount, transaction_type)
            self.accounts[account_name].add_transaction(transaction)
        else:
            print(f"Account {account_name} does not exist.")

    def get_account_balance(self, account_name):
        if account_name in self.accounts:
            return self.accounts[account_name].get_balance()
        else:
            print(f"Account {account_name} does not exist.")
            return None

    def print_account_statement(self, account_name):
        if account_name in self.accounts:
            statement = f"Statement for Account: {account_name}\n"
            for transaction in self.accounts[account_name].transactions:
                statement += str(transaction) + "\n"
            statement += f"Balance: {self.get_account_balance(account_name)}\n"
            return statement
        else:
            return f"Account {account_name} does not exist."

# Define the frontend UI using tkinter
class AccountingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Accounting Software")
        
        self.system = AccountingSystem()
        
        # Initialize UI Elements
        self.setup_ui()
    
    def setup_ui(self):
        # Account Management Frame
        self.account_frame = tk.Frame(self.root)
        self.account_frame.pack(pady=10)

        tk.Label(self.account_frame, text="Account Name:").grid(row=0, column=0)
        self.account_entry = tk.Entry(self.account_frame)
        self.account_entry.grid(row=0, column=1)
        self.add_account_button = tk.Button(self.account_frame, text="Add Account", command=self.add_account)
        self.add_account_button.grid(row=0, column=2)

        # Transaction Management Frame
        self.transaction_frame = tk.Frame(self.root)
        self.transaction_frame.pack(pady=10)

        tk.Label(self.transaction_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
        self.date_entry = tk.Entry(self.transaction_frame)
        self.date_entry.grid(row=0, column=1)

        tk.Label(self.transaction_frame, text="Description:").grid(row=1, column=0)
        self.description_entry = tk.Entry(self.transaction_frame)
        self.description_entry.grid(row=1, column=1)

        tk.Label(self.transaction_frame, text="Amount:").grid(row=2, column=0)
        self.amount_entry = tk.Entry(self.transaction_frame)
        self.amount_entry.grid(row=2, column=1)

        tk.Label(self.transaction_frame, text="Transaction Type:").grid(row=3, column=0)
        self.transaction_type_var = tk.StringVar(value="Receipt")
        self.transaction_type_menu = tk.OptionMenu(self.transaction_frame, self.transaction_type_var, "Receipt", "Payment", "Sales", "Journal")
        self.transaction_type_menu.grid(row=3, column=1)

        self.add_transaction_button = tk.Button(self.transaction_frame, text="Add Transaction", command=self.add_transaction)
        self.add_transaction_button.grid(row=4, columnspan=2, pady=10)

        # Account Statement Frame
        self.statement_frame = tk.Frame(self.root)
        self.statement_frame.pack(pady=10)

        tk.Label(self.statement_frame, text="Account Name:").grid(row=0, column=0)
        self.statement_account_entry = tk.Entry(self.statement_frame)
        self.statement_account_entry.grid(row=0, column=1)
        self.show_statement_button = tk.Button(self.statement_frame, text="Show Statement", command=self.show_statement)
        self.show_statement_button.grid(row=0, column=2)

        self.statement_text = tk.Text(self.statement_frame, height=10, width=50)
        self.statement_text.grid(row=1, columnspan=3, pady=10)

    def add_account(self):
        account_name = self.account_entry.get()
        if account_name:
            self.system.add_account(account_name)
            messagebox.showinfo("Success", f"Account '{account_name}' added.")
            self.account_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a valid account name.")

    def add_transaction(self):
        account_name = self.account_entry.get()
        try:
            date = datetime.datetime.strptime(self.date_entry.get(), "%Y-%m-%d").date()
            description = self.description_entry.get()
            amount = float(self.amount_entry.get())
            transaction_type = self.transaction_type_var.get()

            self.system.add_transaction(account_name, date, description, amount, transaction_type)
            messagebox.showinfo("Success", f"Transaction added to account '{account_name}'.")
            
            # Clear entries after adding
            self.date_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)

        except ValueError as e:
            messagebox.showwarning("Input Error", f"Invalid input: {e}")

    def show_statement(self):
        account_name = self.statement_account_entry.get()
        statement = self.system.print_account_statement(account_name)
        self.statement_text.delete(1.0, tk.END)
        self.statement_text.insert(tk.END, statement)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AccountingApp(root)
    root.mainloop()
