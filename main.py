from functions import *

directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)

rename("./speeches")

Tf = TF()
print(Tf)

Idf = IDF()
print(Idf)

Tf_Idf = TF_IDF(Tf,Idf)
print(Tf_Idf)


repetition()