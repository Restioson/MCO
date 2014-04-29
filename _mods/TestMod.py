print('[Info] TestMod has started...') #Tell the user that the mod has started

import sys #Import the 'sys' module
import mcpi.minecraft as minecraft #Import the minecraft api
import mcpi.block as block
import api #Import the OvenApi

mc = minecraft.Minecraft.create() #Connect to minecraft
api.general.msg('TestMod has been successfully enabled',mc)
api.general.msg('(This is just a testmod, uninstall it if you wish!)', mc)
api.multiplayer.togglenames(mc, False)
api.general.msg('TestMod has disabled nametags', mc)
api.general.saveworld(mc)
while True:
		hit = api.event.getHit(mc)
		if str(hit) != 'None':
				api.general.msg('You clicked at '+str(hit[0])+','+str(hit[1])+','+str(hit[2]), mc)
				api.general.msg('Your position is: '+str(api.player.getPos(mc).x)+str(api.player.getPos(mc).y)+str(api.player.getPos(mc).z), mc)
				api.general.msg('Oops!Sorry!', mc)
				api.player.setPos(mc,(api.player.getPos(mc).x, api.player.getPos(mc).y + 50, api.player.getPos(mc).z))
				api.general.loadworld(mc)
				api.general.msg('World Reset', mc)

print('[Info] TestMod has ended...')#Tell the user that the program has ended (uninplemented)
#EndOfMod
