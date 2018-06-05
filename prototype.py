import random
class prototype(object):

	def __init__(self, gunType =""):
		
		if gunType == "":
			gunRan = random.randint(1,3)
			
			if gunRan == 1:
				gunType = "primary"
			elif gunRan == 2:
				gunType = "secondary"
			elif gunRan == 3:
				gunType = "heavy"
