# class bank

# method1 << account creation ,  arguments << name, acc_no. , min_balance
# method3 <<< deposit,   arguments <<amount  , print balance
# method 2 <<withdraw ,  arguments <<amount(name maati kodutholo) ,   print balance amt

# bank_name common

class Bank:
    bname='canara bank'
    def acc_creation(self,name,accno):
        self.name=name
        self.accno=accno
        self.min=5000
        self.total=self.min
    def deposit(self,dep):
        self.dep=dep
        self.total=self.total+self.dep # deposit cheyyumbo total update cheyyanaanu ith kodukkunnath
        print("an amount of INR",self.dep,"has been credited to your",Bank.bname,"account")
        print("Total Available Balance INR",self.total)
    def withdraw(self,wit):
        self.wit=wit
        if self.wit>self.total:
            print("insufficient balance")
        else:
            self.total=self.total-self.wit # withdraw cheyyumbo total update cheyyanaanu ith kodukkunnath
            print("an amount of INR",self.wit,"has been credited to your",Bank.bname,"account")
            print("Total Available Balance INR", self.total)
ob=Bank()
ob.acc_creation("steewo",100)
ob.deposit(2000)
ob.withdraw(2000)