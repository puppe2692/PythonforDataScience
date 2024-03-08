import sys

NESTED_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ' ': '/ '
}

def morseconverter(str: str):
	for i, item in enumerate(str):
		morse_code = NESTED_MORSE.get(item.upper())
		print(morse_code, end=' ' if i < len(str) - 1 else '\n')
	

def main():
	if (len(sys.argv) != 2):
		print("AssertionError: the arguments are bad")
		return 1
	else:
		try:
			if not all(c.isalnum() or c.isspace() for c in sys.argv[1]):
				raise ValueError("AssertionError: the argument is not alphanumeric")
		except ValueError as e:
			print(e)
			return 1
		morseconverter(sys.argv[1])


if (__name__ == "__main__"):
	main()