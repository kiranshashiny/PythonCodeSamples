# Script to just glob files from a certain folder and print them one a time.
import glob

files=glob.glob('training-data/*.png')

print (files)

for file in files:
	print (file )
