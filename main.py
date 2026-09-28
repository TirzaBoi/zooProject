import os
import sqlite3
def cls(): os.system('cls' if os.name == 'nt' else 'clear') # Terminal will be cleared often
cls() #

# sqlite setup
db = sqlite3.connect("zoo.db") # Connect to the database, creates file if it doesn't exist yet 
cursor = db.cursor() # Cursor to operate the database with

# Init database tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS animals (
        name CHAR,
        species CHAR,
        age INT,
        gender INT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS zoo (
        name CHAR
    )
""")

db.commit()

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
        """Prints all animals found in animals list/database"""
        print("Index | Name, Species, Age, Gender\n")
        for i in range(len(self.animals)):
            printAnimal(self.animals[i], i)
    def add_animal(self, animal:Animal):
        """Add an animal to the animals list and store it in the animals database"""
        self.animals.append(animal)

        cursor.execute("""
            INSERT INTO animals (name, species, age, gender)
            VALUES (?, ?, ?, ?)
        """, (animal.name, animal.species, animal.age, animal.gender))
        db.commit()
    def remove_animal(self, animal:Animal):
        """Delete specific animal from animals list and database"""
        if animal in self.animals:
            cursor.execute("""
                DELETE FROM animals
                WHERE name = ? AND species = ? AND age = ? AND gender = ? 
                LIMIT 1
            """, (animal.name, animal.species, animal.age, animal.gender))
            db.commit()
            self.animals.remove(animal)
        else: print("Animal not found")

# Load the zoos name
cursor.execute("SELECT name FROM zoo")
zooName = cursor.fetchone()
if zooName == None: # If the zoo isn't named yet
    zoo = Zoo(str(input("Insert name for zoo: ")))
    cursor.execute("""
        INSERT INTO zoo (name) VALUES (?)""", (zoo.name,))
    db.commit()
else: # If a name was loaded
    zoo = Zoo(zooName[0])

# Load animals from database
cursor.execute("SELECT name, species, age, gender FROM animals")
animals = cursor.fetchall()
for i in animals: # Add loaded animals to animals list
    zoo.animals.append(Animal(i[0], i[1], i[2], i[3]))

def printAnimal(animal:Animal, index:int=-1):
    """Prints a single specified animal"""
    print((str(index)+" | "if index >= 0 else "")
          +animal.name+", "+animal.species
          +", "+str(animal.age)
          +", "+("Female" if animal.gender else "Male"))

# Main loop
RUNNING = True
while RUNNING:
    # Menu print
    cls()
    print("Welcome to " + zoo.name + "!\n")
    print("1. List animals\n2. Add animal\n3. Remove animal\n4. Leave zoo\n")
    # User input
    choice = 0
    try: choice = int(input("Choice: "))
    except: pass

    match choice:
        case 1:  # List animals
            cls()
            if len(zoo.animals) != 0:
                zoo.list_animals()
                input("\nPress enter to return")
            else: input("No animals found in database\n\nPress enter to return")
        case 2: # Add animal
            cls()
            print("Adding new animal to zoo\n")

            name = input("Animal name: ")
            species = input("Animal species: ")
            while True:
                try: age = int(input("Animal age: ")); break
                except ValueError: # User did not input age as int
                    # \033[A sets terminal cursor back to the age line, \033[K clears it
                    print("\033[A\033[K", end="")
            gender = input("Animal gender (m/f): ").lower().startswith('f')
            addedAnimal = Animal(name, species, age, gender)

            cls()
            printAnimal(addedAnimal)
            if input("\nDo you want this animal to be added to " 
                     + zoo.name 
                     + "? (y/n): ").lower().startswith("y"): zoo.add_animal(addedAnimal)
        case 3: # Remove animal
            if len(zoo.animals) == 0:
                cls()
                input("No animals found in database\n\nPress enter to return")
            else:
                while True:
                    cls()
                    zoo.list_animals()
                    print("\nGive the index of the animal you wish to remove.")
                    deletedAnimal = input("Alternatively, type R to return: ")
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
        case 4: # Exit 
            cls()
            running = False
        case _: pass
