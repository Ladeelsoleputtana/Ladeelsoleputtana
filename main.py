from functions import *

directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)

rename("./speeches")

chaine = "le chat a cru voir un autre chat mais non ce n'était pas un chat mais un chien"
result = TF(chaine)
print(result)

repetition()