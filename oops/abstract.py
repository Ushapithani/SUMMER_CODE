from abc import ABC, abstractmethod
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
obj.pay(100)


# create a abstract class bank with the properties of amount,balance aount,withdraw amout 
#which includes the child classes as a payment gateway google pay ,phoepay,debit card ,creadit bank and banking
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, method, amount, balance_amount, withdraw_amount):
        pass

class PaymentGateway(Payment):
    def pay(self, method, amount, balance_amount, withdraw_amount):
        match method.lower():
            case "googlepay":
                print(f"Paid {amount} using Google Pay")
            case "phonepe":
                print(f"Paid {amount} using PhonePe")
            case "debitcard":
                print(f"Paid {amount} using Debit Card")
            case "creditcard":
                print(f"Paid {amount} using Credit Card")
            case "banking":
                print(f"Paid {amount} using Banking")
            case _:
                print("Unknown payment method")

        balance_amount += amount
        if withdraw_amount <= balance_amount:
            balance_amount -= withdraw_amount
            print(f"Withdrawn {withdraw_amount} via {method}")
        else:
            print(f"Insufficient balance in {method}")
        print(f"Remaining Balance: {balance_amount}\n")

if __name__ == "__main__":
    gateway = PaymentGateway()

    print("Select payment method:")
    print("1. GooglePay")
    print("2. PhonePe")
    print("3. DebitCard")
    print("4. CreditCard")
    print("5. Banking")

    choice = input("Enter your choice (1-5): ")

    methods = {
        "1": "googlepay",
        "2": "phonepe",
        "3": "debitcard",
        "4": "creditcard",
        "5": "banking"
    }

    method = methods.get(choice, "unknown")

    gateway.pay(method, amount=500, balance_amount=1000, withdraw_amount=300)'''


# create an abstarct base class as an vehicle with the properties of model ,color ,type connected with the child classes 
#two ,three and four wheelers 
'''from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def __init__(self, model, color, type):
        self.model = model
        self.color = color
        self.type = type
class TwoWheeler(Vehicle):
    def __init__(self, model, color, type):
        super().__init__(model, color, type)
class ThreeWheeler(Vehicle):
    def __init__(self, model, color, type):
        super().__init__(model, color, type)
class FourWheeler(Vehicle):
    def __init__(self, model, color, type):
        super().__init__(model, color, type)
two_wheeler = TwoWheeler("Yamaha R15", "Blue", "Two Wheeler")
three_wheeler = ThreeWheeler("Auto Rickshaw", "Yellow", "Three Wheeler")
four_wheeler = FourWheeler("Toyota Camry", "White", "Four Wheeler")
print(f"Two Wheeler: Model={two_wheeler.model}, Color={two_wheeler.color}, Type={two_wheeler.type}")
print(f"Three Wheeler: Model={three_wheeler.model}, Color={three_wheeler.color}, Type={three_wheeler.type}")
print(f"Four Wheeler: Model={four_wheeler.model}, Color={four_wheeler.color}, Type={four_wheeler.type}")