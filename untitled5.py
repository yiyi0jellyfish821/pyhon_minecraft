from mcpi.minecraft import Minecraft as mcs 
import time
mc = mcs .create()
x,y,z = mc.player.getTilePos()
width = 5
Height = 5
lenght = 5
block = 20
air = 0
mc.setBlocks(x,y,z,x+width,y+Height,z+lenght,block)
mc.setBlocks(x+1,y+1,z+1,x+width-1,y+Height-1,z+lenght-1,air)
