''' 
zip() - combines multiplle iterable  into iterator of tuples . zip returns an iterator. 
so you have to convert it to a list or another collection type 

we can also unzip

'''
list1 = [1, 2, 3]
list2 = ['a', 'b']

zipped = zip(list1, list2)  #returns iterator object. so convert
print(zipped)  # <zip object at 0x7dcc79a23600>
print(list(zipped))  # Only pairs (1, 'a') and (2, 'b')    



unzipped = [(1, 'a'), (2, 'b')]  # this should not be an zip object
list1, list2 = list(unzipped)
print(list1,list2)  # (1, 'a') (2, 'b')
