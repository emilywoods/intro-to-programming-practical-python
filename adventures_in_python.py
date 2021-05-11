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
        choice = input(
            "What time do you leave Hermannplatz? a. Before 14:00 b. After 14:00\n"
        )
        if choice == "a":
            print(
                "You are very tired when you get to the lake and fall asleep.\n While you are asleep a wild boar runs off with your belongings 🐗"
            )
        if choice == "b":
            print(
                "Oh no, it is too late. By the time you reach the lake, it is already dark and time to go home. 🌉 :("
            )
            exit()


class SBahn(Transportation):
    def __init__(self):
        self.name = "sbahn"
        self.speed = "fast"
        self.description = "The S-Bahn is busy with people getting out of the city today, but you can read a book, listen to music and gaze out the window. 🚉"

    def encounter_obstacles(self):
        choice = input(
            "You miss your stop and end up in Erkner. What do you do? a. Stay there b. Get back on the s-bahn\n"
        )
        if choice == "a":
            print(
                "Great! Spend the rest of the day exploring the sights and sounds around Erker!"
            )
        if choice == "b":
            pass


class Bicycle(Transportation):
    def __init__(self):
        self.name = "bicycle"
        self.speed = "average"
        self.description = "Efficient and green - cycling is a great way to explore! 🚲"

    def encounter_obstacles(self):
        choice = input(
            "You are cycling past the Landwehr canal and spot your best friend in a boat on the canal.\nWhat do you do? a. Stop and join the boat party or b. wave and continue\n"
        )
        if choice == "a":
            print(
                "Who needs the lake? Put on some sunglasses and bob along the canal all day.🚣"
            )
            exit()
        if choice == "b":
            pass

        choice = input(
            "Uh oh, another cobble stone road gives you a flat tire.\nWhat do you do? a. Fix it b. Go home\n"
        )
        if choice == "a":
            pass
        if choice == "b":
            print(
                "That's all the adventure for today! The lake will have to wait for another day"
            )
            exit()


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
        print(
            f"Travelling by {transportation.name} is {transportation.speed}. {transportation.description}\n"
        )
        transportation.encounter_obstacles()
        self.end(character)

    def end(self, character):
        print(
            f"Yay, {character.name}! You reached the lake by {character.transportation.name}. Time to swim and spend the rest of the day snoozing in the sun ⛵"
        )


new_story = Story()
new_story.start()
