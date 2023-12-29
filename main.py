from functions import *

part1 = Part1('speeches')
part1.rename()
part1.TF()
part1.IDF()
part1.TF_IDF()
part1.TF_IDF_Chaque_Doc()
matrice = part1.matrice_tf_idf()

boom = 1
while boom == 1:
    print("\n\nSi vous voulez afficher la matrice TF-IDF, tapez 1.")
    print("Si vous voulez afficher la liste des mots les moins importants dans le corpus de documents, tapez 2.")
    print("Si vous voulez afficher le mot ayant le score TF-IDF le plus élevé, tapez 3.")
    print("Si vous voulez afficher le mot le plus répéter par le président Chirac, tapez 4.")
    print("Si vous voulez afficher les présidents qui ont parlé de la Nation et ceux qui ont le plus répéter, tapez 5.")
    print("Si vous voulez afficher le président ayant parler du climat et de l'écologie, tapez 6.")
    print("Si vous voulez arrêter le programme, tapez 7. \n")
    Choix_menu = int(input("Choisissez un menu : "))
    if Choix_menu == 1:
        print(matrice)
    elif Choix_menu == 2:
        part1.non_important()
    elif Choix_menu == 3:
        part1.score_haut()
    elif Choix_menu == 4:
        part1.repetition()
    elif Choix_menu == 5:
        part1.Nation()
    elif Choix_menu == 6:
        part1.climat_eco()
    elif Choix_menu == 7:
        boom = 0

part2 = Part2
