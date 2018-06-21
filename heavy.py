#Noah ALmeida / Xavier Langavin
#25/05/2018
#Destiny Gun Generator

import random,prototype
class Heavy(prototype.Prototype):
	'''heavy weapon generator'''

	def __init__(self,gunType = ""):
                super().__init__()
                self.gun = gunType

                if gunType == "":
                        self.gun = random.choice(['sword','rocket launcher','grenade launcher','machine gun'])

	def __str__(self):
                return "\nGunType: "+str(self.gun)
		
					

			
