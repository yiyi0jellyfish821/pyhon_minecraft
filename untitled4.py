from mcpi.minecraft import Minecraft as mcs 
import time
mc = mcs .create()
x,y,z=mc.player.getTilePos()
print(x,y,z)
mc.setBlocks(x+1,y,z+1,x-1,y,z-1,46)
mc.setBlock(x,y,z,0)