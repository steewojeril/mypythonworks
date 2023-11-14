import pymysql
n=int(input("enter number of inputs"))
conn=pymysql.connect(host="localhost",user="root",password="admin@123",database="Luminar")
cur=conn.cursor()
for i in range(1,n+1):
    a=int(input("enter a"))
    b=int(input("enter b"))
    print(a,b,"ddd")
    cur.execute(f'insert into custom (a,v) values({a},{b})')
cur.execute('select * from custom')
print(cur.fetchall())
cur.close()
conn.close()