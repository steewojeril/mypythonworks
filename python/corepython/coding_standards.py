'''
    # Naming Conventions
var & fns : snake_case(lowercase words separated by underscores)
constants : UPPER_SNAKE_CASE()
class     : CamelCase (capitalized words without underscores).

'''
# .............................
    # Use Type Hint

def add(a: int, b: int) -> int:  # -> return type hint
    return a + b

# .............................
    # Avoid magic numbers

# Correct:
TAX_RATE = 0.15
price_with_tax = price * (1 + TAX_RATE)

# Incorrect:
price_with_tax = price * 1.15  # What is 1.15? It should be a constant like TAX_RATE
# .............................
    # Avoiding Global Variables  
  
# Correct (passing arguments to functions):
def calculate_area(radius: float) -> float:
    return 3.14 * radius ** 2

# Incorrect (using global variables):
radius = 5
def calculate_area():
    return 3.14 * radius ** 2
