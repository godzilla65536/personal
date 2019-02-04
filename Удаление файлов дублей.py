import os
import hashlib

def sha256(fileName):
	return hashlib.sha256(open(fileName, 'rb').read()).hexdigest()

def delete_files(fileList):
	for file in fileList:
		os.remove(file)

script_path = os.path.split(__file__)[0]
os.chdir(script_path)

filelist = os.listdir(script_path)
filelist.remove(os.path.split(__file__)[1])


duplicate_files = []
hashList = []
for file in filelist:
	Hash = sha256(file)
	if Hash in hashList:
		duplicate_files.append(file)
	else:
		hashList.append(Hash)

delete_files(duplicate_files)
