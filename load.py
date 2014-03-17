import os

class load(object):

	#Loading the food items
	def __init__(self):
		self.items = []
		items = []
		fp = open("./files/basicItems.csv", 'a+')
		for line in fp:
			items.append(line.split("\n")[0])
		fp.close()
		fp = open("./files/compositeItems.csv", 'a+')
		for line in fp:
			items.append(line.split("\n")[0])
		fp.close()
		self.items = items

a = load()
print a.items
