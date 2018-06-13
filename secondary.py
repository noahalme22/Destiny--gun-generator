import random,prototype
class secondary(prototype.prototype):
	'''secondary weapon generator'''

	def __init__(self,gunType="", sidearm = "", fusion = "", sniper = "", shotgun = ""):

			if gunType == "secondary":
				typeRan = random.randint(1,4)
			
				if typeRan == 1:
					gunType = sidearm
					
				elif typeRan == 2:
					gunType = fusion
					
				elif typeRan == 3:
					gunType = sniper

				elif typeRan == 4:
					gunType = shotgun
			
			self.gun = gunType
			self.sidearm = sidearm
			self.fusion = fusion
			self.sniper = sniper
			self.shotgun = shotgun