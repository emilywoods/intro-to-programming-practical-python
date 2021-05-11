def introduction_text(name):
    print("")
    print(
        "It's a beautiful summer's day in Berlin, and you are stuck in Hermannplatz :("
    )
    print(
        "You don't want to be here. It is too noisy, there is too much traffic and all this concrete makes it uncomfortably warm"
    )
    print("The lakes are calling...")
    print("")
    print(f"Well {name}, today we go to Müggelsee!")
    print("")


class Transportation:
    def __init__(self, name, speed, description, obstacles):
        self.name = name
        self.speed = speed
        self.description = description

    def encounter_obstacles(self):
        pass


class Walk(Transportation):
    def __init__(self):
        self.name = "walking"
        self.speed = "slow"
        self.description = "It is a long and tiring walk, but scenic.🚶"

    def encounter_obstacles(self):
        pass


class SBahn(Transportation):
    def __init__(self):
        self.name = "sbahn"
        self.speed = "fast"
        self.description = "The S-Bahn is busy with people getting out of the city today, but you can read a book, listen to music and gaze out the window. 🚉"

    def encounter_obstacles(self):
        pass


class Bicycle(Transportation):
    def __init__(self):
        self.name = "bicycle"
        self.speed = "average"
        self.description = "Efficient and green - cycling is a great way to explore! 🚲"

    def encounter_obstacles(self):
        pass


class Character:
    def __init__(self, name, transportation):
        self.name = name
        self.transportation = transportation


class Story:
    def __init__(self):
        pass

    def start(self):
        name = input("What is your name?\n")
        introduction_text(name)

        choice = input(
            "The only question is, how should we go to the lake? a. walking, b. bicycle or c. sbahn\n"
        )
        if choice == "a":
            transportation = Walk()
        elif choice == "b":
            transportation = Bicycle()
        elif choice == "c":
            transportation = SBahn()
        else:
            print("You have not selected a valid option!")
            exit()

        character = Character(name, transportation)

        self.middle(character, transportation)

    def middle(self, character, transportation):
        pass

    def end(self, character):
        pass

new_story = Story()
new_story.start()
