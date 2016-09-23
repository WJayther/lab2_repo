# dict_algs.py
def call_gt18(list_of_dict):
	result = set()
	for adult in list_of_dict:
		for infant in adult['children']:
			#print(adult['name'],infant['name'],infant['age'])
			if infant['age'] > 18 :
				result.add(adult['name'])
				break
	
	return result

if __name__ == '__main__':
	ivan = {
		'name': 'ivan',
		'age': 34,
		'children': [{
			'name': 'vasja',
			'age': 12,
		}, {
			'name': 'petja',
			'age': 10,
		}],
	}
	
	darja = {
		'name': 'darja',
		'age': 41,
		'children': [{
			'name': 'kirill',
			'age': 21,
		}, {
			'name': 'pavel',
			'age': 15,
		}],
	}
	
	emps = [ivan, darja]
	print(call_gt18(emps))
