from mcpi.minecraft import Minecraft as mcs 
import time
mc = mcs.create()
x,y,z = mc.player.getTilePos()
#mc setBlock(x+1,y+3,z+1,x-1,y,z-1,2)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            mc.setBlock(x+i,y+k,z+1,2)
for j in range(3):
     mc.setBlock(z+1,x-1,y-i,z+1,2)