edges = [
	{
		'min': 0,
		'max': 50000000,
		'rate': 5
	},
	{
		'min': 50000000,
		'max': 250000000,
		'rate': 15
	},
	{
		'min': 250000000,
		'max': 500000000,
		'rate': 25
	},
	{
		'min': 500000000,
		'max': 0,
		'rate': 30
	}
]

def count_tax(number):
	payable = 0
	residue = number
	
	for k in edges:
		factor = k['max'] - k['min'] if k['max'] > 0 else k['min']
		if number > k['min']:
			if residue >= factor and k['max'] > 0:
				payable += factor * k['rate'] / 100
				residue = residue - factor
			else:
				payable += residue * k['rate'] / 100
			
	return payable

def main():
	number = input("Please enter your income: ")
	print "your tax is: {:,}".format(count_tax(number))

if __name__ == '__main__':
	main()