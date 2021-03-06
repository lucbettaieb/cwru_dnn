#!/usr/bin/env python3
'''
Zhiang Chen
July,2016
'''
"Save the list of names in directory."

import os
wd = os.getcwd()
print("Current directory is \""+wd+"\"")
print("Start to get list of names in this directory? (yes/no)")
cmd = input()
assert cmd == "yes" or cmd == "no"
if cmd == "no":
	print("Input correct directory:")
	wd = input()
	assert os.path.isdir(wd)

size = os.path.getsize(wd)
files = os.listdir(wd)
file_name = wd+"/name_lists"
fo = open(file_name,'w')
file = ' '.join(files)
fo.write(file)
fo.close()
print("Saved!")
print("The size of images is " + str(size/1024/1024) + "MB")
print("The number of images is "+str(len(files)))
print("The size of the saved file is "+ str(os.path.getsize(file_name)/1024/1024) + "MB")
