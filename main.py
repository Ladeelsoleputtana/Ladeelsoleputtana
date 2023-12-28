from functions import *

part1 = Part1('./speeches')
part1.rename()
part1.TF()
part1.IDF()
part1.TF_IDF()
part1.TF_IDF_Chaque_Doc()
matrice = part1.matrice_tf_idf()
print(matrice)
part1.non_important()
part1.score_haut()
part1.repetition()

