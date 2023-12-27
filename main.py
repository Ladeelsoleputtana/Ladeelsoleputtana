from functions import *

directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)

rename("./speeches")

Tf = TF()
print(Tf)

Idf = IDF()
print(Idf)


repetition()