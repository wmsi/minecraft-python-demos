import sys
from mcpi.minecraft import Minecraft
import random 

import mcpi.block as block

mc=Minecraft.create()
r = 0
rok = False
xLast,yLast,zLast =  mc.player.getPos()
while True:
    x,y,z = mc.player.getPos()
  
    block_beneath=mc.getBlock(x,y-1,z)
    while rok == False:
        r = random.randint(1, 60)
        if r != 29 and r != 36 and r != 55 and r != 19 and r != 28 and r != 27 and r != 52 and r != 32 and r != 34 and r != 8 and r != 9 and r != 10 and r != 11 and r!= 25 and r != 23 and r != 33:
            rok = True
    print r
    #eprint block_beneath
    if block_beneath == 00 and y <5:
            mc.setBlocks (x+5,y,z-5,x+5,y+3,z+5,r)
            mc.setBlocks (x-5,y,z-5,x-5,y+3,z+5,r)
            mc.setBlocks (x-5,y,z+5,x+5,y+3,z+5,r)
            mc.setBlocks (x-5,y,z-5,x+5,y+3,z-5,r)
    
    rok = False
