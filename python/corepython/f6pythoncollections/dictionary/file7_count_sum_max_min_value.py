dic={"a":1,"b":2,"c":3}


# to get keys only (literable object)
print(dic.keys())
# to get values only (literable object)
print(dic.values())
# to get dic as literable object  [('k1',v1),('k',v2),('k3',v3)]
print(dic.items())

# ................................................
# sorting
# based on key
dic={'a':5,'c':2,'b':66}
sorted_key=dict(sorted(dic.items()))
print(sorted_key)
# based on value
sorted_value=dict(sorted(dic.items(),key=lambda i : i[1]))
print(sorted_value)
# ...............................................
# WORD COUNT  (short method)
# to print count of key provided from a dic  
test_string="cat dog cat rabbit tiger elephant turtle"
ls=test_string.split(' ')                   #['cat', 'dog', 'rabbit', 'tiger', 'elephant', 'turtle']
a={animals: ls.count(animals) for animals in ls}
print(a)        #{'cat': 1, 'dog': 1, 'rabbit': 1, 'tiger': 1, 'elephant': 1, 'turtle': 1}
# ..........................................


# SUM:
# sum of values of dic:
print(sum(dic.values()))
# ...................................

# MAX & MIN

# return key having max value from dic:
'''
dic.get(a) # output : 1
dic.get  # returns key of dic
'''
print('max k',max(dic, key=dic.get))  #key = means we are providing a fn
# return key having min value from dic:
print(min(dic,key=dic.get))

# .................................................

# return max value from dic:
print(max(dic.values()))
# return min value from dic:
print(min(dic.values()))

# ......................................................

# to merge dictionaries
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
prices = {'apple': 1.2, 'banana': 0.5, 'cherry': 2.5}
country_codes = {'USA': 1, 'India': 91, 'UK': 44}

merged_dic={**scores,**prices,**country_codes}
print(merged_dic)
# .........................................
name_list=['steewo','eby']
info={'batch':'april','year':2005}
res=dict.fromkeys(name_list,info)
print(res)

