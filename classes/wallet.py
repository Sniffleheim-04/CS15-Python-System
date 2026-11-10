class Wallet:

    # Constructor
    def __init__(self, name: str, contact_number: str, starting_balance: float):
        self.name = name
        self.__contact_number = contact_number
        self.__current_balance  = starting_balance

    # Return the Contact Number
    def get_contact_number(self):
        return self.__contact_number

    # Return the wallet's current balance
    def get_balance(self):
        return self.__current_balance

