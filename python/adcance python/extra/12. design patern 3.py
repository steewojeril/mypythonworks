# class user [username,role]
# class addcourse[user,course]
# class add batch[user,batchcode,course]
# only admin can add course and batch
# do using decorator

# decorator fun nte akath 2 or 3 arguments enna choice varum . stable aayitt venam kodukkan(2 or 3) thats why we use *arg and **kwarg
def admin_permission(fn):
    def wrapper(*args,**kwargs):
        user=kwargs.get("user") # retrieving current user from kwargs
        if user.role!="admin": # incase of user 1 << ividde user lekk user1(it is an object) varum.
            raise Exception("permission denied")
        fn(*args,**kwargs)
    return wrapper

class User:
    def set_user(self,username,role): # user details
        self.username=username
        self.role=role
    def print_user(self):
        print(self.username,self.role)
class Course:
    @admin_permission
    def set_course(self,*args,**kwargs):
        self.user=kwargs.get("user") #eth user aanu ee course add cheythath ennaruyaan
        self.course=kwargs.get("course")
    def print_course(self):
        print(self.course)
class Batch:
    @admin_permission
    def set_batch(self,*args,**kwargs):
        self.user=kwargs.get("user") # eth user aanu ee batch add cheythath ennaruyaan
        self.course=kwargs.get("course") #eth course ile batch aanu ith ennariyaan
        self.b_code=kwargs.get("b_code")
    def print_batch(self):
        print(self.b_code)
#1
user1=User()
user1.set_user("steewo","admin")

c1=Course()
c1.set_course(user=user1,course="django") # ee course add cheythath user aanu. thats why we gave object admin for course

b1=Batch()
b1.set_batch(user=user1,course=c1,b_code="april django") #django enna course le batch code aanu ith. thats why we gave object c1 for course

user1.print_user()
c1.print_course()
b1.print_batch()

#2
user2=User()
user2.set_user("siva","staff")

c2=Course()
c2.set_course(user=user2,course="ml")

b2=Batch()
b2.set_batch(user=user2,course=c2,b_code="april ml")

user2.print_user()
c2.print_course()
b2.print_batch()