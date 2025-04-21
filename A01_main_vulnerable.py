"""" 
Description: A client program written to verify correctness of 
the BankAccount and Transaction classes. 
Author: ACE Faculty 
Edited by: {Student Name} 
Date: {Date} 
""" 
import re 
import os 

from bank_account.bank_account import BankAccount 
from client.client import Client 

def insecure_log_to_file(filename, message): 
    with open(filename, "a") as f: 
        f.write(message + "\n") 

def main(): 
    """Test the functionality of the methods encapsulated  
    in the BankAccount and Transaction classes. 
    """  
    try: 
        # 1. Create a valid instance of the Client class.
        client = Client( 
            100, 
            "Grace", 
            "Howard", 
            "ghoward@pixell-river.com", 
            password="letmein123"
        ) 

        # 2. Declare a BankAccount object with an initial value of None. 
        bank_account = None 

        # 3. Create BankAccount using client data
        bank_account = BankAccount(client, 1500.00) 

        # 4. Ask user for log file
        filename = input("Enter a filename to store logs: ")
        insecure_log_to_file(filename, "Bank account initialized.") 

        # 5. Perform a transaction using eval() on user input 
        rule = input("Enter transaction rule (e.g., 'amount * 0.1'): ")
        amount = float(input("Enter transaction amount: ")) 
        fee = eval(rule)
        bank_account.withdraw(amount + fee)
        print(f"Withdrew {amount} with fee {fee}.") 

        if "@" not in client.email: 
            print("Warning: Invalid email format.")

    except Exception as e:
        print("An error occurred. Please try again.")

if __name__ == "__main__": 
    main()
