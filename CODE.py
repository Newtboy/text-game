import sys
import time
import random
import console


death_messages_1 = [
    "You fool! You shouldn't have died yet!",
    "The story cannot continue....",
"""                     __       __
                     '.'--.--'.-'
       .,_------.___,   \' r'
       ', '-._a      '-' .'
        '.    '-'Y \._  /
          '--;____'--.'-,
           /..'       '''""",    
    "Wow that whale was certainly something!",
    "sucks to suck",
    "kill yourself- oh wait.",
    "Congrats! That was probably best part of your life, the end.",
    "    anoy anoy anoy",
    "give me soup or give me death",
    "Ya mums' a hoe",
    "Suprise!",
    "How the Hell DID YOU DIE, THIS IS EASY",
    "Congratulations. You played yourself."
]

death_messages_2 = [
    "You fool! You shouldn't have died yet!",
    "The story cannot continue....",
"""                     __       __
                     '.'--.--'.-'
       .,_------.___,   \' r'
       ', '-._a      '-' .'
        '.    '-'Y \._  /
          '--;____'--.'-,
           /..'       '''""",    
    "Wow that whale was certainly something!",
    "    anoy anoy anoy",
    "give me soup or give me death",
    "Suprise!",
    "How DID YOU DIE? THIS IS EASY!",
    "Congratulations. You played yourself."
]

# Define the rooms and their  properties
rooms = {
    "start": {
        "description": "You find yourself in a dimly lit room. There are two doors ahead.",
        "exits": {
            "left": "dark_forest",
            "right": "right_hallway"
        }
    },
    "right_hallway": {
    "description": "You find yourself in a dimly lit hallway. The walls are adorned with faded tapestries.",
    "exits": {
        "forward": "grand_foyer",
        "back": "start"
    }
},

    "grand_foyer": {
    "description": "You step into a grand foyer with a towering ceiling and a chandelier casting a soft glow.",
    "exits": {
        "forward": "mystical_gallery",
        "back": "right_hallway",
        "upstairs": "elegant_study"
    }
},
    "elegant_study": {
        "description": "You ascend a grand staircase and enter an elegant study filled with shelves of books and intricate artifacts.",
        "exits": {
            "downstairs": "grand_foyer"
        },
        "hidden_exits": {
            "search": "hidden_passage"
        }
    },
    
    "hidden_passage": {
        "description": "Your search reveals a hidden passage behind a sliding bookshelf. It leads to a secret room.",
        "exits": {
            "back": "elegant_study",
            "enter": "secret_room"
        }
    },

    "secret_room": {
        "description": "You find yourself in a secret room with ancient maps and mysterious artifacts on display.",
        "exits": {
            "back": "hidden_passage"
        }
    },
    "mystical_gallery": {
    "description": "You enter a gallery lined with paintings that seem to shift and change as you walk by.",
    "exits": {
        "forward": "eerie_sculpture_room",
        "back": "grand_foyer"
    }
},

"eerie_sculpture_room": {
    "description": "The room is filled with unsettling sculptures that appear almost lifelike in the dim light.",
    "exits": {
        "forward": "candlelit_passage",
        "back": "mystical_gallery"
    }
},

"candlelit_passage": {
    "description": "A narrow passage illuminated by candlelight stretches ahead, leading deeper into the unknown.",
    "exits": {
        "forward": "forgotten_chapel",
        "back": "eerie_sculpture_room"
    }
},

"forgotten_chapel": {
    "description": "You step into a forgotten chapel with stained glass windows depicting scenes of a bygone era.",
    "exits": {
        "forward": "entrance_cave",
        "back": "candlelit_passage"
    }
},

"entrance_cave": {
    "description": "You arrive at the entrance of a cave. The wind howls as it rushes out from the depths.",
    "exits": {
        "enter": "cave_passage",
        "back": "forgotten_chapel"
    }
},

"cave_passage": {
    "description": "The cave passage stretches before you, gradually descending into darkness.",
    "exits": {
        "forward": "cave_tunnel",
        "back": "entrance_cave"
    }
},
    "dark_forest": {
        "description": "You are in a dark forest. Moonlight barely filters through the thick canopy.",
        "exits": {
            "forward": "deep_forest",
            "back": "start"
        }
    },
    "deep_forest": {
        "description": "You are in a deep, dense forest with towering trees all around.",
        "exits": {
            "forward": "strange_clearing",
            "back": "dark_forest"
        }
    },
    "strange_clearing": {
        "description": "You find yourself in a strange clearing. The trees appear to claw towards you, and there is a strange fog.",
        "exits": {
            "forward": "old_cottage",
            "back": "deep_forest"
        }
    },
    "mysterious_cave": {
        "description": "You stand before a mysterious cave entrance, a gust of wind blows from within.",
        "exits": {
            "enter": "cave_entrance",
            "back": "start"
        }
    },
    "debug": {
    "description": "You are in the debug room.",
    "exits": {}
    },
    "cave_entrance": {
        "description": "Inside the cave, the air is damp and echoes with distant sounds.",
        "exits": {
            "forward": "cave_tunnel",
            "back": "mysterious_cave"
        }
    },
    "cave_tunnel": {
        "description": "You walk deeper into the cave, the walls shimmer with faint bioluminescent light.",
        "exits": {
            "forward": "dragon_lair",
            "back": "cave_entrance"
        }
    },
    "treasure_room": {
        "description": "You enter a room filled with glittering treasures, some hidden behind ancient tomes.",
        "exits": {
            "search": "secret_treasure_room",
            "back": "cave_tunnel"
        }
    },
    "secret_treasure_room": {
        "description": "A secret passage reveals a room with even more extravagant treasures.",
        "exits": {
            "back": "treasure_room"
        }
    },
    "cottage_interior": {
        "description": "You enter the cozy interior of the old cottage. Flickering candlelight casts eerie shadows on the walls.",
        "exits": {
            "exit": "old_cottage"
        }
    },
    "old_mineshaft": {
        "description": "You go down the trapdoor, but it is too dark to see.",
        "exits": {
            "exit": "cottage_interior"
        }
    },
"dragon_lair": {
    "description": "You enter a massive cavern, and at its center, a fearsome dragon rests on a pile of gold.",
    "exits": {
        "back": "cave_tunnel",
        "speak": "dragon_conversation"
    }
},

    "dragon_conversation": {
        "description": "The dragon speaks, its voice rumbling like thunder. It offers you a choice: answer a riddle or face its fiery breath.",
        "exits": {
            "riddle": "dragon_riddle",
            "fiery_breath": "fiery_death"
        }
    },

    "dragon_riddle": {
        "description": "",
        "exits": {
            "answer": "dragon_riddle_answer",
            "back": "dragon_conversation"
        }
    },

    "dragon_riddle_answer": {
        "description": "The dragon stares, then starts to chuckle. The laugher gets louder and more hearty. It laughs so hard it decides to not kill you immediately.",
        "exits": {
            "back": "dragon_conversation"
        }
    },

    "fiery_death": {
        "description": "The dragon's fiery breath engulfs you, and your journey comes to a sudden and unfortunate end.",
        "exits": {},
        "actions": [
            {
                "on_enter": {
                    "command": "die"
                }
            }
        ]
    },
    "end": {
        "description": "You have reached the end of your journey.",
        "exits": {}
    }
}


enemy_rooms = ["deep_forest", "treasure_room"]  # Add other enemy rooms here
defeated_enemies = {}
searched_abandoned_house = False
found_secret_treasure = False
met_sorcerer = False
has_lantern = False
player_gold = 0
player_health = 100
in_interaction = False

def add_item_to_inventory(item):
    player["inventory"].append(item)
    console.set_color(255,215,0)
    print(item + " has been added to your inventory.")
    console.set_color()

def remove_item(item):
    player["inventory"].remove(item)
    print(item + " has been removed from your inventory.")

def has_item(item):
    return item in player["inventory"]

def display_gold():
    print("Gold:", player["gold"])

def display_health():
    print("Health:", player["health"])

def main():
    player["name"] = input("Enter your name: ")
    print("Welcome,", player["name"])
 
    while True:
        choice = input("Enter your choice: ")

def initial_interaction():
    global in_interaction
    global player_health
    
    print_slow("Welcome to the adventure! Before we begin, I have a couple of questions for you.")
    teacher_response = input("Are you a teacher? (yes/no): ").lower()
    age_response = input("Are you under 15 years old? (yes/no): ").lower()
    
    if teacher_response == "yes" or age_response == "yes":
        print_slow("Thank you for your input. The game now doesn't contain offensive/inappropriate material, so I can't get in trouble. Also, you aren't missing anything but a few inappropriate jokes.")
        return False
    else:
        print_slow("Thank you for your input. The game will continue as normal.")
        return True

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.03)
    print("")

def die():
    if in_interaction == False:
        player_health = -1
        death_message = random.choice(death_messages_1)
        sys.exit(0)
    else:
        player_health = -1
        death_message = random.choice(death_messages_2)
        console.set_color(100,0,0)
        print_slow(death_message)
        console.set_color()
        sys.exit(0)

def sorcerer_conversation():
    working_words = [
        "adventure"
    ]  # List to store the working words
    attempts = 0  # Number of times the player has attempted to respond

    while True:
        response = input("Enter your response: ").lower()

        if "adventure" in response:
            print_slow("Ah, an adventurer seeking mysteries! I might have a task for you...")
            print_slow("But before I proceed, I must know if you are honest.")
            honesty_response = input("Are you an honest person? (yes/no): ").lower()

            if honesty_response == "yes":
                print_slow("Very well. I shall reward your honesty.")
                print_slow("The sorcerer hands you a simple lantern.")
                add_item_to_inventory("lantern")
                break
            else:
                print_slow("I sense deceit in your words. Choose your next words wisely.")
                print_slow("I offer you a powerful potion, but it will cost you more than you think.")
                gold_response = input("Do you accept this offer? (yes/no): ").lower()

                if gold_response == "yes":
                    global player_health
                    player_health = -1
                else:
                    print_slow("Very wise. Beware of dishonesty.")
                    player_health = 0
                break
        else:
            attempts += 1

            if attempts < 3:
                print_slow("What? You need to speak up.")
            else:
                hint = ", ".join(working_words)
                print_slow(f"What? You need to speak up. ({hint})")

def dragon_conversation():
    working_words = ["gold", "treasure"]
    attempts = 0

    while True:
        response = input("Enter your response: ").lower()

        if "gold" in response or "treasure" in response:
            print_slow("A fierce dragon looks at you with curiosity:")
            print_slow("The dragon speaks:")
            print_slow("You seek gold and treasure, do you?")
            response = input("Enter your response: ").lower()

            if "yes" in response:
                print_slow("Very well, mortal. But what will you offer in return?")
                offering_response = input("Enter your offering: ").lower()

                if "sword" in offering_response:
                    print_slow("A sword, you say? Interesting...")
                    print_slow("The dragon accepts your offering and leads you to its hoard of gold.")
                    player_gold += 100
                    console.set_color(255, 215, 0)
                    print("You got 100 gold!")
                else:
                    print_slow("Your offering does not interest me. Begone!")
                    return False  # Indicate failure
            else:
                print_slow("Hmmm, your hesitation speaks volumes.")
                return False  # Indicate failure
        else:
            attempts += 1

            if attempts < 2:
                print_slow("What? You need to speak up.")
            elif attempts < 3:
                hint = ", ".join(working_words)
                print_slow(f"What? You need to speak up. ({hint})")
            else:
                print_slow("The dragon's eyes narrow. 'Incorrect,' it says. 'Prepare for a challenge.'")
                return False  # Indicate failure

# In your main game loop:


def room_intro(room_name, rooms_dict):
    global met_sorcerer
    global player_gold
    global has_lantern
    global player_health

    print_slow(rooms_dict[room_name]['description'])
    print_valid_moves(room_name, rooms_dict)
    
    if room_name == "dragon_lair" and "speak" in rooms_dict[room_name]['exits']:
        room_intro("dragon_conversation", rooms_dict)
    elif room_name == "strange_clearing":
        if not met_sorcerer:
            print_slow("A cloaked figure stands before you:")
            print_sorcerer_art()
            print_slow("The sorcerer speaks:")
            print_slow("Greetings, traveler. I am the ancient sorcerer. What brings you to this place?")
        
            # Call the sorcerer_conversation function here
            sorcerer_conversation()

            # Set met_sorcerer to True to prevent the sorcerer's introduction from repeating
            met_sorcerer = True
        else:
            print_slow("The sorcerer stands before you.")
        
        
    elif room_name == "fiery_death":
        if not rooms_dict[room_name].get("entered"):
            player_health = -1
            rooms_dict[room_name]["entered"] = True
    
    elif room_name == "debug":
        new_room_name = input("Enter the name of the area you want to enter: ").lower()
        if new_room_name in rooms_dict:
            current_room = new_room_name
        else:
            print_slow("That area does not exist.")
    elif room_name == "dragon_riddle":
        dragon_conversation()
    elif room_name == "cottage_interior":
        print_slow("You are in the cozy interior of the old cottage.")
        action = input("What would you like to do? ").lower()
        
        if action == "die":
            die()

        if action == "search":
            search_chance = random.random()
            if search_chance > 0.2:
                print_slow("You discover a loose floorboard beneath the rug.")
                print_slow("Upon lifting the floorboard, you find a hidden hatch.")
                print_slow("Would you like to enter the hatch? (yes/no)")
                response = input("> ").lower()
                if response == "yes":
                    if has_lantern:
                        print_slow("You descend through the hatch and find yourself in an old mineshaft.")
                        current_room = "old_mineshaft_dark"
                    else:
                        print_slow("You need a lantern to safely navigate the mineshaft.")
                else:
                    print_slow("You decide not to enter the hatch.")
            else:
                print_slow("You search the room but find nothing of interest.")
    
def print_valid_moves(room_name, rooms_dict):
    print_slow("Valid moves:")
    for exit_direction in rooms_dict[room_name]['exits']:
        print_slow("- " + exit_direction)
    if room_name in enemy_rooms and not defeated_enemies.get(room_name):
        print_slow("- fight")
    if room_name == "abandoned_house" and not searched_abandoned_house:
        print_slow("- search")
    if room_name == "treasure_room" and not found_secret_treasure:
        print_slow("- search for secret area")

def print_sorcerer_art():
    sorcerer_art = """
              _,._
  .||,       /_ _\\
 \.`',/      |'L'| |
 = ,. =      | -,| L
 / || \    ,-'\"/,'`.
   ||     ,'   `,,. `.
   ,|____,' , ,;' \| |
  (3|\    _/|/'   _| |
   ||/,-''  | >-'' _,\\
   ||'      ==\ ,-'  ,'
   ||       |  V \ ,|
   ||       |    |` |
   ||       |    |   \\
   ||       |    \    \\
   ||       |     |    \\
   ||       |      \_,-'
   ||       |___,,--")_\
   ||         |_|   ccc/
   ||        ccc/
   ||
        """
    print(sorcerer_art)
print_game_over = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠛⣻⣿⣻⣿⣿⣶⠶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠶⣦⡀⠀⠀⠀⠀⠀⠀⢀⡴⢋⣤⠶⣟⣛⣿⡿⠿⣿⣿⣷⡾⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⣤⣿⡇⠀⠀⠀⠀⠀⢀⡞⣦⣨⣿⡳⠉⢛⣋⣤⣤⣘⣷⣿⡇⣼⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⣿⣭⡇⠀⠀⠀⠀⠀⢸⡁⣿⡟⠉⠉⠓⠻⠿⠿⠟⠛⠉⠀⠀⠉⢫⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠈⠀⠇⠀⠀⠀⠀⠀⢸⡿⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣦⣤⡿⣂⠀⠀⠀⠀⠀⠘⣿⣿⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠙⠋⢸⠀⠀⠀⠀⠀⢀⢿⣿⠁⠀⢀⣀⣤⣀⣀⠆⠀⣀⣤⣴⣶⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⠤⣿⠀⠀⢸⣀⣀⡀⠀⠀⣿⣻⣻⡂⠚⣫⣽⠿⣻⠟⢁⠀⣿⠛⠛⠹⠛⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⣾⠀⠀⠸⣇⣈⢹⣤⣄⠻⡿⡝⣇⠀⠀⠀⠈⠉⠀⠘⠚⣷⣄⠀⠀⠀⠘⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⠟⠛⣿⠀⠀⠙⢯⠉⠳⣿⠾⣷⡿⣷⢮⢷⡀⠀⠀⣠⠦⣗⠀⣹⣽⣆⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡞⠉⡇⢸⡟⣆⠀⠀⠀⠀⠀⡤⢧⡈⡇⠈⠻⣆⠙⢤⣼⣯⣀⣈⣛⣿⠿⣯⡗⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠛⠀⡇⢶⠀⠸⡄⠀⠀⠀⢸⠁⠀⢹⡇⠀⣰⣿⣄⠈⠃⠙⢿⣦⣤⡴⣾⢿⠇⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⡀⢰⡇⠀⠀⠀⢻⠀⠀⠀⢸⡆⠀⠀⣷⣾⣿⣿⠈⢳⡀⠀⠀⠹⣷⣮⡵⠟⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠐⠂⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣧⡀⠘⠳⣄⠀⠀⠀⠀⢀⡴⣻⠀⠀⠰⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣦⡀⠈⠙⠒⠒⣺⣿⣶⣿⣿⣿⣶⣽⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠓⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣯⢳⣀⠀⢀⣼⣷⣤⣞⣛⠿⣿⠈⠀⢹⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⢄⣀⡀⠀⠀⠀⠄⢰⡿⢿⣿⣿⣿⣿⣿⣿⣧⡻⣿⡿⠁⠈⠛⢿⣛⣻⣿⠀⠀⠀⢿⣿⣿⣿⣿⡀⠀⣀⣀⣤⣤⣴⣶⡾⠿⠿⣿⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⠀⠀⣀⣤⠖⠋⣠⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⢹⠿⢛⣦⣀⣀⣨⣿⣿⣿⣿⣿⡿⢻⣿⣻⣭⣭⣤⣤⣄⠀⣿⣇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠟⠛⠉⠁⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣀⣠⣤⣴⣿⣶⡿⠿⠿⠛⠛⢩⣭⢻⣷⣿⣿⡿⠿⠈⣿⣿⠉⠻⣿⡆⠸⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠠⣎⣁⣠⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠛⠋⣙⣽⣦⣄⠀⢿⣷⡀⠀⢸⣿⠘⣿⣧⠀⠀⠀⠀⢹⣿⣶⣾⣿⣇⠀⣿⣆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⡛⣿⣯⣭⣴⣾⣿⠁⠀⠀⢰⣿⡟⠛⢿⣷⠈⢿⣧⠀⢸⣿⠀⢹⣿⣿⠿⠇⠀⠘⣿⡏⠉⢹⣿⡄⢸⣿⠀
⠀⠀⠀⢀⣀⣀⣤⣤⣶⣾⡿⠿⢿⠻⠛⠋⣽⣅⠀⠀⢠⣿⣇⠸⣿⡟⠋⠉⠁⠀⠀⠀⠘⣿⡇⠀⠸⣿⡆⠈⢿⣷⣸⣿⠀⠘⣿⣇⢀⣀⣀⡄⢹⣿⡄⠈⠿⠷⠘⣿⡆
⠰⣶⡿⠿⠛⣛⣫⣉⠉⠀⢠⣾⣿⣿⣷⡄⢸⣿⣷⣤⣾⣿⣿⠀⣿⣷⣤⣶⣦⠀⠀⠀⠀⢿⣿⠀⠀⣿⣧⠀⠈⢿⣿⣿⠀⠀⢿⣿⠿⠿⠛⠃⢈⣋⣤⣤⣴⣶⣶⡿⠇
⠀⣿⣇⠀⣼⣿⠿⢿⣿⣆⣿⣿⠀⠈⢿⣷⠈⣿⡏⢿⣿⠉⣿⡇⢸⣿⡏⠉⠁⠀⠀⠀⠀⠘⢿⣷⣶⣿⠏⠀⠀⠈⠛⢃⣀⣀⣤⣴⣶⣾⠿⠿⠿⠛⠋⠉⠉⠀⠀⠀⠀
⠀⠸⣿⠀⢿⣿⠀⠀⢙⣃⠘⣿⣷⣶⣾⣿⡆⢻⣿⠀⠀⠀⢻⣿⠈⣿⣷⣶⣶⣿⠇⠀⠀⠀⢀⣈⣉⣤⣴⣶⣶⠿⠿⠟⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⡇⢸⣿⡆⢸⣿⣿⡀⢿⣿⠉⠈⣿⣧⠸⣿⣧⠀⠀⠘⠿⡃⢘⣉⣡⣤⣤⣴⣾⠿⠿⠟⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⠀⢿⣷⣤⣼⣿⠀⠸⣿⠆⠀⠘⣛⣀⣩⣥⣤⣶⣶⣿⠿⠟⠛⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⣿⡇⠀⠉⠛⣋⣡⣤⣤⣶⣶⣶⠿⠟⠛⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢻⣿⣾⠿⠿⠟⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

def battle(player_health, enemy_health):
    while player_health > 0 and enemy_health > 0:
        print_slow("Your health: {}, Enemy health: {}".format(player_health, enemy_health), delay=0.05)
        player_attack = random.randint(5, 15)
        enemy_attack = random.randint(3, 10)

        print_slow("You attack the enemy for {} damage!".format(player_attack), delay=0.05)
        enemy_health -= player_attack
        if enemy_health <= 0:
            print_slow("You defeated the enemy!")
            return True

        print_slow("The enemy attacks you for {} damage!".format(enemy_attack), delay=0.05)
        player_health -= enemy_attack
        if player_health <= 0:
            print_slow("You have been defeated by the enemy.")
            return False

def search_abandoned_house():
    global player_gold
    print_slow("You search the abandoned house and find a small stash of gold pieces!")
    gold_found = random.randint(5, 20)
    player_gold += gold_found
    print_slow("You found {} gold pieces.".format(gold_found))
    global searched_abandoned_house
    searched_abandoned_house = True

def search_secret_treasure():
    global player_gold
    success_chance = random.random()
    if success_chance < 0.6:
        print_slow("You discover a hidden lever that opens a secret passage!")
        gold_found = random.randint(15, 30)
        player_gold += gold_found
        console.set_color(255,215,0)
        print_slow("You found a secret treasure area and collected {} gold!".format(gold_found))
        console.set_color()
        global found_secret_treasure
        found_secret_treasure = True
    else:
        print_slow("You search for a while, but you don't find anything unusual.")

player = {
    "name": "",
    "inventory": [],
    "gold": 0,
    "health": 100
}

def play_game(rooms_dict):
    global player_health
    player_health = 100
    global player_gold
    global defeated_enemies
    global searched_abandoned_house
    global found_secret_treasure
    global met_sorcerer
    global has_lantern
    player_gold = 0
    searched_treasure_room = False
    current_room = "start"
    
    player = {
    "current_room": "start",
    "health": 100,
    "inventory": []
    }


    while True:
        room_name = current_room
        if player_health > 0:
            room_intro(room_name, rooms_dict)
    
        if player_health <= 0:
            if in_interaction == False:
                death_message = random.choice(death_messages_1)
                print_slow(death_message)
                break
            else:
                death_message = random.choice(death_messages_2)
                console.set_color(255, 0, 0)  # Set the color to red
                print(print_game_over)
                console.set_color()  # Reset the color
                print_slow(death_message)
                break
        
        
        if current_room == "end":
            print_slow("Congratulations! You have completed the game.")
            print_slow("You collected {} gold pieces.".format(player_gold))
            break
        elif room_name == "treasure_room":
            print(rooms[room_name]["description"])
            action = input("> ").lower()
        
            if action == "search":
                if not found_secret_treasure:
                    search_secret_treasure()
                else:
                    print("You search the room but find nothing new.")
            elif action in rooms[room_name]["exits"]:
                player["current_room"] = rooms[room_name]["exits"][action]
            else:
                print("Invalid action!")
        elif current_room in enemy_rooms and not defeated_enemies.get(current_room):
            print_slow("An enemy appears! Do you want to fight or leave?")
            action = input("> ").lower()
            if action == "fight":
                enemy_health = random.randint(20, 40)
                if battle(player_health, enemy_health):
                    defeated_enemies[current_room] = True
                    player_gold += random.randint(5, 15)
                    continue
            else:
                # If player chooses to leave, move to the back exit
                current_room = rooms_dict[current_room]['exits']['back']
                continue
        elif current_room == "treasure_room" and not found_secret_treasure:
            print_slow("You are in a room filled with glittering treasures.")
            action = input("> ").lower()
            if action == "search":
                if not searched_treasure_room:
                    search_result = search_secret_treasure()
                    searched_treasure_room = True
                    if search_result:
                        continue
                else:
                    print_slow("You have already searched this area.")
        elif current_room == "abandoned_house" and not searched_abandoned_house:
            print_slow("You find an old abandoned house covered in vines.")
            action = input("> ").lower()
            if action == "search":
                search_abandoned_house()
            else:
                current_room = rooms_dict[current_room]['exits']['back']
        else:
            print_slow("What would you like to do?")
            action = input("> ").lower()
            
            if action == "gold":
                display_gold()
            elif action == "health":
                display_health()
        
            elif action in rooms_dict[current_room]['exits']:
                current_room = rooms_dict[current_room]['exits'][action]
            elif action == "debug":
                print("Available rooms:")
                for room_name in rooms_dict:
                    print("- " + room_name)
                chosen_room = input("Enter the name of the room: ")
                if chosen_room in rooms_dict:
                    current_room = chosen_room
                else:
                    print("Invalid room name.")
            elif action == "die":
                player_health = -1
                continue
            else:
                print_slow("You can't do that here.")
                print_valid_moves(current_room, rooms_dict)
                continue

if __name__ == "__main__":
    print_slow("Welcome to the Text Adventure Game!")
    initial_interaction()
    play_game(rooms)