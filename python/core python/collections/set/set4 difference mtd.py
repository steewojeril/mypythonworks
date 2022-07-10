all_students=["arun","anu","midhun","alwin","manu","aravind","ram", "kiran"]
passed_students=["arun","alwin","aravind","anu"]
# there is no difference mtd inside list class
# but there is difference mtd inside set class
failed_students=set(all_students)-set(passed_students)
print(failed_students)
failed_students.remove("ram")
print(failed_students)