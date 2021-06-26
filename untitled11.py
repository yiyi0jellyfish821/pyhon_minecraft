from mcpi.minecraft import Minecraft as mcs 
import time
mc = mcs .create()
while True:
    hits = mc.events.pollProjectileHits()
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x,hit.pos.y,hit.pos.z
        #mc player.setpos(x,y,z)
        mc.createExplosion(x,y,z,10)