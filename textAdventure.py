# Text Adventure :)
# By Taras Koffman / Kane Bebb

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

### Player Setup ###
class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'
myPlayer = player()

### Title Screen ###
def title_screen_selections():
    option = input("> ")
    if option.lower() == "play":
        start_game() #### This is a placeholder currently
    elif option.lower() == "help":
        help_menu() #### Also a placeholder
    elif option.lower() == "quit":
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print('Please enter a valid command')
        option = input("> ")
        if option.lower() == "play":
            start_game()  #
        elif option.lower() == "help":
            help_menu()  #
        elif option.lower() == "quit":
            sys.exit()

def title_screen():
    os.system('clear')
    print("############################")
    print("#     Welcome Traveler     #")
    print("############################")
    print("          - Play -          ")
    print("          - Help -          ")
    print("          - Quit -          ")
    print("      Made by Taz/Kane      ")
    title_screen_selections()

def help_menu():
    print("############################")
    print("#     Welcome Traveler     #")
    print("############################")
    print("- Use up, down, left, and right to move ")
    print("- Type commands to execute them ")
    print("- Use 'Look' to inspect something")
    print("            GLHF :)         ")
    title_screen_selections()



###### Game Functionality ######
def start_game():

##### SAMPLE MAP #####

"""
 a   b  c  d   ## Player starts at b2 ##
-------------
|  |  |  |  |  1
-------------
|  |  |  |  |  2
-------------
|  |  |  |  |  3
-------------
|  |  |  |  |  4
-------------

"""
ZONENAME = ""
DESCRIPTION = "describe"
EXAMINATION = "examine"
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False
                 'b1': False, 'b2': False, 'b3': False, 'b4': False
                 'c1': False, 'c2': False, 'c3': False, 'c4': False
                 'd1': False, 'd2': False, 'd3': False, 'd4': False}

zonemap = {
    'a1':  {
    ZONENAME: ""
    DESCRIPTION = "describe"
    EXAMINATION = "examine"
    SOLVED = False
    UP = 'up', 'north'
    DOWN = 'down', 'south'
    LEFT = 'left', 'west'
    RIGHT = 'right', 'east'
},
'a1':  {
    ZONENAME: ""
    DESCRIPTION = "describe"
    EXAMINATION = "examine"
    SOLVED = False
    UP = 'up', 'north'
    DOWN = 'down', 'south'
    LEFT = 'left', 'west'
    RIGHT = 'right', 'east'
},

'a1':  {
    ZONENAME: ""
    DESCRIPTION = "describe"
    EXAMINATION = "examine"
    SOLVED = False
    UP = 'up', 'north'
    DOWN = 'down', 'south'
    LEFT = 'left', 'west'
    RIGHT = 'right', 'east'
},

'a1':  {
    ZONENAME: ""
    DESCRIPTION = "describe"
    EXAMINATION = "examine"
    SOLVED = False
    UP = 'up', 'north'
    DOWN = 'down', 'south'
    LEFT = 'left', 'west'
    RIGHT = 'right', 'east'
},

'a1':  {
    ZONENAME: ""
    DESCRIPTION = "describe"
    EXAMINATION = "examine"
    SOLVED = False
    UP = 'up', 'north'
    DOWN = 'down', 'south'
    LEFT = 'left', 'west'
    RIGHT = 'right', 'east'
},


















}
