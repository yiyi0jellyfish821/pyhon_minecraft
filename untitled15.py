from mcpi.minecraft import Minecraft as mcs 
import time
mc = mcs.create()
x,y,z=mc.player.getTilePos()
nuber=10
for i in range(nuber):
    mc.spawnEntity(x,y,z,60)
    mc.postToChat(str(i+1)+"隻魚")