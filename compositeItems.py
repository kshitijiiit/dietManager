import os

class composite(object):

	@staticmethod
	def calori():


	@staticmethod
	def storeFood(name, items, quantity, keywords):
		food = load()
		fp = open("./files/compositeItems.csv", 'a+')
		fp.write("\"" + name + "\",\"")
		for i in range(len(keywords)):
			fp.write(keywords[i])
			if i is not len(keywords):
				fp.write(",")
		fp.write("\"")
		

		fp.close()



