from classes.wallet import Wallet
from classes.text import Text
import time

isRunning: bool = True
wallets: Wallet = []
current_wallet: int = 0

# FUNCTIONS
def main_menu(): # Prints the user options
    print(Text.main_menu)
    option = input("Select (1-5): ")
    match option:
        case "1":
            wallets[current_wallet].top_up(input("Enter Top-up Amount (P): "))
        case "2":
            wallets[current_wallet].send_load(input("Enter Amount Sent (P): "))
        case "3":
            wallets[current_wallet].send_load_fee(input("Enter Amount Sent (+ P15 Fee) (P): "))
        case "4":
            wallets[current_wallet].show_balance()
        case "5":
            print("\n"+"-"*32 + "\n         PROGRAM EXITED\n" + "-"*32)
            global isRunning
            isRunning = False
        case _:
            print("INVALID INPUT!")

def create_wallet():
    print(Text.line)
    name = input("Enter Name: ")
    contact_number = input("Enter Contact Number: ")
    starting_balance = input("Enter Starting Balance: ")
    try:
        sb = float(starting_balance)
    except ValueError:
        print("\nENTER VALID NUMBER!")
        return

    print("\n"+"-"*32 + "\n         SUCCESS\n" + "-"*32)
    time.sleep(1)
    return Wallet(name, contact_number, sb)


# MAIN CODE BLOCK
wallets.append(create_wallet())
while isRunning:
    main_menu()
    time.sleep(1)
    

