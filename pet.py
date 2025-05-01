from typing import List

class Pet:
    """
    A class to represent a digital pet with attributes and behaviors.

    Attributes:
        name (str): The name of the pet.
        pet_type (str): The type or breed of the pet.
        hunger (int): Hunger level (0 = full, 10 = very hungry).
        energy (int): Energy level (0 = tired, 10 = fully rested).
        happiness (int): Happiness level (0 = sad, 10 = very happy).
        tricks (List[str]): List of tricks the pet has learned.
        age (int): Age of the pet in virtual days.
        health (float): Health level (0 = poor, 10 = excellent).
    """

    def __init__(self, name: str, pet_type: str = "dog") -> None:
        self.name: str = name
        self.pet_type: str = pet_type
        self.hunger: int = 5
        self.energy: int = 5
        self.happiness: int = 5
        self.tricks: List[str] = []
        self.age: int = 0
        self.health: float = 10.0

    def eat(self, food: str = "pet food") -> None:
        """
        Feed the pet to reduce hunger and increase happiness and health.

        Args:
            food (str): The type of food given to the pet.
        """
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        self.health = min(10, self.health + 0.5)
        print(f"🍗 {self.name} savored some {food}. Delicious!")

    def sleep(self) -> None:
        """
        Let the pet sleep to restore energy, increase hunger, and age by one day.
        """
        self.energy = min(10, self.energy + 5)
        self.hunger = min(10, self.hunger + 1)
        self.age += 1  # each sleep counts as a day
        print(f"😴 {self.name} had a cozy nap and feels rejuvenated!")

    def play(self, game: str = "fetch") -> None:
        """
        Play with the pet to increase happiness but decrease energy and increase hunger.

        Args:
            game (str): The game played with the pet.
        """
        if self.energy < 2:
            print(f"😴 {self.name} is too tired to play right now. Let's rest first.")
            return

        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"🎾 {self.name} enjoyed playing {game} with you! What a blast!")

    def train(self, trick: str) -> None:
        """
        Teach the pet a new trick if it has enough energy.

        Args:
            trick (str): The trick to teach the pet.
        """
        if self.energy < 1:
            print(f"😴 {self.name} is too tired to learn right now. Try again later.")
            return

        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        self.energy = max(0, self.energy - 1)
        print(f"🎓 {self.name} mastered a new trick: {trick.capitalize()}!")

    def show_tricks(self) -> None:
        """
        Display all tricks the pet has learned.
        """
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet. Time to start training! 🐾")
        else:
            print(f"🎪 {self.name} can perform these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"  {i}. {trick.capitalize()}")

    def get_status(self) -> None:
        """
        Print the current status of the pet including hunger, energy, happiness, health, and age.
        """
        print(f"\n📊 {self.name}'s Status ({self.pet_type.capitalize()}):")
        print(f"🍽️  Hunger: {'❤️' * self.hunger}{'🤍' * (10 - self.hunger)}")
        print(f"⚡ Energy: {'⚡️' * self.energy}{'⬜️' * (10 - self.energy)}")
        print(f"😊 Happiness: {'😊' * self.happiness}{'😐' * (10 - self.happiness)}")
        print(f"🏥 Health: {'💪' * int(self.health)}{'🩹' * (10 - int(self.health))}")
        print(f"📅 Age: {self.age} virtual days")

    def bathe(self) -> None:
        """
        Bathe the pet, which decreases happiness slightly but improves health.
        """
        self.happiness = max(0, self.happiness - 1)
        self.health = min(10, self.health + 1)
        print(f"🛁 {self.name} had a bath! Fresh and clean, but not too happy about it.")

    def exercise(self) -> None:
        """
        Exercise the pet to improve health but decrease energy and increase hunger.
        """
        if self.energy < 3:
            print(f"😴 {self.name} is too tired to exercise. Let's rest first.")
            return

        self.energy = max(0, self.energy - 3)
        self.hunger = min(10, self.hunger + 2)
        self.health = min(10, self.health + 1)
        print(f"🏃‍♂️ {self.name} went for a run! Getting stronger every day!")

    def celebrate_birthday(self) -> None:
        """
        Celebrate the pet's birthday, increasing age by one year and happiness to max.
        """
        self.age += 36
        self.happiness = 10
        print(f"��🎂 Happy Birthday, {self.name}! Wishing you a fantastic year ahead! �")
