# continue >>> condition will skip and controll will go to loop itself(in break it will exit from loop)

for i in range(1,51):  #1,2,3,.........23,24   25 will not be printed ), 26,......50
    if(i==25):
        continue
    print(i)

i=1
while i<=50:
    if i==25:
        continue
    print(i)
    i+=1