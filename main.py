import os
def cls(): os.system('cls' if os.name == 'nt' else 'clear') # Terminal will be cleared often
cls() #

class Animal:
    def __init__(self, name:str, species:str, age:int, gender:bool):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender # False 0 = male, True 1 = female
# classes
class Zoo:
    def __init__(self, name:str):
        self.name = name
        self.animals = []
    def list_animals(self):
        print("Index | Name, Species, Age, Gender\n")
        for i in range(len(self.animals)):
            printAnimal(self.animals[i], i)
    def add_animal(self, animal:Animal):
        self.animals.append(animal)
    def remove_animal(self, animal:Animal):
        if animal in self.animals: self.animals.remove(animal)
        else: print("Animal not found")

zoo = Zoo(str(input("Insert name for zoo: ")))

def printAnimal(animal:Animal, index:int=-1):
    print((str(index)+" | "if index >= 0 else "")
          +animal.name+", "+animal.species
          +", "+str(animal.age)
          +", "+("Female" if animal.gender else "Male"))

running = True
while running:
    cls()
    print("Welcome to " + zoo.name + "!\n")
    print("1. List animals\n2. Add animals\n3. Remove animals\n4. Leave zoo\n")
    choice = int(input("Choice: "))
    match choice:
        case 1: 
            cls()
            if len(zoo.animals) != 0:
                zoo.list_animals()
                input("\nPress enter to return")
            else: input("No animals found in database\n\nPress enter to return")
        case 2:
            cls()
            print("Adding new animal to zoo\n")

            name = input("Animal name: ")
            species = input("Animal species: ")
            while True:
                try: age = int(input("Animal age: ")); break
                except ValueError: # User did not input age as int
                    # \033[A sets cursor back to age, \033[K clears the line
                    print("\033[A\033[K", end="")
            gender = input("Animal gender (m/f): ").lower().startswith('f')
            addedAnimal = Animal(name, species, age, gender)

            cls()
            printAnimal(addedAnimal)
            if input("\nDo you want this animal to be added to " 
                     + zoo.name 
                     + "? (y/n): ").lower().startswith("y"): zoo.add_animal(addedAnimal)
        case 3:
            if len(zoo.animals) == 0:
                cls()
                input("No animals found in database\n\nPress enter to return")
            else:
                while True:
                    cls()
                    zoo.list_animals()
                    print("\nGive the index of the animal you wish to remove.")
                    deletedAnimal = input("Alternatively, type the letter R to return to the menu: ")
                    if deletedAnimal.lower().startswith("r"): break
                    else:
                        try: 
                            index = int(deletedAnimal)
                            try:
                                cls()
                                if input("Do you really want to remove the " 
                                        + zoo.animals[index].species
                                        + " named "
                                        + zoo.animals[index].name 
                                        + "? (y/n): ").lower().startswith("y"):
                                    zoo.remove_animal(zoo.animals[index]); break
                            except IndexError: pass # Index was out of range
                        except ValueError: pass # Input was not an index
        case 4: 
            cls()
            running = False