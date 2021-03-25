def readFile():

	studentList = list()
	#read the file
	readFromFile = open("SortMe.txt", "r")

	#append each name to studentList
	for eachName in readFromFile:
		studentList.append(eachName)
		#print(eachName)

	readFromFile.close()

	sortListNamesReverse(studentList)


def sortListNamesReverse(studentList):
	studentList.sort(reverse=True)
	studentList.sort(key=len, reverse=True)

	###########################
	#for testing purposes only
	printList(studentList)
	###########################

	return studentList

#############################
def printList(thisList):
	for item in thisList:
		print(item)
#############################

if __name__ == '__main__':
	readFile()
