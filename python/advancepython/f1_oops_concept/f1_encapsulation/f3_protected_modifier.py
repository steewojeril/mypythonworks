# protected_modifier.py

class Animal:
    def __init__(self, species):
        self._species = species  # protected attribute

    def _speak(self):  # protected method
        print(f"{self._species} makes a sound.")

class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed

    def dog_info(self):
        print(f"{self._species} is a type of {self.breed} breed.")

# Example of protected access:
dog = Dog("Dog", "Golden Retriever")
dog.dog_info()  # Accessing protected method within subclass
print(dog._species)  # This works but it is discouraged (protected variable)
