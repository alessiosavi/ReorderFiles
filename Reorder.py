import glob
import os
import shutil
import time
from pathlib import Path

# root_path is your user home directory
root_path = str(Path.home())
pathToSearchIn = os.path.join(root_path, '/Downloads')


def get_folder_size():
	folderSize = len([file for file in glob.glob(glob.escape(pathToSearchIn) + '/**/*', recursive=True)])
	return folderSize


def sizeChecker(sleep_time: int = 10):
	oldFolderSize = get_folder_size()
	print("Folder size (old size): {} Elements".format(oldFolderSize))
	time.sleep(sleep_time)  # in seconds
	newFolderSize = get_folder_size()
	print("Folder size (new size): {} Elements".format(newFolderSize))
	if newFolderSize > oldFolderSize:
		print("Changes detected!")
		reOrderFiles()
	else:
		print("No changes!")
	sizeChecker()  # run again the function after time set


def divideFiles():
	listOfFiles = glob.glob(pathToSearchIn + '/*')
	latestFile = max(listOfFiles, key=os.path.getmtime)
	print(latestFile)
	return latestFile


def reOrderFiles():
	newFile = divideFiles()
	# PDF files
	if newFile.lower().endswith('.pdf'):
		destination = root_path + '/Libri'  # change the folder destination (Must NOT be a system directory)
		shutil.move(newFile, destination)
		main()
	# Image files
	ext = ('.png', '.jpeg', 'jpg')
	if newFile.lower().endswith(tuple(ext)):
		destination = root_path + '/Immagini'  # change the folder destination (Must NOT be a system directory)
		shutil.move(newFile, destination)
		main()
	# Video files
	ext = ('.mkv', '.mp4')
	if newFile.lower().endswith(tuple(ext)):
		destination = root_path + '/Anime'  # change the folder destination (Must NOT be a system directory)
		shutil.move(newFile, destination)
		main()


def main():
	while True:
		sizeChecker(10)


inputUser = input("Do you also want to reorder the files already present in the folder? [y/n] ")
if inputUser == "y":
	reOrderFiles()
else:
	main()
