import random
class Prototype(object):

	def __init__(self, gunType =""):
		
		if gunType == "":
			gunType = random.choice("primary","secondary","heavy")
