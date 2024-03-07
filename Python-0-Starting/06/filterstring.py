import sys
from ft_filter import ft_filter


def filterstring(str: str, nbr: int):

	word_list = str.split(' ')
	greater_words = ft_filter(lambda word: len(word) > nbr, word_list)
	greater_list = [item for item in greater_words]

	if len(greater_list) < 1:
		print("[]")
	else:
		print(greater_list)


def main():
	if (len(sys.argv) != 3):
		print("AssertionError: the arguments are bad")
		return 1
	elif (type(sys.argv[1]) != str):
		print("AssertionError: the arguments are bad")
		return 1
	else:
		try:
			sys.argv[2] = int(sys.argv[2])
		except ValueError:
			print("AssertionError: the arguments are bad")
		filterstring(sys.argv[1], sys.argv[2])


if (__name__ == "__main__"):
	main()