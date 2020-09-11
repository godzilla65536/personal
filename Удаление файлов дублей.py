import os
import hashlib

def sha256(fileName):
	return hashlib.sha256(open(fileName, 'rb').read()).hexdigest()

def delete_files(fileList):
	for file in fileList:
		os.remove(file)

workDir = input('Specify the path with duplicate files: ')

fileList = [os.path.join(workDir, fileName) for fileName in os.listdir(workDir) if os.path.isfile(os.path.join(workDir, fileName))]

duplicate_files = []
hashList = []
for file in fileList:
	Hash = sha256(file)
	if Hash in hashList:
		duplicate_files.append(file)
	else:
		hashList.append(Hash)

print('Duplicate files found: ' + str(len(duplicate_files)))

if len(duplicate_files) != 0:

    print('Duplicate files:')
    for fileName in duplicate_files:
        print('\t' + fileName)

    confirm = input('Delete these duplicate files? [y/n]: ')

    if confirm == 'y':
        delete_files(duplicate_files)
        print('Deletion finished')
    else:
        print('Deletion not confirmed')
