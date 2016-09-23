# str_algs.py
def swap_string(string):
	output = str()
	for i in string:
		output = i + output
	
	return output

if __name__ == '__main__':
	test = "How can we swap a string?"
	print(swap_string(test))
