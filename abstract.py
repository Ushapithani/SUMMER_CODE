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

