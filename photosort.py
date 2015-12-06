import os, sys, re  
import shutil

foldertoanalyze=sys.argv[1]
year=sys.argv[2]


def decidethefolder (filename, year): 
	index=filename.find(year)
	if index >-1: 	
		month=filename[index+4:index+6]
		day=filename[index+6:index+8]
		outfolder=( "_".join(["f", year, month]) , "_".join(["f", year, month, day]) )
	else: 
		outfolder=("_".join(["f", year, "unclassified"]),   "_".join(["f", year, "unclassified", "noday"]) )
	return outfolder  

for filename in os.listdir(foldertoanalyze) :
	folder=decidethefolder(filename , year)
	monthfolder=folder[0]; dayfolder="/".join(folder )
	if not os.path.exists(monthfolder):
		os.makedirs(monthfolder)	
	if not os.path.exists(dayfolder): 
		os.makedirs(dayfolder)

	cmd= "mv %s/%s %s " %(foldertoanalyze, filename, dayfolder ) 
	os.system(cmd)
	#shutil.copy2('%s/%s' % (myoriginfolder, i ), wheretocopy)		


