class Wallet:

    # Constructor
    def __init__(self, name: str, contact_number: str, starting_balance: float):
        self.name = name
        self.__contact_number = contact_number
        self.__current_balance  = starting_balance

    # Returns the contact number of the wallet's owner
    def get_contact_number(self):
        return self.__contact_number

    # Returns the current balance of the wallet
    def get_balance(self):
        return self.__current_balance

    # Adds the current balance
    def top_up(self, amount: float):
        try:
            n = float(amount)
            if n < 1:
                print("\n"+"-"*32 + "\n       TOP UP AMOUNT CANNOT BE LESS THAN ZERO\n" + "-"*32)
                return
        except  ValueError:
            print("\n"+"-"*32 + "\n       PLEASE ENTER A VALID NUMBER\n" + "-"*32)
            return
        
        self.__current_balance += n
        print("\n"+"-"*32 + 
              "\n       Top-up Successful!" + 
             f"\n     New Balance: P{self.__current_balance:.2f}\n" + "-"*32)

    # Prints the current balance
    def show_balance(self):
        print("\n"+"-"*32 + f"\nCurrent Balance: P{self.__current_balance}\n" + "-"*32)

    # Sends load to the same network without fee
    def send_load(self, amount: float):
        try:
            n = float(amount)
            if n < 1:
                print("\n"+"-"*32 + "\n       TOP UP AMOUNT CANNOT BE LESS THAN ZERO\n" + "-"*32)
                return
        except  ValueError:
            print("\n"+"-"*32 + "\n       PLEASE ENTER A VALID NUMBER\n" + "-"*32)
            return

        if self.__current_balance < 0:
            print("\n"+"-"*32 + "\n       CURRENT BALANCE IS ZERO\n" + "-"*32)
            return
        elif n > self.__current_balance:
            print("\n"+"-"*32 + "\n       AMOUNT EXCEEDS CURRENT BALANCE\n" + "-"*32)
            return
        else:
            self.__current_balance -= n
            print("\n"+"-"*32 + 
                    "\n       Sent Successfully!" + 
                    f"\n     New Balance: P{self.__current_balance:.2f}\n" + "-"*32)
    
    # Sends load to other network with fee
    def send_load_fee(self, amount: float):
            fee = 15
            try:
                n = float(amount)
                if n < 1:
                    print("\n"+"-"*32 + "\n       TOP UP AMOUNT CANNOT BE LESS THAN ZERO\n" + "-"*32)
                    return
            except  ValueError:
                print("\n"+"-"*32 + "\n       PLEASE ENTER A VALID NUMBER\n" + "-"*32)
                return

            n += fee
            if self.__current_balance < 0:
                print("\n"+"-"*32 + "\n       CURRENT BALANCE IS ZERO\n" + "-"*32)
                return
            elif n > self.__current_balance:
                print("\n"+"-"*32 + "\n       AMOUNT EXCEEDS CURRENT BALANCE\n" + "-"*32)
                return
            else:
                self.__current_balance -= n
                print("\n"+"-"*32 + 
                        "\n       Sent Successfully!" + 
                        f"\n     New Balance: P{self.__current_balance:.2f}\n" + "-"*32)


