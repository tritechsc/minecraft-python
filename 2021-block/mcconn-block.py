from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
# set player to 0,0,0
mc.player.setPos(0,0,0)
# CLEAR AN AREA WITH AIR TO BUILD
air = 0
mc.setBlocks(-19,0,-19,19,64,19,air) # clear some air                                               
x, y, z = mc.player.getPos()
xyzString = str(x)+" , "+str(y)+" , "+str(z)
print(xyzString)
# mc.setBlock (x,y,z, material_number) 

#this is going to be more but I need to learn more first, I will come back to this but it is a shape so whatever
#  Bottom Left Shape #black
mc.setBlock(-15,41,2,35,15)
mc.setBlock(-15,40,2,35,15)
mc.setBlock(-15,39,2,35,15)
mc.setBlock(-15,38,2,35,15)
mc.setBlock(-15,37,2,35,15)
mc.setBlock(-15,36,2,35,15)
mc.setBlock(-15,35,2,35,15)
mc.setBlock(-15,34,2,35,15)
mc.setBlock(-15,33,2,35,15)
mc.setBlock(-15,32,2,35,15)
mc.setBlock(-15,31,2,35,15)
mc.setBlock(-15,30,2,35,15)
mc.setBlock(-15,29,2,35,15)
mc.setBlock(-15,28,2,35,15)
mc.setBlock(-15,27,2,35,15)
mc.setBlock(-15,26,2,35,15)
mc.setBlock(-15,25,2,35,15)
mc.setBlock(-15,24,2,35,15)
mc.setBlock(-15,23,2,35,15)
mc.setBlock(-15,22,2,35,15)
mc.setBlock(-15,21,2,35,15)
mc.setBlock(-14,20,2,35,15)
mc.setBlock(-13,19,2,35,15)
mc.setBlock(-12,18,2,35,15)
mc.setBlock(-11,17,2,35,15)
mc.setBlock(-10,16,2,35,15)
mc.setBlock(-9,15,2,35,15)
mc.setBlock(-8,14,2,35,15) 
mc.setBlock(-7,13,2,35,15)
mc.setBlock(-6,12,2,35,15)
mc.setBlock(-5,11,2,35,15)
mc.setBlock(-4,10,2,35,15)
mc.setBlock(-3,9,2,35,15)	
mc.setBlock(-2,8,2,35,15)	 
mc.setBlock(-1,7,2,35,15)	 
mc.setBlock(0,6,2,35,15)	
mc.setBlock(1,5,2,35,15) 	
mc.setBlock(2,4,2,35,15) 	
mc.setBlock(3,3,2,35,15) 	
mc.setBlock(4,2,2,35,15)  	
mc.setBlock(5,1,2,35,15)
mc.setBlock(6,2,2,35,15)
mc.setBlock(6,3,2,35,15)
mc.setBlock(6,4,2,35,15)
mc.setBlock(6,5,2,35,15)
mc.setBlock(6,6,2,35,15)
mc.setBlock(6,7,2,35,15)
mc.setBlock(6,8,2,35,15)
mc.setBlock(6,9,2,35,15)
mc.setBlock(6,10,2,35,15)
mc.setBlock(6,11,2,35,15)
mc.setBlock(6,12,2,35,15)
mc.setBlock(6,13,2,35,15)
mc.setBlock(6,14,2,35,15)
mc.setBlock(6,15,2,35,15)
mc.setBlock(6,16,2,35,15)
mc.setBlock(6,17,2,35,15)
mc.setBlock(6,18,2,35,15)
mc.setBlock(6,19,2,35,15)
mc.setBlock(6,20,2,35,15)
mc.setBlock(6,21,2,35,15)
mc.setBlock(5,22,2,35,15)
mc.setBlock(4,23,2,35,15)
mc.setBlock(3,24,2,35,15)
mc.setBlock(2,25,2,35,15)
mc.setBlock(1,26,2,35,15)
mc.setBlock(0,27,2,35,15)
mc.setBlock(-1,28,2,35,15)
mc.setBlock(-2,29,2,35,15)
mc.setBlock(-3,30,2,35,15)
mc.setBlock(-4,31,2,35,15)
mc.setBlock(-5,32,2,35,15)
mc.setBlock(-6,33,2,35,15)
mc.setBlock(-7,34,2,35,15)
mc.setBlock(-8,35,2,35,15)
mc.setBlock(-9,36,2,35,15)
mc.setBlock(-10,37,2,35,15)
mc.setBlock(-11,38,2,35,15)
mc.setBlock(-12,39,2,35,15)
mc.setBlock(-13,40,2,35,15)
mc.setBlock(-14,41,2,35,15)

mc.player.setPos(0,0,-5)