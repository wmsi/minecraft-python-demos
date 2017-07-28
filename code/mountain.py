from mcpi.minecraft import Minecraft  #this line tells the computer to connect to minecraft. don't mess with it
import random

mc = Minecraft.create()

mc.postToChat ("Hello, WMSI Mobile STEM Explorers!!")


#### Things to change

block = 2   # Change this number to change the block type
size = 4  # Change this number to change the size of the BASE
          # of the mountain (from center to edge)
height = 4 # Change this number to change the height of the mountain

randomLevels = True # Whether to add randomness to each level
# controls how the mountains looks
# set to 1 to only PLACE blocks, and 0 to place NO blocks
# Set any number inbetween to do more or less placing
blockVsNotBlock = 0.5

#####################

Px,Py,Pz = mc.player.getPos() #establishes coordinates for your position 

# Move it away from the player, but keep it on the ground
centerx = Px + size + 2
centerz = Pz + size + 2
centery = Py

mc.postToChat ("Now lets make a mountain!!  :)")

def rand():
    # returns 1 or 0 randomly
    return int(random.random() + 0.5)

def randBlock():
    # whether to do a random block
    return rand() <= blockVsNotBlock
    
def makeNormalLevel(levelSize, y):
    mc.setBlocks(centerx + levelSize, centery + y, centerz + levelSize, \
                 centerx - levelSize, centery + y, centerz - levelSize, block)
            
def makeScatteredLevel(levelSize, y):
    # make a base at each level
    for x in range(levelSize):
        for z in range(levelSize):
            # go in all four directions
            level = centery + y
            # randomly place or not place on each corner, according to blockVsNotBlock
            if randBlock():
                mc.setBlock(centerx + x, level, centerz + z, block)
            if randBlock():
                mc.setBlock(centerx - x, level, centerz + z, block)
            if randBlock():
                mc.setBlock(centerx + x, level, centerz - z, block)
            if randBlock():
                mc.setBlock(centerx - x, level, centerz - z, block)

# Main loop

for y in range(height):
    # decrease the size as we go up (we need to use fractions in the middle)
    # we subtract from 1 to invert the pyramid
    levelSize = int(size * (1 - (y / float(height))))

    if randomLevels:
        makeScatteredLevel(levelSize, y)
    else:
        makeNormalLevel(levelSize, y)


mc.postToChat ("Ok, done!  Look to your left to see the mountain") #this puts a message in your chat box. within the "" you can change the message. 

#hit F5 to run code! a box will pop up asking you to save the code. hit ok and your code will run!
     
