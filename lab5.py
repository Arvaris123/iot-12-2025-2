from enum import Enum

class Kind(Enum):
    DOG = "dog"
    CAT = "cat"
    BIRD = "bird"
    OTHER = "other"

class Pet:
    
    def __init__(self, name: str = "", breed: str = "", age: float = 0.0, greeting: str = "", mass: float = 0.0, kind: Kind = Kind.OTHER):
        self.__name = name
        self.__breed = breed
        self.__age = age
        self.__greeting = greeting
        self.__mass = mass
        self.__kind = kind

    def get_name(self):
        return self.__name

    def get_breed(self):
        return self.__breed

    def get_age(self):
        return self.__age

    def get_greeting(self):
        return self.__greeting

    def get_mass(self):
        return self.__mass

    def get_kind(self):
        return self.__kind

    def is_polite(self) -> bool:
        return "hello" in self.__greeting.lower()

    def __str__(self):
        return f"{self.__name} ({self.__age} y, {self.__kind.name})"
    
class Home:
    
    def __init__(self):
        self.__pets: list[Pet] = [] 
    
    def add_pet(self, pet: Pet):
        self.__pets.append(pet)  
    
    def get_pets(self) -> list[Pet]:
        return self.__pets  

    def sort_by_age(self):
        n = len(self.__pets)
        for i in range(n):
            for j in range(0, n - 1 - i):
                if self.__pets[j].get_age() > self.__pets[j + 1].get_age():
                    self.__pets[j], self.__pets[j + 1] = self.__pets[j + 1], self.__pets[j]  

    def are_friends(self):
        friends: list[tuple[Pet, Pet]] = []   
        n = len(self.__pets)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(self.__pets[i].get_age() - self.__pets[j].get_age()) < 2:
                    friends.append((self.__pets[i], self.__pets[j]))
        return friends  

def main():
    p1 = Pet("Rex", "Labrador", 3, "Hello, friend!", 25.0, Kind.DOG)
    p2 = Pet("Murka", "British", 2, "Meow", 4.5, Kind.CAT)
    p3 = Pet("Kesha", "Parrot", 6, "Hello human!", 0.5, Kind.BIRD)

    home = Home()
    home.add_pet(p1)   
    home.add_pet(p2)
    home.add_pet(p3)
    
    home.sort_by_age()  
    print("Pets by age:")
    for p in home.get_pets():  
        print(" ", p)

    for a, b in home.are_friends():  
        print(f" {a.get_name()} and ️ {b.get_name()}")

    print("\nIs", p1.get_name(), "polite?", p1.is_polite())  
    print("\nIs", p2.get_name(), "polite?", p2.is_polite())
    print("\nIs", p3.get_name(), "polite?", p3.is_polite())
if __name__ == "__main__":
    main()

