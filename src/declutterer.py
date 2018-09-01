from poly1305_donna import *
from os import listdir, remove
from os.path import isfile, join
import optparse

def declutter(directoryName):
	images = getImages(directoryName)
	imageHash = getHashList(images, directoryName)
	duplicates = getDuplicate(images, imageHash)
	deleteDuplicate("test_images", duplicates)
	return

def deleteDuplicate(directoryName, duplicates):
	directoryPath = "./" + directoryName
	print ("Deleting...")
	for img in duplicates:
		print (img)
		os.remove(directoryPath + "/" + img)
	print (len(duplicates), "files deleted.")


def getDuplicate(images, imageHash):
	duplicates = []
	i = 0
	for hash in imageHash:
		if countOccurence(imageHash, hash) > 1:
			duplicates.append(images[i])
			images.remove(images[i])
			imageHash.remove(imageHash[i])
		i += 1

	return duplicates

def getHashList(images, directoryName):
	imageHash = []
	key = get_key()
	for img in images:
		imgPath = "./" + directoryName + "/" + img
		imageHash.append(getHash(key, imgPath))
	return imageHash

def countOccurence(lst, elem):
	count = 0
	for element in lst:
		if element == elem: count += 1
	return count

def getImages(directoryName):
	directoryPath = "./" + directoryName
	images = [img for img in listdir(directoryPath) if isfile(join(directoryPath, img))]
	return images

def getHash(key, imagePath):
	image = open(imagePath, 'r')
	content = image.read()
	image.close()
	return authenticate(key, content)

if __name__ == '__main__':
	# parse command line arguments
	parser = optparse.OptionParser(usage="%prog Directory")
	options, args = parser.parse_args()
	if len(args) < 1:
		parser.error("No directory argument")
	else:
		directoryName = args[0]
		if not os.path.isdir(directoryName):
			parser.error("Directory not found")
		declutter(directoryName)
