#list
results = [
    {"district":"tvm","win": 98, "A+": 45000},
    {"district":"ktm","win": 95, "A+": 44000},
    {"district":"apy","win": 97, "A+": 47000},
    {"district":"idk","win": 90 ,"A+": 38000},
    {"district":"ekm","win": 99, "A+": 56000},
    {"district":"pta","win": 99, "A+": 58000},
    {"district":"tsr","win": 98, "A+": 57000},
    {"district":"kzd","win": 99, "A+": 58000},
    {"district":"pkd","win" :95, "A+": 50000},
    {"district":"mpm","win": 90,"A+": 4500},

]

# 1. win % of tvm
# 2. district with highest win %
# 3. district with lowest win %
# 4. district with highest full A+
# 5. district with lowest full A+
# 6. total no of A+
# 7. total win %
# 8. sort districts with resp to win% (acsending)

# 1. win % of tvm
for i in results:
    if i["district"]=="tvm":
        print(i["win"])
# using lis comprehension
tvm_win=[i["win"] for i in results if i["district"]=="tvm"]
print(tvm_win)
# or
# print([result["win"] for result in results if result["district"]=="tvm"])

# 2. district with highest win %
print(max(results,key=lambda res:res["win"]))

# 3. district with lowest win %
print(min(results,key=lambda res:res["win"]))

# 4. district with highest full A+
print(max(results,key=lambda res:res["A+"]))

# 5. district with lowest full A+
print(min(results,key=lambda res:res["A+"]))

# 6. total no of A+
dis_aplus=sum([i["A+"] for i in results])
print(dis_aplus)



# 7. total win %
win=[i["win"] for i in results]
total_win=(sum(win)/1000)*100
print("total win percentage :",total_win)

# 8. sort districts with resp to win% (acsending)
results.sort(key=lambda res:res["win"])
print(results)

# 9. sort districts with resp to win% (descending)
results.sort(reverse=True,key=lambda res:res["win"])
print(results)