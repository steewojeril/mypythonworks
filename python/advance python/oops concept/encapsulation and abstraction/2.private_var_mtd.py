# public protected private 

# private : var/mtds can access only inside the class(public mtd loode  access cheyyam ennathaanu ithkond udheshikkunnath), cant access outside the class
# (means direct aayi inherited class nte akathum(self.__var) and outside cls (object.__var ennum paranjaccess cheyyanum pattilla)

# but through public mtd and through name mangling we can access it outside the class
# public mtd refers to : evedeyaano private var declare cheythittullath ullath , aviduthe public mtd
# inherited cls le public function vazhi pattilla
class Person:
    def __init__(self):
        self.name="steewo" #public
        self._bank="canara bank"  #protected
        self.__pin=1234   #private
    def printp(self):
        print("inside person")
        print(self.name)
        print(self._bank)
        print(self.__pin)  #ee cls  i evede venelum access cheyyam.but if it is in private mtd it is not accessible
class Employee(Person):
    def __init__(self):
        Person.__init__(self) # employee nte obj create cheyyumbo thanne parent inte init execute aakan vendi. illenil athint obj create cheyyandi varum
    def printe(self):
        print("inside employ")
        print(self.name)
        print(self._bank)

        #accessing private var outside the cls(inherited cls) through public mtd (printp)
        super().printp() #explicitly calls the method from the parent class (Person) regardless of any overrides 
        self.printp() # calls the method from the current class (Employee), 
        # here there is no difference between super. and self.
        # suppose ivide printp override cheyyindel
        # super. >>parent thanne call aakuum
        # self.  >>latest aayirikkum call aavuka 

        # print(self.__pin)  #error: cant acces here  (not access outside the cls(here inherited cls))

p1=Person()
print(p1.name)  
print(p1._bank)  
p1.printp() #  accessing private var through public mtd outside the cls
# print(p1.__pin)  # error: will not work bcoz private var cannot be accessed outside the class
e1=Employee()
e1.printp()  #  accessing private var through public mtd outside the cls
e1.printe() # error: if try to self.__pin  else no error (inherit cls nte akathe public mtd loode access pattilla)