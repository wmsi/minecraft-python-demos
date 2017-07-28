from mcpi.minecraft import Minecraft  #this line of code turns on minecraft
from time import sleep

mc = Minecraft.create()    

flower = 3 #this line of code tells the computer what flower to generate. what willa different number do?

while True:  #this line says "Are you running? if true, generate flowers"
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, flower)
    sleep(0.1)

    #hit F5 while minecraft is open and try it out!
