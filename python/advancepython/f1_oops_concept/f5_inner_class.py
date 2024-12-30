class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.laptop = self.Laptop()  # Creating an inner class object

    def show(self):
        # Printing student details
        print(f"Student: {self.name}, {self.age}")
        # Calling laptop's show method to display laptop details
        print(self.laptop.show())  # Print the formatted string returned by Laptop.show()

    class Laptop:
        def __init__(self):
            self.brand = input("Enter brand: ")
            self.ram = int(input("Enter RAM capacity: "))

        def show(self):
            # Returning formatted string instead of printing
            return f"Laptop: {self.brand}, RAM: {self.ram}GB"


# Creating a Student object
st = Student("Steewo", 20)
st.show()
# print(st.laptop.show())
