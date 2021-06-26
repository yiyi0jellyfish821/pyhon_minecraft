from mcpi.minecraft import Minecraft as mcs 
import time
mc = mcs.create()
x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z,63,0,"I love minecraft",\
           "","and Pyhon")