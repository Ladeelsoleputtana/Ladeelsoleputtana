def speeches(a,b,c,d,e,f,g,h):
    a = "Nomination_Chirac1.txt"
    b = "Nomination_Chirac2.txt"
    c = "Nomination_Giscard dEstaing.txt"
    d = "Nomination_Hollande.txt"
    e = "Nomination_Macron.txt"
    f = "Nomination_Mitterand1.txt"
    g = "Nomination_Mitterand2.txt"
    h = "Nomination_Sarkozy.txt"
    Prénom= input("Enter the name of a french president :")
    if Prénom == 'Jacques':
        x = int(input("which speech would you like to read ?"))
        if x == 1:
            with open("Nomination_Chirac1.txt")

import os
def list_of_files(directory, extension):

 files_names = []
 for filename in os.listdir(directory):
 if filename.endswith(extension):
 files_names.append(filename)
 return files_names
# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
print_list(files_names)