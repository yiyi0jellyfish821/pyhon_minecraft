def plantTree(x,y,z):
    mc.setBlocks(x+1,y+3,z+1,x-1,y+5,z-1,35)
    mc.setBlocks(x,y,z,x,y+4,z,3)
from mcpi.minecraft import Minecraft as mcs 
import time
mc = mcs.create()
x,y,z = mc.player.getTilePos()
for i in range(10):
    for j in range(10):
            plantTree(x+i*5,y+j*i,z)