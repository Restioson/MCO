#Event
def getHit(mc):
        "Returns first event's pos then, the entityID of who caused the hit and then the block ID."

        blockEvents = mc.events.pollBlockHits()
        if len(blockEvents)>0:
                return ( blockEvents[0].pos.x, blockEvents[0].pos.y, blockEvent[0].pos.z, blockEvents[0].entityId, mc.getBlock(blockEvents[0].pos.x, blockEvents[0].pos.y, blockEvents[0].pos.z) )

def clear(mc):
        mc.events.clearAll()

