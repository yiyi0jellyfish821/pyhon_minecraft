from mcpi.minecraft import Minecraft as mcs 
import time
mc = mcs .create()
import time
import random
while True:
    x,y,z = mc.player.getPos()
    x = x+random.uniform(-20,20)
    z = z+random.uniform(-20,20)
    y = y+30
    mc.spawnEntity(x,y,z,78)
    time.sleep(0.5)
    
    
    