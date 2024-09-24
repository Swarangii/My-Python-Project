class account:
  def __init__(self,bal,acc):
    self.balance = bal
    self.acc = acc
  def debit(self,withdraw):
    self.balance -= withdraw
    print(f"Your account {self.acc} is Debited with Rs.{withdraw}")
    print(f"Your Total Bank Balance of Acc No. {self.acc} is now Rs.{self.get_balance()}")
  def credit(self,deposite):
    self.balance += deposite
    print(f"Your account {self.acc} is credited with Rs.{deposite}")
    print(f"Your Total Bank Balance of Acc No. {self.acc} is now Rs.{self.get_balance()}")
  def get_balance(self):
    return self.balance
s1 = account(10000000000, 987665443134)
s1.debit(5000000) 
s1.credit(10000000000) 
s1.get_balance()