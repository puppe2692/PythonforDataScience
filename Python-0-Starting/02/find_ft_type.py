def all_thing_is_obj(object: any) -> int:
	if (type(object) == str):
		print(object + " is in the kitchen : " + str(type(object)))
	elif (type(object) == int):
		print("type not found")
	else:
		print((type(object).__name__) + " : " + str(type(object)))
	return 42