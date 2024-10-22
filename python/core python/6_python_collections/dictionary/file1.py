# 1. how to define
dic={} # empty list

# In dictionary, elements are added as key- value pairs
dic={"roll":101,"name":'vinay',"age":26,"dept":'bigdata',"salary":1000}
print(dic)
# key <<< roll, name, age, dept, salary
# values <<< 101, vinay, 26, bigdata, 1000
# keys are in " " (even the key is an  integer)
# values are in ' ' if string

# 2. hetrogenous data supported or not
# it supports hetrogenous data


# 3. duplicated values is allowed or not
dic1={"roll":101,"age":26,"age":27}
print("dic1=",dic1)
# duplicated keys are not supported

dic2={"roll":101,"name":'vinay',"mark":26,"age":26}
print("dic2=",dic2)
# duplicated values are supported




# 4. insertion order is preserved or not
# insertion order is preserved(output order is same as that of input)

# 5. mutable or imutable (updation of data)
# dictionary is mutable
