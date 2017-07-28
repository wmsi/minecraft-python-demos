from mcpi.minecraft import Minecraft  #this line tells the computer to connect to minecraft. don't mess with it

mc = Minecraft.create()

mc.postToChat ("Hello, WMSI Mobile STEM Explorers!!")

block = 10   # Change this number to change the block type

size = 2  # Change this number to change the number of blocks per size
          # for our MEGA Block placement

x,y,z = mc.player.getPos() #establishes coordinates for your position 


x2= x + 1 # replace "1" with a different number to make your block wider!
y2=y + 1  # replace "1" with a different number to make your block Taller!
z2= z + 1 # replace "1" with a different number to make your block wider in 3D!

mc.postToChat ("Now lets put down a MEGA Block!!  :)")


# The MEGA block command ... places a megablock to your left
mc.setBlocks(x+1,y+1,z+1,x2,y2,z2,block)


mc.postToChat ("Ok! Ready?  Look to your left to see the MEGA Block!") #this puts a message in your chat box. within the "" you can change the message. 

#hit F5 to run code! a box will pop up asking you to save the code. hit ok and your code will run!
     
