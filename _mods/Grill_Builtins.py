print('[Info] Grill_Builtins has started...') #Tell the user that the mod has started

import sys #Import the 'sys' module
import mcpi.minecraft as minecraft #Import the minecraft api
import mcpi.block as block
import api #Import the OvenApi

mc = minecraft.Minecraft.create() #Connect to minecraft

api.general.msg('GrillTools has been successfully enabled', mc)
while True:
	hit = api.event.getHit(mc)
	api.general.msg('You clicked at '+str(hit[0])+', '+str(hit[1])+', '+str(hit[2])+' on a/n 'str(dir(block.Block(hit[4])))+' Block')
	print('[Info] Grill_Builtins has ended...')#Tell the user that the program has ended
#EndOfMod
