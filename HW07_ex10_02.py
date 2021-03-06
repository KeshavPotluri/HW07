# I want to be able to call capitalize_nested from main w/ various lists 
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested_withoutLC(listOfLists):
	newList = list()
	for item in listOfLists:
		if type(item) == type(list()):
		 	newNestedList =	capitalize_nested(item)
		 	newList.append(newNestedList)
		else:
			newList.append(item.capitalize())
	return newList

def capitalize_nested(listOfLists):
	newList = [capitalize_nested(word) if type(word) is list else word.capitalize() for word in listOfLists]
	return newList

def main():
	pass	

if __name__ == '__main__':
    main()