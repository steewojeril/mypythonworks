class Students:
    School = "St. Thomas"  # Class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1  # Instance variable
        self.m2 = m2
        self.m3 = m3

    # Instance Method
    def avg(self):  # Calculates average of marks
        return (self.m1 + self.m2 + self.m3) / 3

    def get_marks(self):  # Accessor (Getter) method
        return self.m1, self.m2, self.m3

    def set_marks(self, m1):  # Mutator (Setter) method
        self.m1 = m1

    # Class Method
    @classmethod
    def get_school(cls):  # Operates on the class variable
        return cls.School

    # Static Method
    @staticmethod
    def info():  # General utility function eg:factorial
        print("This is general information about the school.")

# Example Usage
st1 = Students(85, 90, 95)
print(f"Average Marks: {st1.avg()}")  # Instance method
print(f"School Name: {Students.get_school()}")  # Class method
Students.info()  # Static method
