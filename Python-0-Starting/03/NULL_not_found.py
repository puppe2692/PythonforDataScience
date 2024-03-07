import math

def NULL_not_found(object: any) -> int:
	if (object == None):
		print ("Nothing: " + str(object) + " " + str(type(object)))
	elif (object == 0 and type(object) != bool):
		print ("Zero: " + str(object) + " " + str(type(object)))
	elif (object == ''):
		print ("Empty: " + str(object) + " " + str(type(object)))
	elif (object == False):
		print ("Fake: " + str(object) + " " + str(type(object)))
	elif (type(object) != str and math.isnan(object)):
		print ("Cheese: " + str(object) + " " + str(type(object)))
	else:
		print("Type not Found")
		return 1
	return 0
	