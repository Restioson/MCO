#API
def saveworld(mc):
	mc.saveCheckpoint()
	
def loadworld(mc):
	mc.restoreCheckpoint()
	
def msg(msg, mc):
	mc.postToChat(msg)

#def set_immutable(state, mc):
#	mc.setting('world_immutable', state)
#Bug ^^^ :(
