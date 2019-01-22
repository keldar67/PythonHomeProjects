#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#  Reads the Journal File and filters out any none comment lines
#
#  
#  
#  
#
#  January 2019
#
#========================================================================#
import os
#------------------------------------------------------------------------#
def ReadJournalFileComments(filename, output):
	f = open(filename, "r")

	for aline in f.readlines():
		if aline.strip().startswith("\'"):
			pass
			#Do Nothing
		else:
			print(aline)
			output.append(aline)

	f.close()

	return output
#------------------------------------------------------------------------#
def WriteJournalFileComments(output, filename):
	f = open(filename,"w")
	for line in output:
		f.write(line)
	f.close()
#------------------------------------------------------------------------#
def GetNewFilename(filename):
	return os.path.splitext(filename)[0] + '_NO COMMENTS_.txt'
#------------------------------------------------------------------------#
def main():
	filename = r'C:\Users\ijames\AppData\Local\Autodesk\Revit\Autodesk Revit 2019\Journals\journal.0001.txt'

	#For the Journal File contents
	output = []

	#Parse the Journal filtering out Non Comment Lines Only
	output = ReadJournalFileComments(filename, output)

	#Create a new output file adjacent to the Journal File.
	newfile = GetNewFilename(filename)

	#Write the parsed data to the new file
	WriteJournalFileComments(output, newfile)
#------------------------------------------------------------------------#
if __name__ == '__main__': main()
#------------------------------------------------------------------------#