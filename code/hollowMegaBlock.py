import sys
from mcpi.minecraft import Minecraft

import mcpi.block as block

mc = Minecraft.create()


mc.setBlocks(0,0,0,20,20,20,4)

mc.setBlocks(1,1,1,19,19,19,0)
mc.setBlocks(10,5,10,15,9,15,20)
mc.setBlocks (11,6,11,14,8,14,0)
mc.setBlocks (5,0,1,5,0,19,49)

#for x in range (1,19):
 #       for y in range (1,19):
  #              if (x%5==0 and y%5==0):
   #                      mc.setBlock (x,y,1,50)
    #                mc.setBlock (x,y,19,50)
                                 
#for z in range (1,19):
 #       for y in range (1,19):
  #              if (z%5==0 and y%5==0):
   #                           mc.setBlock (1,y,z,50)
    #                   mc.setBlock (1          9,y,z,50)
                

outside = 1

print ("start loop...Outside = ",outside)

while outside == 1:
        x,y,z = mc.player.getPos()
        block_beneath = mc.getBlock(x,y-1,z)
        print ("Block = ", block_beneath, "  outside = ", outside) 
        if block_beneath == 49:

                for x in range (10,15):
                        for y in range (5,9):
                                if (x%2==0 and y%2==0):
                                         mc.setBlock (x,y,10,50)
                                         mc.setBlock (x,y,15,50)
                         
                for z in range (10,15):
                        for y in range (5,9):
                                if (z%2==0 and y%2==0):
                                         mc.setBlock (10,y,z,50)
                                         mc.setBlock (15,y,z,50)
                

                


