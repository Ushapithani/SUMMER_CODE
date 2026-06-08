'''from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self ,amount):
        prnt("paid" ,amount,"using google pay")
        pass
class GooglePay(Payment):
    def pay(self, amount):  
        print("paid", amount, "using google pay")
        pass
obj= GooglePay()
obj.pay(100)'''


# create a abstract class bank with the properties of amount,balance aount,withdraw amout 
#which includes the child classes as a payment gateway google pay ,phoepay,debit card ,creadit bank and banking

from abc import ABC, abstractmethod

# Abstract class
class Payment(ABC):
    @abstractmethod
    def pay(self, amount, balance_amount, withdraw_amount):
        pass

# Child classes
class GooglePay(Payment):
    def pay(self, amount, balance_amount, withdraw_amount):
        print(f"Paid {amount} using Google Pay")
        balance_amount += amount
        if withdraw_amount <= balance_amount:
            balance_amount -= withdraw_amount
            print(f"Withdrawn {withdraw_amount} via Google Pay")
        else:
            print("Insufficient balance in Google Pay")
        print(f"Remaining Balance: {balance_amount}\n")

class PhonePe(Payment):
    def pay(self, amount, balance_amount, withdraw_amount):
        print(f"Paid {amount} using PhonePe")
        balance_amount += amount
        if withdraw_amount <= balance_amount:
            balance_amount -= withdraw_amount
            print(f"Withdrawn {withdraw_amount} via PhonePe")
        else:
            print("Insufficient balance in PhonePe")
        print(f"Remaining Balance: {balance_amount}\n")

class DebitCard(Payment):
    def pay(self, amount, balance_amount, withdraw_amount):
        print(f"Paid {amount} using Debit Card")
        balance_amount += amount
        if withdraw_amount <= balance_amount:
            balance_amount -= withdraw_amount
            print(f"Withdrawn {withdraw_amount} via Debit Card")
        else:
            print("Insufficient balance in Debit Card")
        print(f"Remaining Balance: {balance_amount}\n")

class CreditCard(Payment):
    def pay(self, amount, balance_amount, withdraw_amount):
        print(f"Paid {amount} using Credit Card")
        balance_amount += amount
        balance_amount -= withdraw_amount
        print(f"Withdrawn {withdraw_amount} via Credit Card")
        print(f"Remaining Balance: {balance_amount}\n")

class Banking(Payment):
    def pay(self, amount, balance_amount, withdraw_amount):
        print(f"Paid {amount} using Banking")
        balance_amount += amount
        if withdraw_amount <= balance_amount:
            balance_amount -= withdraw_amount
            print(f"Withdrawn {withdraw_amount} via Banking")
        else:
            print("Insufficient balance in Banking")
        print(f"Remaining Balance: {balance_amount}\n")

if __name__ == "__main__":
    gpay = GooglePay()
    gpay.pay(500, 1000, 300)

    phonepe = PhonePe()
    phonepe.pay(200, 500, 800)

    credit = CreditCard()
    credit.pay(1000, 1000, 1500)
