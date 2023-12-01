from functions import *

directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)

for i in range(len(files_names)):
    with open("speeches/Nomination_{}.txt".format(), 'r') as f, open("cleaned/{}.txt",'w') as f1:
        
mini()