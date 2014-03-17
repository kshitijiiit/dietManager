import os

class log(object):
	
	def sotreLog(self,user, date, month, year, item,calory):

			string = '"' + item + '","' + calory + '"' + '\n';

			path = os.path.join(os.getcwd())+"/files/logs/"+user;
			check=os.path.exists( path);

			if(check == False):
				os.mkdir(path);

			path = path + "/" + date + "-" + month + "-" + year + ".csv";

			fp = open( path , 'a+');
			fp . writelines(string);
			fp.close();

	def view(self, user, date, month, year):
		path = os.path.join(os.getcwd())+"/files/logs/"+user+"/" + date + "-" + month + "-" + year + ".csv";
		check=os.path.exists( path);
		loglist="";
		if check==True :
			fp = open(path, 'r');
			for line in fp:
				loglist += line;
			fp.close();
		print loglist,

	def modify(self, user, date, month, year, item, newcal):
			path = os.path.join(os.getcwd())+"/files/logs/"+user+"/" + date + "-" + month + "-" + year + ".csv";
			item = '"' + item + '"';
			fp = open(path, 'r+');
			data="";
			cont=0;
			for line in fp:
				cont+=1;
				ln=line;
				ln = ln.split(',');
				if item==ln[0]:
					data += item + ',"' + newcal +'"\n';
				else :
					data += line;
			fp.close();
			fp = open(path, 'w+');
			fp.write(data);
			fp.close();
	
obj = log();
obj.sotreLog("rishav", "12", "12", "2014","item", "120");
obj.sotreLog("rishav", "12", "12", "2014","item", "120");
obj.sotreLog("rishav", "12", "12", "2014","item", "120");
obj.sotreLog("rishav", "12", "12", "2014","item", "120");
obj.sotreLog("rishav", "12", "12", "2014","item", "120");
obj.sotreLog("rishav", "12", "12", "2014","item", "120");
obj.view("rishav", "12", "12", "2014");
obj.modify("rishav", "12", "12", "2014","item","200");

