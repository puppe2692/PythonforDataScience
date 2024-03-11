def count_in_list(object: list, str: str) -> int:
	return sum(1 for s in object if s == str)