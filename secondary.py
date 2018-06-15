import random,prototype
class Secondary(prototype.Prototype):
	'''secondary weapon generator'''

	def __init__(self,gunType = ""):
                super().__init__()
                self.gun = gunType
                
                if gunType == "":
                        self.gun = random.choice(["shotgun","sniper","fusion","sidearm"])
				
			
			
