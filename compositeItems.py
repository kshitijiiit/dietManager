import os

from load import load

class composite(object):

	@staticmethod
	def calorie(items, quantity):
		food = load()
		totalCal = 0
		totalQuantity = 0
		for i in range(len(items)):
			for j in range(len(food.items)):
				l = food.items[j].split(',')
			 	if l[0].split('\"')[1] == items[i]:
			 		totalCal = totalCal + int(l[2].split("\"")[1]) * int(quantity[i])
			 		totalQuantity = totalQuantity + int(quantity[i])
		
		return ( float(totalCal) / float(totalQuantity) )

	def storeFood(self, name, items, quantity, keywords):
		fp = open("./files/compositeItems.csv", 'a+')
		fp.write("\"" + name + "\",\"")
		for i in range(len(keywords)):
			fp.write(keywords[i])
			if i is not len(keywords) - 1:
				fp.write(":")
		fp.write("\",\"" + str(self.calorie(items, quantity)) + "\",\"")
		for i in range(len(items)):
			fp.write(items[i])
			if i is not len(items) - 1:
				fp.write(":")
		fp.write("\",\"")
		for i in range(len(quantity)):
			fp.write(quantity[i])
			if i is not len(quantity) - 1:
				fp.write(":")
		fp.write("\"\n")
		fp.close()

	@staticmethod
	def deleteFood(name):
		l = ""
		fp = open("./files/compositeItems.csv", 'a+')
		for line in fp:
			if (line.split(','))[0].split('\"')[1] != name:
				l = l + line
			else:
				print "Entry Deleted!", line,
		fp.close()
		os.remove("./files/compositeItems.csv")
		fp = open("./files/compositeItems.csv", 'w+')
		fp.write(l)
		fp.close()


a = composite()
b = ['orange', 'jam']
c = ['1','2']
d = ['milk', 'cold']
a.storeFood("shake", b, c, d)
a.deleteFood("shake")
