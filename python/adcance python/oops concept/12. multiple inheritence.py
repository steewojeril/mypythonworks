# class person << name age
# class parent << place phone
# class employ id des salary

# print  name age place phone id des salary


# like 'self' , 'this' is an instance keyword .vere eth key word koduthalum ith work aakum
class Person:
    def setperson(this,name,age):
        this.name=name
        this.age=age
class Parent:
    def setparent(this,place,phone):
        this.place=place
        this.phone=phone
class Employ(Person,Parent):
    def setemploy(this,id,des,salary):
        this.id=id
        this.des=des
        this.salary=salary
    def printemploy(this):
        print(this.name, this.age, this.place, this.phone,this.id,this.des,this.salary) # if we not give this salary << no problem

emp=Employ()
emp.setperson('steewo',24)
emp.setparent('marathakkara',9567144225)
emp.setemploy(100,'web developer',100000)
emp.printemploy()