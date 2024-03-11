def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	try:
		len(height) == len(weight)
	except ValueError:
		print("ArgumentError: List sizes are not matching")
	try:
		type(height) == list[int | float]
		type(weight) == list[int | float]
	except ValueError:
		print("ArgumentError: not the right type")
	
	bmi_list = []
	for i, item in enumerate(height):
		new_value = weight[i] / item ** 2
		bmi_list.append(new_value)

	return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	try:
		type(bmi) == list[int | float]
		type(limit) == int
	except ValueError:
		print("ArgumentError: not the right type")

	boolean_list = []
	for item in bmi:
		if item <= limit:
			boolean_list.append(False)
		else:
			boolean_list.append(True)

	return (boolean_list)
