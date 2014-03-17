import os

from load import load

class basic(object):

	@staticmethod
	def storeFood(name, energy, keywords=""):
		fp = open("./files/basicItems.csv", 'a+')
		fp.write("\"" + name + "\",\"")
		for i in range(len(keywords)):
			fp.write(d[i])
			if i is not len(keywords) - 1:
				fp.write(",")
		fp.write("\",\"" + energy +"\"\n")
		fp.close()

	@staticmethod
	def readFood(name):
		fp = open("./files/basicItems.csv", 'r+')
		for line in fp:
			copy = line
			l = line.split(',')
			l = l[0].split("\"")
			if l[1] == name:
				print copy
				return
		print "No match found!!!"
			
		fp.close()

	@staticmethod
	def deleteFood(name):
		ans = ""
		fp = open("./files/basicItems.csv", 'r+')
		for line in fp:
			copy = line
			l = line.split(',')
			l = l[0].split("\"")
			if l[1] != name:
				ans = ans + copy
		        else:
				print "Match Found!!! Entry Deleted!!!"

		fp.close()
		os.remove("./files/basicItems.csv")
		fp = open("./files/basicItems.csv", 'w+')
		fp.write(ans)
		fp.close()


#a = basic()
#a.storeFood("ddsd", "122")
#a.readFood("jam")
#a.deleteFood("jam")
b = load()
print b.items	
