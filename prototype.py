import random
class prototype(object):

	def __init__(self, gunType =""):
		
		if gunType == "":
			gunType = random.choice("primary","secondary","heavy")
