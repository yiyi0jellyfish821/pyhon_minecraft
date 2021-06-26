from mcpi.minecraft import Minecraft as mcs 
import time
mc = mcs .create()
x,y,z = mc.player.getTilePos()
print(x,y,z)
mc.setBlock(x+1,y+1,z146)
（