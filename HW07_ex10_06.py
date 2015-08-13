# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted_withoutLC(listOfList):
	maxCount = len(listOfList)
	for n in range(maxCount - 1):
		if listOfList[n] > listOfList[n + 1]:
			return False
	return True

def is_sorted(listOfList):
	return all(listOfList[i] > listOfList[i-1] for i in range(1, len(listOfList)))

def main():
	pass

if __name__ == '__main__':
    main()
