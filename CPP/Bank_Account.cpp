#include <iostream>
#include <string>
using namespace std;

// BankAccount class definition
class BankAccount {
private:
    string accountHolder;
    double balance;

public:
    // Constructor
    BankAccount(string name, double initialBalance) {
        accountHolder = name;
        balance = initialBalance;
    }

    // Method to deposit money
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout << "Deposited $" << amount << " successfully.\n";
        } else {
            cout << "Deposit amount must be positive.\n";
        }
    }

    // Method to withdraw money
    void withdraw(double amount) {
        if (amount > balance) {
            cout << "Insufficient funds to withdraw $" << amount << ".\n";
        } else if (amount > 0) {
            balance -= amount;
            cout << "Withdrew $" << amount << " successfully.\n";
        } else {
            cout << "Withdrawal amount must be positive.\n";
        }
    }

    // Method to display account details
    void displayDetails() const {
        cout << "Account Holder: " << accountHolder << endl;
        cout << "Current Balance: $" << balance << endl;
    }
};

int main() {
    // Create an account for John Doe with an initial balance of $1000
    BankAccount johnAccount("John Doe", 1000.0);

    // Display account details
    johnAccount.displayDetails();

    // Perform some transactions
    johnAccount.deposit(500.0);
    johnAccount.withdraw(300.0);
    johnAccount.withdraw(1500.0); // Attempt to withdraw more than the balance

    // Display final account details
    johnAccount.displayDetails();

    return 0;
}
