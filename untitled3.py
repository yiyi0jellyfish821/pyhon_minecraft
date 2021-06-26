from mcpi.minecraft import Minecraft as mcs 
import time
mc = mcs .create()
x,y,z=mc.player.getTilePos()
print(x,y,z)
i=0
x=x+10
while i<3:
    mc.setBlock(x+i,y+1,z,152)
    mc.setBlock(x+i,y,z,46)
    i=i+1