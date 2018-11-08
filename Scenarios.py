def game(scenario):
	success = 0 #measure of user's success in life
	
	if game("school"):
	#scenario - You're overwhelmed with coming out and the ramifications of that on top of school.
	#In the wake of a very difficult semester, you are on academic probation and have to decide how to move forward.
	#option 1 - Drop out and find a job to live on
	#option 2 - Try to finish on time at the recommended pace of 12-15 credits per semester
	#option 3 - Switch to a part-time course load to make things more manageable
		if raw_input.lower() == "option 1":
		
		elif raw_input.lower() == "option 2":
		
		elif raw_input.lower() == "option 3":
			success += 5
		else:
			raise typeError "Input is not an option."
		
	elif game("job"):
	#scenario - You're applying for a job and must choose an industry and company that will have an accepting environment
	#but also be sustainable for you to live on.
	#option 1 - Something creative, probably freelance or short-term contract-based
	#option 2 - Something stable, probably corporate but pays decently
	#option 3 - Whatever you can find - retail, food service, etc.
		if raw_input.lower() == "option 1":
		
		elif raw_input.lower() == "option 2":
		
		elif raw_input.lower() == "option 3":
		
		else:
			raise typeError "Input is not an option."
			
	elif game("relationship")
	#scenario - You're looking to date but aren't sure where to find someone
	#option 1
	#option 2
	#option 3
		if raw_input.lower() == "option 1":
		
		elif raw_input.lower() == "option 2":
		
		elif raw_input.lower() == "option 3":
		
		else:
			raise typeError "Input is not an option."

	if success >= 10:
		print "Congratulations! You scraped your way through adversity and into a comfortable life"
	if success >= 5 and < 10:
		print "You've struggled through a lot and are still struggling. You don't know when or if things will get better but while you're waiting for your miracle, you've just gotta keep going"
	if success < 5:
		print "You've struggled and fallen more times than you can count. You feel like the world was built against you - it's left you marginalized, defeated, and homeless"