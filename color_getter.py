import random

def containsSun(lines):
	for l in lines:
		if "sun" in l:
			return True
	return False

def get_color_for_words(lines):
	if containsSun(lines):
		return (1, 1, 0)
	else:
		return (0, 0, 1)
