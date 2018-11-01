
class User(object):
	var work ##job
	var education ##education status, ex: dropped out, high school, GED, bachelor's, master's, doctorate
	var resources ##socioeconomic status, money, housing, etc.

	def step(self, sequence):
		for i in sequence:
			
