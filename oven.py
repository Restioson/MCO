import os, thread, sys, Oven_Dependency_Scripts, time  #Import 'os', 'thread' and 'sys'
try:
	sys.stdout = open('mods.log','w')
except:
	pass
cdir = os.listdir('./_mods') #Get all files in '_mods' directory
while True:
	if Oven_Dependency_Scripts.test_for_open.DoesServiceExist('localhost',4711) == True:
		break
	else:
		time.sleep(5)
for file in cdir: #Loop
	splitfl = file.split('.')
	splitfl.reverse()
	if splitfl[0]  == 'py' or splitfl[0]  == 'pyw': #If they are python files:
		os.system('python ./_mods/'+file+' &')
		try:
			print('Mod "'+file.split('.')[0]+'" has been succesfully loaded')
		except:
			pass



#Troubleshooting
#print(cdir) // Uncomment for troubleshooting
	
