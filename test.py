import math
import os
import re
import csv

path = os.getcwd()
parent = os.path.dirname(path)
f_list = next(os.walk(str(parent) + '/GHdoc/Results_all/python'))[2]

#print(f_list)

# for root, dirs, files in os.walk(d_list[0]):
# 	for file in files:
# 		# v = os.path.join(subdir,dirv).replace("\\","/")
# 		dir_list.append(file)

# print(dir_list)
for file in f_list:
	f_name = file.split("_")[0]

	# # allconsFile = open("allcons.txt",'a',encoding="utf-8-sig", errors='ignore')
	#consFile = "./cpp/{}_consolidate.txt".format(f_name)
#	commFile = "./python/{}_commit.txt".format(f_name)
#	issFile = "./python/{}_issue.txt".format(f_name)
	pFile = "./python/{}_pullreq.txt".format(f_name)

# 		# readmeFile = open(readme_name,"w")
	#consolidateFile = open(consFile,'w',encoding="utf-8-sig", errors='ignore')
#	commitFile = open(commFile,'a',encoding="utf-8-sig", errors='ignore')
#	issueFile = open(issFile,'a',encoding="utf-8-sig", errors='ignore')
	pullFile = open(pFile,'a',encoding="utf-8-sig", errors='ignore')
	new = str(parent)+"/GHdoc/Results_all/python/"+str(file)

	if(file.endswith("PRData.txt")):
	#			consolidateFile.write("PRData================================")
				# allconsFile.write("PRData================================")
				

				f = open(new,encoding="utf-8-sig", errors='ignore')
				text = f.readlines()
				if(len(text)>1):
					for i in range(len(text)):
						
						if(text[i].find("title")!=-1 and text[i].find("=")!=-1):
							title = text[i].split("=")[1]
	#						consolidateFile.write(title)
							# allconsFile.write(title)
							pullFile.write(title)
						
						if(text[i].find("body =")!=-1):
							start = i
							j = i+1

							body = text[i].split("=")[1]
							while(text[j].find("state")==-1):
								body = body+(text[j])
								j= j+1
							# print(body)
	#						consolidateFile.write(body)
							# allconsFile.write(body)
							pullFile.write(body)


#	if(file.endswith("IRData.txt")):
	#			consolidateFile.write("IR Data==================================")

#				f = open(new,encoding="utf-8-sig", errors='ignore')
#				text = f.readlines()
#				if(len(text)>1):
#					for i in range(len(text)):
#						
#						if(text[i].find("title=")!=-1):
#							title = text[i].split("=")[1]
	#						consolidateFile.write(title)
							# allconsFile.write(title)
#							issueFile.write(title)
						
#						if(text[i].find("body =")!=-1):
#							j = i+1
							# print("________"+str(text[i]))
#							body = text[i].split("=")[1]
#							while(text[j].find("state")==-1):
#								body = body+(text[j])
#								j= j+1
#							# print(body)
	#						consolidateFile.write(body)
							# allconsFile.write(body)
#							issueFile.write(body)
#						if(text[i].find("comment =")!=-1):
#							j = i+1
#							comment = text[i].split("=")[1]
#
#						
#							while(text[j].find("comment date")==-1):
#								comment = comment+(text[j])
#								j= j+1
#							print("here")	
#							print(text[j])	
##							# print(comment)
#	#						consolidateFile.write(comment)
#							# allconsFile.write(comment)
#							issueFile.write(comment)
#			# consolidateFile.write("==================================")				
#
#	
#	if(file.endswith("CData.txt")):
#				# consolidateFile.write("CData==================================")
#
#				# # commitFile.write("hi")
#				# # commitFile.write(new)
#				# print(new)
#				f = open(new,encoding="utf-8-sig", errors='ignore')
#
#				
#	#			commitFile.write(str(f))
#				text = f.readlines()
#				if(len(text)>1):
#
##					for i in range(len(text)):
						
#						if(text[i].find("message")!=-1):
#							j = i+1
#							if(len(text[i].split("="))>1):
#								message = text[i].split("=")[1]
#
#							while(text[j].find("url")==-1):
#								if(text[j].find("comment date")==-1 and text[j].find("comment id")==-1):
#									message = message+(text[j])
#								j= j+1
#							print(message)
#							print(str(commitFile))
#							print("_______________________")
#							# consolidateFile.write(message)
#							# allconsFile.write(message)
#							commitFile.write(message)
#
#
#						if(text[i].find("comment =")!=-1 ):
#							j = i+1
#							comment = text[i].split("=")[1]
#							print("-------------------")
#							
#						
#							while(text[j].find("comment date")==-1 or text[j].find("date =")==-1):
#								comment = comment+(text[j])
#
#								j= j+1
#							# print(comment)
							# print(comment)
	#						consolidateFile.write(comment)
							# allconsFile.write(comment)
#							commitFile.write(comment)	
