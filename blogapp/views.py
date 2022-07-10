from blogapp.models import users,posts
#1
def authenticate(**kwargs): # to return data of loged user
    username=kwargs.get("username")
    password=kwargs.get("password")
    user=[user for user in users if user["username"]==username and user["password"]==password]
    return user



session={}

#iniyulla nth karyam cheyyanamenkilum user login cheythirikkanam. so ellathinteyum akath if user in session , else "you must login" ith kodukkanam
# so athinte repeatation ozhivakkan aanu decorator use cheyyunnath
# attribute nu alla decorator kodukkandath.(means post id check cheyth post edukkanna function repeat cheyyunnu enn karuthi athinu decorator use cheyyilla)
# functionality kkanu decorator kodukkanath(user admin aano normal user aano, user login cheythittundo)
def signin_required(fn):
    def wrapper(*args,**kwargs):# decorate cheyyenda functions nte no. of arguments aanu ivide kodukkanadath. ith oru pole aavan vendi aanu nammal  ella function lum *args **kwargs koduthath
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("you must login")
    return wrapper

#2
class SignInView: #just sucess aano invalid aano nn just print cheyyan vendi and also to add userr to the session(dictionary)
    def post(self,*args,**kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        user=authenticate(username=username,password=password) # format of user
        if user:
            session["user"]=user[0] # user==> [{}] , user[0]==> {}
            print("success")
        else:
            print("invalid")

#3
class PostsView:
    @signin_required
    def get(self,*args,**kwargs):
        return posts

    @signin_required
    def post(self,*args,**kwargs):
        userId=session["user"]["id"]
        kwargs["userId"]=userId
        posts.append(kwargs)
        print(posts)

#4
class MyPostListView:
    @signin_required
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        my_posts=[post for post in posts if post["userId"]==userId]
        return my_posts



#5
class PostDetailsView: # retrieve del edit
    #6

    def get_object(self,id): #pass cheyyunna id de post edukkan.
        post=[post for post in posts if post["postId"]==id][0] #[0] koduthillel error varum bcoz list ayittanu ivide kidakkunnath [{}] bcoz of list comprehension. athine ingane {} aakanam ennale kalayan patuu
        return post

    @signin_required
    def get(self,*args,**kwargs): #particular pos kittan
        post_id=kwargs.get("postId")
        post=self.get_object(post_id)
        return post

    @signin_required
    def delete(self,*args,**kwargs):
        postId=kwargs.get("postId")
        data=self.get_object(postId)
        if data:
            posts.remove(data)
            print("post removed")
            print(len(posts))

    @signin_required
    def put(self,*args,**kwargs):
        postId=kwargs.get("postId")
        instance=kwargs.get("data")
        data=self.get_object(postId)
        if instance:
            data.update(instance)
            print(data)

class LikeViews: # to add like to post by logged user
    @signin_required
    def get(self,*args,**kwargs): #get or post eth venelum vakkam. onnum post cheyyann illatha karanam get
        userId=session.get("user")["id"]
        postId=kwargs.get("postId")
        post=[post for post in posts if post["postId"]==postId][0]
        if post:
            post["liked_by"].append(userId)
            print(post)


# cheriya functionality okke class il ezhuthanam ennilla
@signin_required
def signout(*args,**kwargs): #*args **kwargs koduthaale ithine decorate cheyyan pattullu
    user=session.pop("user") # pop =key value pair ne remove cheyyum,nammal aa remove cheyytha value ne user lot save cheyth vachirikkunnu enn mathram
    print(f"{user['username']} logged out")




# print(session)

# data=PostsView()
# print(data.get())
# data.post(postId=9,
#          title="new title",
#          content="new content",
#          liked_by=[]) # post itta vasham aarum like cheyyillallo, thats why empty list

log=SignInView()
log.post(username="anu",password="Password@123")

mp=MyPostListView()
print(mp.get())

post_details=PostDetailsView()
post_details.delete(postId=6)
print(post_details.get(postId=3))
data={
    "title":"updated title"
}
post_details.put(postId=4,data=data)

like=LikeViews()
like.get(postId=1)

signout()