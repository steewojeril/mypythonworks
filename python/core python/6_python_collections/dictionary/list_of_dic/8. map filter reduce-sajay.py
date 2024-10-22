frameworks=[
    {"fw_name":"dhango","language":"python","rating":4},
    {"fw_name":"flask","language":"python","rating":4},
    {"fw_name":"oodo","language":"python","rating":4},
    {"fw_name":"express","language":"javascript","rating":5},
    {"fw_name":"wordpress","language":"php","rating":3}
]
# print all fw_name ==> map
# print all rating ==>map

# condition varumbol filter
# print all fw_name hsving language python ==> filter


# 1. print all fw_name ==> map
fw_name=[i["fw_name"] for i in frameworks]
print(fw_name)

# 2. print all rating ==>map
print([i["rating"] for i in frameworks])

# 3. print python fw_name ==> filter
print([i["fw_name"] for i in frameworks if i["language"]=="python"])

# 4. print all fw_name having rating >4 ==> filter
print([i["fw_name"] for i in frameworks if i["rating"]>4])

# 5. sort frameworks based on rating
# sorted()
# frameworks.sort
# 2 um same aanu

# eth key vachaanu sort cheyyandath enn paranj kodukkanam
# sort enna fn nte akath 2 argument und(*arg(tuple),**arg(dic)) (ctrl+click on sort fn)

# ascending
# refer lambda in functional programming
# variable_name = lambda arguments:return

# key kk atkath paranj kodukkendath ==> ee framework nakath eth key vachaanu ee functionality apply cheyyendath
frameworks.sort(key=lambda fw:fw["rating"]) #( frameworks lthe oro fw aanu input aayi varunnath aa fw nte rating aanu return cheyyendath)
print(frameworks)
# descending
frameworks.sort(key=lambda fw:fw["rating"],reverse=True)
print(frameworks)

# 6. print highest rating fw
print(max(frameworks,key=lambda fw:fw["rating"]))

# 7. print lowest rating fw
minimum=(min(frameworks,key=lambda fw:fw["rating"])) # fw having low rating
print(minimum["rating"]) # lowest rating
