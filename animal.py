class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

    def __str__(self):
        return f"{self.name} ({self.group}) - Legs: {self.number_of_legs}, Skills: {', '.join(self.skills)}"


animals = [
    Animal("Cat", "Mammals", 4, ["climbing", "jumping", "hunting"]),
    Animal("Eagle", "Birds", 2, ["flying", "hunting", "sharp vision"]),
    Animal("Frog", "Amphibians", 4, ["jumping", "swimming", "croaking"]),
    Animal("Shark", "Fish", 0, ["swimming", "hunting", "smelling blood"]),
    Animal("Snake", "Reptiles", 0, ["slithering", "camouflaging", "biting"])
]

for animal in animals:
    print(animal)
