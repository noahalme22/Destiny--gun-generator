#Noah ALmeida / Xavier Langavin
#25/05/2018
#Destiny Gun Generator

import random,prototype
class heavy(prototype.prototype):
	'''primary weapon generator'''

	def __init__(self,gunType1 = "",rocket = "", grenade = "", sword = "", machine = ""):
	

		if gunType1 == "heavy":
				typeRan1 = random.randint(1,4)
			
				if typeRan1 == 1:
					gunType1 = rocket
					
				elif typeRan1 == 2:
					gunType1 = grenade
					
				elif typeRan1 == 3:
					gunType1 = sword

				elif typeRan1 == 4:
					gunType1 = machine
					
	
		self.gunType1 = gunType1		
		self.rocket = rocket
		self.grenade = grenade
		self.sword = sword
		self.machine = machine
			