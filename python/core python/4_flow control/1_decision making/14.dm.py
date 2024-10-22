# Accept any city from the user and display monument of that city.
#                   City                                 Monument
#                   Delhi                               Red Fort
#                   Agra                                Taj Mahal
#                   Jaipur                              Jal Mahal

city=input("enter the city") #default data type of input is string
if(city=='delhi'):
    print("Red Fort")
elif(city=='agra'):
    print("Taj Mahal")
elif (city=='jaipur'):
    print("Jal Mahal")
else:
    print("invalid")