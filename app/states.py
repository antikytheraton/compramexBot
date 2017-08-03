def checkFile(file_txt,var):
	try:
		file=open(file_txt,'r')
	except:
		file=open(file_txt,'w')
		file.write(var)

def readState(file_txt):
	print(file_txt)
	file=open('states.txt','r')
	content=file.readline()
	print("contenido del archivo")
	print(content)
	return content

def overwriteState(file_txt,ID):
	file = open(file_txt, "w")
	file.write(str(ID))
	file.close()

checkFile("states.txt","10")
