# linear search



def while_search(list: list, element: int) -> str:
    i = 0
    while i < len(list):  # Use the parameter list instead of the global variable ls
        if list[i] == element:
            return f"{element} found"  # Return message when element is found
        i += 1 
    return f"{element} not found"  # Return message when element is not found
def for_search(list: list, element: int) -> str:
    for i in list:
        if i == element:
            return f"{element} found"
    return f"{element} not found"

# Test the function with different elements
ls = [2, 6, 5, 4, 55, 2, 3, 69, 13, 15]
print(while_search(ls, 2))  # Output: "2 found"
print(while_search(ls, 10))  # Output: "10 not found"

print(for_search(ls, 2))  # Output: "2 found"
print(for_search(ls, 10))  # Output: "10 not found"


# this method is called 'linear search'
# linear search - for small list
# disadvantage - time consuming
# to overcome this disadvantage we use 'binary search'
