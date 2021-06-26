from mcpi.minecraft import Minecraft as mcs 
import time
mc = mcs.create()
x,y,z=mc.player.getTilePos()
def build(x,y,z,base):
    heigth=(base//2)+1
    for i in range(height):
        x=x=i
        y=y+i
        z=z+i
        x2=x+base-i
        z2=z+base-i
        mc.setblock(x1,y1,z1,x2,y1,z2,24)
        x2,y1,z2=mc.player.getTilePos()   
base=int(input())
bulid(x,y,z,base)