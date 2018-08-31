from hashlib import *

def main():
    print(getHash(b"abcd"))

def getHash(image):
    algorithm = sha256()
    algorithm.update(image)
    return algorithm.hexdigest()

main()
