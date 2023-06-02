# to round a digit to 2 decimal points
# there is round fn:
# round(numer,no_of_digits)
# but it eliminates 0s after decimal
# eg:2  output>>2
# eg :2.40   >> 2.4
a=2
print(round(a,2))

# effective method  using decimal module

# import Decimal fun from decimal module
from decimal import Decimal

n=12
dec_nmuber=Decimal(n)    #making n to decimal object
rounding=dec_nmuber.quantize(Decimal('0.00'))   #quarantize is a mtd of Decimal object
print(rounding)