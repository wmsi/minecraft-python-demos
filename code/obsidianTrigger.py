import sys
from mcpi.minecraft import Minecraft

import mcpi.block as block

mc=Minecraft.create()

while True:
    x,y,z = mc.player.getPos()
    block_beneath=mc.getBlock(x,y-1,z)
    print block_beneath
    if block_beneath == 35:
        mc.setBlocks (x+5,y,z,x+5,y+3,z+5,4)

        
