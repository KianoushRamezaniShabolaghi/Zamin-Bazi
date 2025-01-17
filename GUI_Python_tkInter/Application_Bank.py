import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self, account_holder, initial_balance):
        """
        Constructor to initialize account holder and balance.
        """
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Method to deposit money into the account.
        """
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f} successfully."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        """
        Method to withdraw money from the account.
        """
        if amount > self.balance:
            return f"Insufficient funds to withdraw ${amount:.2f}."
        elif amount > 0:
            self.balance -= amount
            return f"Withdrew ${amount:.2f} successfully."
        else:
            return "Withdrawal amount must be positive."

    def display_details(self):
        """
        Method to display account details.
        """
        return f"Account Holder: {self.account_holder}\nCurrent Balance: ${self.balance:.2f}"


class BankAccountApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Account App")

        # Create the BankAccount object
        self.account = BankAccount("John Doe", 1000.0)

        # Create and pack the widgets
        self.create_widgets()

    def create_widgets(self):
        # Account Details
        self.account_details_label = tk.Label(self.root, text=self.account.display_details(), justify=tk.LEFT)
        self.account_details_label.pack(pady=10)

        # Deposit
        self.deposit_label = tk.Label(self.root, text="Deposit Amount:")
        self.deposit_label.pack()
        self.deposit_entry = tk.Entry(self.root)
        self.deposit_entry.pack(pady=5)
        self.deposit_button = tk.Button(self.root, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=5)

        # Withdraw
        self.withdraw_label = tk.Label(self.root, text="Withdraw Amount:")
        self.withdraw_label.pack()
        self.withdraw_entry = tk.Entry(self.root)
        self.withdraw_entry.pack(pady=5)
        self.withdraw_button = tk.Button(self.root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(pady=5)

        # Update Button
        self.update_button = tk.Button(self.root, text="Update Account Details", command=self.update_account_details)
        self.update_button.pack(pady=10)

    def deposit(self):
        amount = self.deposit_entry.get()
        try:
            amount = float(amount)
            result = self.account.deposit(amount)
            messagebox.showinfo("Deposit", result)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def withdraw(self):
        amount = self.withdraw_entry.get()
        try:
            amount = float(amount)
            result = self.account.withdraw(amount)
            messagebox.showinfo("Withdraw", result)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def update_account_details(self):
        self.account_details_label.config(text=self.account.display_details())


# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BankAccountApp(root)
    root.mainloop()
