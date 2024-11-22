# define a class called VirtualPet with the following fields:
# (1) name - the name of the pet
# (2) energy - the enery points for the pet, default value is 10
# (3) hunger - the pet's hunger level, default value is 0
# When an instance of VirtualPet is created, only the name is needed
# for the __init__ method



# this class has the following methods:
# (1) play() - simulate playing by reducing the energy by 2 and increase the hunger by 2
#     each time this method is called. If insufficient energy, prints "Too tired to play"
# (2) feed() - to simulate feeding the pet and reducing hunger by reducing hunger by the formula
#     hunger = max(0, hunger - 3). If hunger is less than 0, the pet is overfeed (which is possible)
# (3) sleep() - let the pet sleep to restore energy by increasing the energy by 10.
# (4) __str__ - returns the details of the pet in the format "pet_name with x energy points and y hunger level", 
#     e.g., Timmy with 100 energy points and 0 hunger level




class VirtualPet:
    """
    A class to represent a virtual pet.

    Attributes:
        name (str): The name of the pet.
        energy (int): The energy points of the pet, default is 10.
        hunger (int): The hunger level of the pet, default is 0.
    """

    def __init__(self, name):
        """
        Initialize the VirtualPet with a name. Default values:
        energy = 10, hunger = 0.
        
        Parameters:
            name (str): The name of the pet.
        """
        self.name = name
        self.energy = 10
        self.hunger = 0

    def play(self):
        """
        Simulate playing with the pet. Reduces energy by 2 and increases hunger by 2.
        If energy is less than 2, print "Too tired to play".
        """
        if self.energy < 2:
            print("Too tired to play")
        else:
            self.energy -= 2 # self.energy=self.energy-2
            self.hunger += 2 # self.hunger=self.hunger+2

    def feed(self):
        """
        Simulate feeding the pet. Reduces hunger by 3 using the formula:
        hunger = max(0, hunger - 3).
        """
        self.hunger = max(0, self.hunger - 3)

    def sleep(self):
        """
        Simulate the pet sleeping. Restores energy by increasing it by 10.
        """
        self.energy += 10 # self.energy=self.energy+10

    def __str__(self):
        """
        Return a string representation of the pet's details.
        Format: "pet_name with x energy points and y hunger level".
        """
        return f"{self.name} with {self.energy} energy points and {self.hunger} hunger level"


# Testing the VirtualPet class
if __name__ == "__main__":
    pet = VirtualPet("Timmy")
    print(pet)  # Initial details 
    
    pet.play()
    print(pet)  # After playing
    
    pet.feed()
    print(pet)  # After feeding
    
    pet.sleep()
    print(pet)  # After sleeping
