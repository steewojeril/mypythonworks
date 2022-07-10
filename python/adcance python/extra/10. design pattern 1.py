# eth order call cheythaalum highest number il ninnu venam lowest number operate(div and sub) cheyyendath
# ithaanu nammade problem
# so 2 place lum nammal same sathanam(if n1>n2, else) use cheyyende?
def sub(n1,n2):
    if n1>n2:
        return n1-n2
    else:
        return n2-n1
def div(n1,n2):
    if n1>n2:
        return n1/n2
    else:
        return n2/n1

# here we violated DRY rule
# DRY :do not repeat yourself (code ne repeat cheyyan padilla)
print(sub())
print(div())

# athpole thanne
# suppose 3 classes
# here also something is repeating
class ProductListView:
    # if user is logged in
class AddToCartView:
    # if user is logged in
class OrderView:
    # if user is logged in

# so inganathe oru common problem varumbol athine solve cheyyan oru decorator function ezhthanam
# refer to next pyhton file