from mcpi.minecraft import Minecraft  #this line tells the computer to connect to minecraft. don't mess with it
from random import randint

mc = Minecraft.create()

mc.postToChat ("Hello, WMSI Mobile STEM Explorers!!")

Px,Py,Pz = mc.player.getPos() #establishes coordinates for your position. no need to change. 

# Change this to change what the maze looks like
# The '#' are blocks in the maze and the spaces are opennings

maze = ["## #######",
        "## #######",
        "##   #   #",
        "#### ### #",
        "#### #   #",
        "#### # ###",
        "##     ###",
        "## ## ####",
        "#  ##   ##",
        "#######  #",
        "###     ##",
        "##  #### #",
        "##       #",
        "######## #",
        "## ## ## #",
        "## ## ## #",
        "##       #",
        "#### #####",
        "##   ##  #",
        "#### ### #",
        "#### #   #",
        "###  # ###",
        "####   ###",
        "##### ####"]


block = 1  # Change this number to change the block type. Try 57. or 46. or 95

height = 3 # how high to make the maze

add_roof = False # set to True to add a roof to the maze!
  
mc.postToChat ("Now we're creating a Maze!  :)")

# This goes thorough all the blocks in the maze list and places the corresponding block

for z in range(len(maze)):
    for x in range(len(maze[z])):
        for y in range(height):
            symbol = maze[z][x]

            # choose which block we used based on the symbol in the maze
            block_here = 0 # 0 is air, an empty block
            if symbol == "#":
                block_here = block
            elif symbol == " ":
                block_here = 0

            # place the correct block at the right position!
            # we add 1 to start away from the player
            mc.setBlock(Px + 1 + x, Py + y, Pz + 1 + z, block_here)

        # add a roof block if we're told to! (go one above and don't add air)
        if add_roof:
            mc.setBlock(Px + 1 + x, Py + y + 1, Pz + 1 + z, block)

mc.postToChat ("Ok! Ready?  Look to your left to see the maze! Go find the entrance!") #this puts a message in your chat box. within the "" you can change the message. 

#hit F5 to run code! a box will pop up asking you to save the code. hit ok and your code will run!

