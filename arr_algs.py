# arr_algs.py
def find_min(array):
	min = array[0]
	for i in array:
		if i < min: 
			min = i
	
	return min

def find_avrg(array):
	result = 0.0
	for i in array:
		result += i
	return result/len(array)

if __name__ == '__main__':
	test = [167, 1234, -12, -34, 99]
	print(find_min(test))
	print(find_avrg(test))
