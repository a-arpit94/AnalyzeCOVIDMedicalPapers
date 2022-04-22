from Providers.CosmosDBProvider import CosmosDBProvider

def updateStringToList():
	dbDataDic = CosmosDBProvider().getData()
	for item in dbDataDic:
		print(item.get('authors'))
	# print (dbData)


def Convert(string):
	li = list(string.split())
	return li

# Driver code	
str1 = "Geeks-for-Geeks"
s = [str1]
print(s)
# print(Convert(str1))

# updateStringToList()