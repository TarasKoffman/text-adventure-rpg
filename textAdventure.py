answer = input("Would you like to play? (Yes/No)")
if answer.lower().strip() == "yes":

      print("\nYou walk into a shabby inn on the corner just before the fence "
            "that surrounded the small town. \n A mangled tree stood over the inn, "
            "protruding through the roof.")

      print("\n\nAs you enter, you see a hunched old woman with grey hair trailing her feet."
            "\n She is hobbling over table to table, pouring a steaming liquid into bowls "
            "\n held by men in armour. You guess that your entrance seems quite the"
            "\n unusual event to the tavern folk, as all but one of the heads in the inn has"
            "\n turned towards you, bearing scornful eyes on each. You notice a close-by hand"
            "\n drifting to its corresponding sword. Before the hand can reach its destination, "
            "\n the unturned head speaks over the room.")

      print("\n\"Welcome, traveler. \n I believe I didn't catch your name...\"")
      name = input()
      print("\n\"Ah," + name + ", it's nice to see a lone traveller "
                               "on the road every once in a while, "
                               "reminds me of the old times.\"")

      print("\nThe lady turns her head and gives you a wink, or a blink depending on your disposition"
            "\ntowards such things, as it appears only one eye is present in its socket. She continues "
            "\nserving the tavern, and by now all the soldiers or mercenaries or whoever they were"
            "\nhad put away their sword hands and scornful glances, to your relief.")

      print("\n\n Do you sit in a dark chair you see to your right or go and order a drink? (Sit/Drink)")

else:
      print("That's too bad")


