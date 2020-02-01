import os, pefile
current = "./"
files = os.listdir(current)
count = 0
for file in files:
	if (file[3] == "u"):
		try:
			ppath = os.path.join(current, file)
			pe = pefile.PE(ppath)
		except:
			os.remove(file)
		count = count + 1
		print(count)