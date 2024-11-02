import random

class TextAdventureGame:
    def __init__(self, seed=None):
        if seed:
            random.seed(seed)
        self.locations = [
            "a dark forest", "a mystical cave", "an abandoned castle", "a haunted graveyard",
            "a bustling village", "an enchanted garden", "a deep ocean", "a snowy mountain",
            "a scorching desert", "a hidden temple", "a magical library", "a floating island"
        ]
        self.events = [
            "find a treasure", "fall into a pit", "encounter a dragon", "meet a wizard",
            "get lost in a maze", "discover a secret passage", "find a magical artifact", "battle a band of thieves",
            "discover a hidden grove", "encounter a talking tree", "meet a band of elves", "get trapped in quicksand",
            "discover an ancient scroll", "meet a talking animal", "find a portal to another dimension", "get caught in a magical storm"
        ]
        self.player_alive = True
        self.has_treasure = False

    def start_game(self):
        print("Welcome to the Ultimate Fantasy Adventure Game!")
        print("Your goal is to find the treasure and survive the perils.")
        self.play_round()

    def play_round(self):
        while self.player_alive:
            self.describe_location()
            choice = self.get_choice()
            self.handle_choice(choice)
            if not self.player_alive:
                print("Game Over! You have perished in your quest.")
            elif self.has_treasure:
                print("You have won the game with the treasure! Congratulations!")
                break

    def describe_location(self):
        location = random.choice(self.locations)
        print(f"\nYou find yourself in {location}.")

    def get_choice(self):
        print("\nYou have the following choices:")
        print("1. Explore further")
        print("2. Rest for a while")
        print("3. Check your inventory")
        return input("What do you choose to do? (1/2/3): ")

    def handle_choice(self, choice):
        if choice == "1":
            self.random_event()
        elif choice == "2":
            print("You decide to rest and regain your strength.")
        elif choice == "3":
            self.check_inventory()
        else:
            print("Invalid choice. Try again.")

    def random_event(self):
        event = random.choice(self.events)
        print(f"\nWhile exploring, you {event}!")
        if event == "fall into a pit":
            self.player_alive = False
        elif event == "encounter a dragon":
            self.dragon_encounter()
        elif event == "meet a wizard":
            self.wizard_encounter()
        elif event == "find a treasure":
            print("Congratulations! You have found the treasure!")
            self.has_treasure = True
        elif event == "get lost in a maze":
            self.maze_encounter()
        elif event == "discover a secret passage":
            print("You find a secret passage leading to a hidden chamber.")
        elif event == "find a magical artifact":
            self.magical_artifact()
        elif event == "battle a band of thieves":
            self.thieves_encounter()
        elif event == "discover a hidden grove":
            print("You discover a beautiful hidden grove filled with rare flowers.")
        elif event == "encounter a talking tree":
            print("A talking tree offers you advice on your quest.")
        elif event == "meet a band of elves":
            print("You meet a band of elves who share their knowledge and supplies.")
        elif event == "get trapped in quicksand":
            self.quicksand_encounter()
        elif event == "discover an ancient scroll":
            print("You find an ancient scroll with magical spells.")
        elif event == "meet a talking animal":
            print("A talking animal helps guide you on your journey.")
        elif event == "find a portal to another dimension":
            print("You find a portal that transports you to a mysterious new world.")
        elif event == "get caught in a magical storm":
            self.magical_storm_encounter()

    def dragon_encounter(self):
        print("The dragon breathes fire! You must fight or flee.")
        choice = input("Do you want to fight (1) or flee (2)? (1/2): ")
        if choice == "1":
            if random.random() < 0.5:
                print("You bravely fight and defeat the dragon!")
            else:
                print("The dragon overwhelms you with its fiery breath.")
                self.player_alive = False
        elif choice == "2":
            print("You manage to escape the dragon's lair.")
        else:
            print("Invalid choice. The dragon catches you off guard.")
            self.player_alive = False

    def wizard_encounter(self):
        print("The wizard offers you a choice of two potions.")
        choice = input("Do you choose the red potion (1) or the blue potion (2)? (1/2): ")
        if choice == "1":
            if random.random() < 0.7:
                print("The red potion heals your wounds and strengthens you.")
            else:
                print("The red potion turns out to be poisonous.")
                self.player_alive = False
        elif choice == "2":
            if random.random() < 0.7:
                print("The blue potion grants you magical powers.")
            else:
                print("The blue potion has no effect.")
        else:
            print("Invalid choice. The wizard vanishes in a puff of smoke.")
            self.player_alive = False

    def maze_encounter(self):
        print("You get lost in a maze of twisting passages.")
        choice = input("Do you want to keep moving (1) or wait for help (2)? (1/2): ")
        if choice == "1":
            if random.random() < 0.5:
                print("You find your way out of the maze!")
            else:
                print("You wander endlessly and run out of supplies.")
                self.player_alive = False
        elif choice == "2":
            print("Eventually, a friendly traveler helps you out of the maze.")
        else:
            print("Invalid choice. You remain lost.")
            self.player_alive = False

    def magical_artifact(self):
        print("You find a magical artifact that grants you a special power.")
        power = random.choice(["invisibility", "super strength", "telepathy", "healing"])
        print(f"The artifact grants you the power of {power}!")

    def thieves_encounter(self):
        print("You are ambushed by a band of thieves!")
        choice = input("Do you want to fight (1), negotiate (2), or flee (3)? (1/2/3): ")
        if choice == "1":
            if random.random() < 0.5:
                print("You bravely fight and defeat the thieves!")
            else:
                print("The thieves overpower you.")
                self.player_alive = False
        elif choice == "2":
            print("You manage to negotiate with the thieves and they let you go.")
        elif choice == "3":
            print("You manage to escape the thieves.")
        else:
            print("Invalid choice. The thieves catch you off guard.")
            self.player_alive = False

    def quicksand_encounter(self):
        print("You get trapped in quicksand!")
        choice = input("Do you want to struggle (1) or stay still (2)? (1/2): ")
        if choice == "1":
            if random.random() < 0.5:
                print("You manage to pull yourself out of the quicksand!")
            else:
                print("You sink deeper into the quicksand.")
                self.player_alive = False
        elif choice == "2":
            print("You stay still and eventually someone helps you out of the quicksand.")
        else:
            print("Invalid choice. You sink deeper into the quicksand.")
            self.player_alive = False

    def magical_storm_encounter(self):
        print("You get caught in a magical storm!")
        choice = input("Do you want to find shelter (1) or brave the storm (2)? (1/2): ")
        if choice == "1":
            if random.random() < 0.5:
                print("You find shelter and wait out the storm.")
            else:
                print("The shelter collapses, and you get caught in the storm.")
                self.player_alive = False
        elif choice == "2":
            if random.random() < 0.5:
                print("You brave the storm and make it through unscathed.")
            else:
                print("The storm overwhelms you.")
                self.player_alive = False
        else:
            print("Invalid choice. The storm catches you off guard.")
            self.player_alive = False

    def check_inventory(self):
        print("You check your inventory and find some supplies to help you on your quest.")

if __name__ == "__main__":
    game = TextAdventureGame(seed=42)  # Set a seed for reproducibility or leave it out for full randomness
    game.start_game()
