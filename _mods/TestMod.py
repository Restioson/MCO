print('[Info] TestMod has started...') #Tell the user that the mod has started

import sys #Import the 'sys' module
import mcpi.minecraft as minecraft #Import the minecraft api
import mcpi.block as block
import api #Import the OvenApi

mc = minecraft.Minecraft.create() #Connect to minecraft
api.general.msg('TestMod has been successfully enabled',mc)
api.general.msg('(This is just a testmod, uninstall it if you wish!)')
api.multiplayer.togglenames(mc, False)
api.general.msg('TestMod has disabled nametags')
state_immutable = False
while True:
		hit = api.event.getHit(mc)
		if str(hit) != 'None':
				api.general.msg('You clicked at '+str(hit[0])+','+str(hit[1])+','+str(hit[2]), mc)
				api.general.msg('Your position is: '+str(api.player.getPos().x)+str(api.player.getPos().y)+str(api.player.getPos().z)
				api.general.msg('Oops!Sorry!')
				api.player.setPos(api.player.getPos().x, api.player.getPos().y + 50, api.player.getPos().x)
				if state_immutable == False:
					api.general.set_immutable(True, mc)
					api.general.msg('Your world is now immutable')
				else:
					api.general.msg('Your world is no longer immutable')
					api.general.set_immutable(False, mc)

print('[Info] TestMod has ended...')#Tell the user that the program has ended (uninplemented)
#EndOfMod
