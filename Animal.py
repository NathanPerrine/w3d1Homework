class Animal:
    def __init__(self, name, energy=10):
        self.name = name
        self.energy = energy

    def eat(self, food, restore):
        print(f"Eating {food}")
        print("Energy restored!")
        self.energy += restore
        print(f"Energy level: {self.energy}")

    def play(self, time):
        print("Play time!")
        print("Losing energy...")
        self.energy -= time
        print(f"Energy level: {self.energy}")

    def sleep(self, time):
        print("Time to sleep!")
        print("Restoring energy...")
        self.energy += time
        print(f"Energy level: {self.energy}")



puppy = Animal('Slagathor', 10)
puppy.eat('kibble', 20)
puppy.play(10)
puppy.sleep(20)


