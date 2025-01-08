'''
Errors
3 types 
compile time 
    syntax error : missing, worng spelling
logical 
    compiled but wrong output
run time
    compiled, logically correct , but not working for specific input or run time
    mistake is done by user
    but we should understand what users will mistakes

    error that you dont know 
    except exception as e:
    
issues of errors:
    normal error varumbol user nu manassilavila error enthaanu
    execution stops in between. 

try => try to excecute
except => if there is an error
finally => execute if we get error as well as if we dont get ther error

'''



a = 10
b = 0

try:
    print("Trying to open the process...")
    # Prompt user for input; handle invalid input
    c = int(input("Enter a number: "))  # This may raise a ValueError
    print(a / b)  # This will raise a ZeroDivisionError if b = 0
    # print("closed") # if above statement got error this will not work . bcoz it suddenly goes to except
except ZeroDivisionError as e:
    print("Can't divide by zero:", e)  # Handles division by zero errors
except ValueError as e:
    print("Invalid input. Please enter a valid integer:", e)  # Handles invalid input
except Exception as e:  # This catches all other types of exceptions not covered by the above
    print("Something went wrong:", type(e), e)  # Handle any unexpected error
finally:
    print("closed, execute if we get error as well as if we dont get ther error.")
