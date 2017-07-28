import sys
from mcpi.minecraft import Minecraft

import mcpi.block as block

mc=Minecraft.create()

xLast,yLast,zLast =  mc.player.getPos()
while True:
    x,y,z = mc.player.getPos()
    diffX = x-xLast
    diffZ = z-zLast
   
    if (diffX) != 0:
        signX =  (x-xLast)/abs(x-xLast)

    if (diffZ) != 0:
        signZ = (z-zLast)/abs(z-zLast)

  
    block_beneath=mc.getBlock(x,y-1,z)
    #eprint block_beneath
    if block_beneath == 35:
            mc.setBlocks (x+5,y,z-5,x+5,y+3,z+5,4)
            mc.setBlocks (x-5,y,z-5,x-5,y+3,z+5,4)
            mc.setBlocks (x-5,y,z+5,x+5,y+3,z+5,4)
            mc.setBlocks (x-5,y,z-5,x+5,y+3,z-5,4)

    if block_beneath == 5:
            mc.setBlocks (x+5,y,z-5,x+5,y+3,z+5,46,1)
            mc.setBlocks (x-5,y,z-5,x-5,y+3,z+5,46)
            mc.setBlocks (x-5,y,z+5,x+5,y+3,z+5,46,1)
            mc.setBlocks (x-5,y,z-5,x+5,y+3,z-5,46)

    xLast,yLast,zLast = x,y,z
    
