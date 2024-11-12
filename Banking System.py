# Banking system using python OOPs concept
from contextlib import closing


class banking:
    #MAKING THE HOLDER PRIVATE
    __holders = {}

    def __init__(self, name: str, amount: int):
        self.name = name.lower()
        self.amount = amount
        banking.__holders[name.lower()] = [amount]
        print(f'Hello {name.upper()},\nYour account has been created successfully.\nYour current balance is {amount}')

    def adding(self, amount: int):
        if self.name.lower() not in banking.__holders:
            print('No such account holder exist.\nPlease enter correct name')

        banking.__holders[self.name.lower()].append(amount)
        print(
            f'Successfully Added {amount} to {self.name.upper()}\'s account.\nNew balance is {sum(banking.__holders[self.name.lower()])} amount')

    def withdraw(self, amount: int):
        condition = sum(banking.__holders[self.name.lower()])
        if amount > condition:
            difference = sum(banking.__holders[self.name.lower()]) - amount
            print('Not enough funds available to withdraw.\nShortfall of Rs.' + str(difference))

        if self.name.lower() not in banking.__holders:
            print('No such account holder exist.\nPlease enter correct name')

        if self.name.lower() in banking.__holders and amount <= condition:
            banking.__holders[self.name.lower()].append(-amount)
            print(
                f'Successfully deducted {amount} from {self.name.upper()}\'s account.\nNew balance is {sum(banking.__holders[self.name.lower()])}')

    def transactions(self):
        if self.name not in banking.__holders:
            print('No such account holder exist.\nPlease enter correct name')
        else:
            values = banking.__holders[self.name]
            print('Transactions for the account holder ' + self.name.upper() + ' is below.\n' + str(values))

    def transfer(self, r_name: str, amount: int):
        self.r_name = r_name.lower()
        self.amount = amount
        if self.r_name not in banking.__holders:
            print('No such account holder exist.\nPlease enter correct name')
        else:
            banking.__holders[self.r_name].append(amount)
            banking.__holders[self.name].append(-amount)
            print('Successfully Transfered amount ' + str(
                amount) + ' to ' + r_name + '\'s account.\nYour new balance is ' + str(sum(banking.__holders[self.name])))
#CREATING A PRIVATE FUNCTION FOR CHECKING THE NUMBER OF OWNERS AND TOTAL MONEY DEPOSIT IN BANK
    def __holder_information(self):
        owners = list(banking.__holders.keys())
        number = len(owners)
        money = sum(banking.__holders.values())
        print(owners)
        print(number)
        print(money)

    def closing(self):
        if self.name not in banking.__holders:
            print('No such account holder exist.\nPlease enter correct name')
        else:
            print("Thank you for being a part of our banking service.\nPlease college your amount Rs." + str(sum(banking.__holders[self.name])) + ' from the counter')
            banking.__holders.pop(self.name)

aditya = banking('aditya', 5000)
harshita = banking('Harshita', 5000)
aditya.adding(200)
aditya.withdraw(200)
aditya.withdraw(20000)
aditya.transactions()
aditya.transfer('harshita', 550)
aditya.transfer('bhaloo', 550)
aditya.transactions()
harshita.transactions()
harshita.closing()
# print(aditya.__holders)
# aditya.__holder_information()

