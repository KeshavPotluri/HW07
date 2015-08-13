# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum_withoutLC(nested_lists):
	sumOfNumbers = 0
	for item in nested_lists:
		if type(item) == type(list()):
			sumOfNumbers += nested_sum(item)
		else:
			sumOfNumbers += item
	return sumOfNumbers
			
def nested_sum(nested_lists):
	new_list = [nested_sum(item) if type(item) is list else item for item in nested_lists]
	return sum(new_list)

def main():


	pass

if __name__ == '__main__':
    main()
