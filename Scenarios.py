# -*- coding: utf-8 -*-

success = 0 # Measure of user's success in life

class Question():
	# Question simulates a scenario with options being presented to the user

	def __init__(self):
		# Each question has a scenario text and options text

		# School scenario
		self.school = """Scenario: You're overwhelmed with coming out and the ramifications of that on top of school./nIn the wake of a very difficult semester, you are on academic probation and have to decide how to move forward.
		/nOption 1 - Drop out and find a job to live on
		/nOption 2 - Try to finish on time at the recommended pace of 12-15 credits per semester
		/nOption 3 - Switch to a part-time course load to make things more manageable, but take much longer to get a living wage"""

		# Job scenario
		self.job = """Scenario: You're applying for a job and must choose an industry and company that will have an accepting environment but also be sustainable for you to live on.
		/nOption 1 - Something creative, probably freelance or short-term contract-based
		/nOption 2 - Something stable, probably corporate but pays decently
		/nOption 3 - Whatever you can find - retail, food service, etc."""

		# Housing scenario
		self.housing = """Scenario: You're looking to rent an apartment or house with your partner. You need to choose a neighborhood and type of landlord.
		/nOption 1 - Private landlord with one-bedroom apartment.
		/nOption 2 - Move in with friends or strangers who have an opening in an affordable apartment.
		/nOption 3 - Property management company with more expensive one-bedroom apartment. """

	# Function to present question and reassess success variable
	def ask_question(question):
		print question.text
		choice = raw_input().lower()
		if choice == "option 1":
			success += 2
		elif choice == "option 2":
			success += 3
		elif choice == "option 3":
			success += 4
		else:
			print "Input is not a valid option."
			ask_question(question)

Question(self.school)
Question(self.job)
Question(self.housing)

if success >= 10:
		print("Congratulations! You scraped your way through adversity and into a comfortable life")
	if success >= 5 and < 10:
		print("You've struggled through a lot and are still struggling. You don't know when or if things will get better but while you're waiting for your miracle, you've just gotta keep going")
	if success < 5:
		print("You've struggled and fallen more times than you can count. You feel like the world was built against you - it's left you marginalized, defeated, and homeless")
