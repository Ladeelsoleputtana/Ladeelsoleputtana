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

chaque_doc = TF_IDF_Chaque_Doc(Idf)
print(chaque_doc)

matrice = matrice_tf_idf(chaque_doc)
print(matrice)

repetition()