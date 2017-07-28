import sys
from mcpi.minecraft import Minecraft

import mcpi.block as block

mc=Minecraft.create()

xLast,yLast,zLast =  mc.player.getPos()
while True:
    x,y,z = mc.player.getPos()
  
    block_beneath=mc.getBlock(x,y-1,z)

    
    #eprint block_beneath
    if block_beneath == 00 and x <50 and y <4:
            mc.setBlocks (x+5,y,z-5,x+5,y+1,z+5,11)
            mc.setBlocks (x-5,y,z-5,x-5,y+1,z+5,11)
            mc.setBlocks (x-5,y,z+5,x+5,y+1,z+5,11)
            mc.setBlocks (x-5,y,z-5,x+5,y+1,z-5,11)
    

    if block_beneath == 00 and x >50 and y <4:
            mc.setBlocks (x+5,y,z-5,x+5,y+1,z+5,9)
            mc.setBlocks (x-5,y,z-5,x-5,y+1,z+5,9)
            mc.setBlocks (x-5,y,z+5,x+5,y+1,z+5,9)
            mc.setBlocks (x-5,y,z-5,x+5,y+1,z-5,9)

    
    

