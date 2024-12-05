# super() : child implimentation + parent implementation venamenkil

# child nu : parent nte properties venam("gold":"2kg","car":"ertiga") + child nte properties venam ("bike":"royal enfield")

# self : to point current instance
# super : to point parent(parent class ne refer cheyyan)


class Parent:
    def properties(self):
        self.props={"gold":"2kg","car":"ertiga"}
        return self.props
    def car(self):
        print("ertiga")

class Child(Parent):
    def properties(self):
        props = super().properties()  # super nn koduthal parent lekk povum, then aviduthe properties venam. ithella, 'prop' il und(dict aayi)
        props["bike"]="royal enfield"
        return props
p=Parent()
print(p.properties())

ch=Child()
print(ch.properties())

# example: 2
class Ide:
    def functionalities(self):
        funcs=["create file","rename","delete"]
        return funcs
class Pycharm(Ide):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("execute")
        funcs.append("debug")
        return funcs

py=Pycharm()
print(py.functionalities())

