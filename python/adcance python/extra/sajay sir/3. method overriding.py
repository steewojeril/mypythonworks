# child nu : parent nte properties venam("gold":"2kg","car":"ertiga") + child nte properties venam ("bike":"royal enfield")

# self : to point current instance
# super : to point parent(parent class ne refer cheyyan)


class  Parent:
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