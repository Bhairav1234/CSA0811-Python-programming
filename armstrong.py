
def isArmstrong(val: int) -> bool:
	"""val will be tested to see if its an Armstrong number. 
	Arguments:
		val {int} -- positive integer only. 
	Returns:
		bool -- true is /false isn't
	"""

	parts = [int(_) for _ in str(val)]

	counter = 0
	for _ in parts:
		counter += _**3
	return (counter == val)


print(isArmstrong(153))

print(isArmstrong(1253))
