#Event
def getHit(mc)
	"Returns first event's pos then, the entityID of who caused the hit and then the block ID."
	blockEvents = mc.events.pollBlockHits()
		return ( blockEvents[0].pos.x, blockEvents[0].pos.y, blockEvents[0].pos.z, blockEvents[0].EntityId, mc.getBlock(blockEvents[0].pos.x, blockEvents[0].pos.y, blockEvents[0].pos.z) )

def clear(mc):
	mc.events.clearAll()
