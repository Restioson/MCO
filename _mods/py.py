print('[Info] Foo has started...')
import sys
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

mc.postToChat('Foo has started!!!!!!')
print('[Info] Foo has ended...')
sys.exit(0)
#EndOfMod
