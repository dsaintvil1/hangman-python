""" 
Danerick Saint-Vil

"""

import random

# Word bank of words to use for the game
word_bank = [
    # Animals
    ["elephant", "giraffe", "kangaroo", "penguin", "dolphin", "tiger",
    "lion", "zebra", "alligator", "chimpanzee", "rhinoceros", "flamingo",
    "hippopotamus", "gorilla", "meerkat", "otter", "porcupine", "raccoon",
    "squirrel", "turtle", "panther", "cobra", "whale", "shark", "octopus"],

    # Food
    ["spaghetti", "hamburger", "chocolate", "croissant", "pancake", "sandwich",
    "omelette", "lasagna", "pizza", "strawberry", "blueberry", "pineapple",
    "avocado", "cucumber", "tomato", "broccoli", "carrot", "potato", "onion",
    "pumpkin", "cheesecake", "burrito", "taco", "sushi", "noodles"],

    # Places
    ["mountain", "desert", "island", "volcano", "rainforest", "village",
    "city", "ocean", "beach", "valley", "canyon", "river", "waterfall",
    "castle", "palace", "temple", "museum", "harbor", "stadium", "bridge"],

    # Science & Tech
    ["gravity", "electricity", "magnet", "galaxy", "planet", "asteroid",
    "neutron", "quantum", "molecule", "voltage", "robotics", "circuit",
    "satellite", "telescope", "microscope", "physics", "chemistry", "biology",
    "equation", "experiment", "data", "algorithm", "computer", "variable"],

    # Sports
    ["soccer", "basketball", "baseball", "volleyball", "cricket", "rugby",
    "badminton", "tennis", "golf", "boxing", "wrestling", "cycling",
    "skateboard", "snowboard", "surfing", "archery", "fencing", "karate",
    "swimming", "diving"],

    # Misc
    ["umbrella", "keyboard", "headphones", "notebook", "calendar", "backpack",
    "camera", "sunglasses", "pillow", "blanket", "lantern", "compass",
    "airplane", "bicycle", "train", "rocket", "planetarium", "diamond",
    "rainbow", "fireworks", "treasure", "dragon", "castle", "wizard", "potion"]
]

round_bank = []
def reset():
    for x in range(len(word_bank)):
        round_bank.append(word_bank[x][random.randrange(len(word_bank[x]))])

def draw(step):
    print(f" _____\n|{"|":>6}")
    if step > 0:
        print(f"|{"( )":>7}")
    else:
        print("|")
    if step == 2:
        print(f"|{"|":>6}")
    elif step == 3:
        print(f"|{"/|":>6}")
    elif step > 3:
        print(f"|{"/|\\":>7}")
    else:
        print("|")
    if step == 5:
        print(f"|{"/":>5}")
    elif step > 5:
        print(f"|{"/ \\":>7}")
    print("|\n")

draw(6)




