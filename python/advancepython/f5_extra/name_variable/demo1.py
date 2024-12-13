# NOTE :__main__  means starting point of execution(like in c++,java)

print("demo1 says : ",__name__)  # output : if we execute this particular file , it gives __main__ .(because this is the starting point when run this file right?)

# if we are importing this file in another module ,it gives name of this file ie 'demo1'


'''
USECASE example:
simple use case: if we want to execute a part of code only when execute this particular file ( not when this is imported ) 
'''
def run_only_if_exceute_from_current_file():
    print("executed from demo1")


if __name__ == '__main__':
    run_only_if_exceute_from_current_file()
