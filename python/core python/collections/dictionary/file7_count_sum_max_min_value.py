dic={"a":1,"b":2,"c":3}


# to get keys only (will get as list)
print(dic.keys())
# to get values only (will get as list)
print(dic.values())

# WORD COUNT  (short method)
# to print count of key provided from a dic  
test_string="cat dog cat rabbit tiger elephant turtle"
words_list=test_string.split(' ')                   #['cat', 'dog', 'rabbit', 'tiger', 'elephant', 'turtle']
a={animals: words_list.count(animals) for animals in words_list}
print(a)        #{'cat': 1, 'dog': 1, 'rabbit': 1, 'tiger': 1, 'elephant': 1, 'turtle': 1}



# SUM:
# sum of values of dic:
print(sum(dic.values()))

# MAX AND MIN
# key having max value from dic:
print(max(dic, key=dic.get))
# key having min value from dic:
print(min(dic,key=dic.get))
    # max value from dic:
print(max(dic.values()))
    # min value from dic:
print(min(dic.values()))
