from blog.models import users,posts
def authentication(**kwargs): # checking the entered credentials are coorrect
    username=kwargs.get("username")
    email=kwargs.get("email")
    user_data=[user for user in users if user["username"]==username and user["email"]==email]
    return user_data
# user=authentication("Bret","Sincere@april.biz") #here namukk ariyilla nthaanu nammal pass cheyyunnath enn. so nammal dictionary pole pass cheyyum . athinu **kwargs venam. refer views in ecommerse
# if user: # means if any value is there in user
#     print(user)
# else:
#     print("invalid credentials")

    # get: to retrieve data
    # post: to create data
    # put/patch : to uedit
    # del  : to delete
# actually authentication already django il ind nammuk ath eduth use cheythal mathi

# ini muthal oru class in oru function mathram koduthal mathi(suppose login and log out , login oru class il kodukkaanam logout vere class il kodukkanam)
# ith oru rule aanu.(single responsibility rule)(design pattern(design principle) enna topic il varunnathaanu ithellam)
#loosely coupled aayirikkum angottum ingottum connection undaakilla
# suppose login and logout is in same class, athil ethenkilum orennam failure vannal motham fail akille?

# refer extra << design pattern
def login_required(fn): #login cheythallalle logoout cheyyan pattu. ith koduthillel error kanikkum if user is already logout
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("you must login")
    return wrapper

@login_required
def loged_user(): # to know the userid of user who loged in
    username = session.get("user")
    userId = [user["id"] for user in users if user["username"] == username][0]
    return userId


session={} # log in muthal logout vare  aa alde details store cheyth vekkan vendi aanu ith
class SignInView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        email=kwargs.get("email")
        user=authentication(username=username,email=email)
        if user:
            print("success")
            session["user"]=username
            print(session)
        else:
            print("invalid credentials")



# @login_required
# def logout(*args,**kwargs):
#      session.pop("user")
#
# logout()

class PostListView:
    @login_required
    def get(self,*args,**kwargs):
        return posts

pl=PostListView()
try:
    all_posts=pl.get()
except Exception as e:
    print(e)

class MyPostsView:
    @login_required
    def get(self,*args,**kwargs):
        userId=loged_user()
        qs=[post for post in posts if post["userId"]==userId]
        return qs

class PostCreateView:
    @login_required
    def post(self,*args,**kwargs):
        userId=loged_user()
        title=kwargs.get("title")
        body=kwargs.get("body")
        data={
            "userId":userId,
            "title":title,
            "body":body
        }
        print(data)
        posts.append(data)
        print("post created successfully")

class SpPost:
    @login_required
    def get(self,*args,**kwargs): # to retrieve particular post
        id=kwargs.get("id")
        pos=[post for post in posts if post.get("id")==id]
        return pos
    @login_required
    def put(self,id=None,*args,**kwargs):
        post=[p for p in posts if p.get("id")==id][0]
        title=kwargs.get("title")
        body=kwargs.get("body")
        post["title"]=title
        post["body"]=body
        print(post)


user=SignInView()
user.post(username="Antonette",email="Shanna@melissa.tv")

po=PostCreateView()
po.post(title="new title",body="new body")

mp=MyPostsView()
print(mp.get()[-1])

sp=SpPost()
print(sp.get(id=12))

sp.put(id=13,title="updated title",body="updated body")