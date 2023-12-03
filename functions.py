import os

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def mini(): #Fonction qui met en minuscule les fichiers et qui supprime les ponctuations qu'il faut
    liste = [",", '.', ':', ';', '!', '?', '"'] #Liste des ponctuations normales
    liste1 = ['-',"'"] #Liste de ponctuations spécifiques
    with open("speeches/Nomination_{}.txt".format(),'r') as f,open("cleaned/{}.txt".format(), 'w') as f1: #Lecture des fichiers depuis le dossier speeches et Ecriture des nouveaux fichiers dans le dossier cleaned
        contenu = f.readlines() #Lire chaque ligne
        for ligne in contenu: #Boucle pour que "ligne" soit dans le "contenu"
            for caractere in ligne: #Boucle pour que "caractere" soit dans le "ligne"
                if 65 <= ord(caractere) <= 90: #Condition pour vérifier si le caractere est entre 65 et 90 (Décimal des caracteres en Code ASCII) et Si c'est entre cette intervalle
                    minuscule = caractere.lower() #Fonction qui convertit en minuscule
                    f1.write(minuscule) #Ecriture de la variable "minuscule" dans f1
                elif caractere in liste1: #Si caractere dans liste1 alors
                    f1.write(" ") #Mettre un espace
                elif caractere in liste: #Et si caractere dans liste alors
                    f1.write("") #Rien écrire
                else:
                    f1.write(caractere) #Ecriture de la variable "caractere"

def rename():
file_list = os.listdir(r"./speeches")
del_car1 = '.txt'
del_car2 = 'Nomination_'
for i in range(len(file_list)):
    file_list[i] = file_list[i].replace(del_car1, "")
    file_list[i] = file_list[i].replace(del_car2, "")
for j in range(len(file_list)):
    file_list[j] = file_list[j].replace('1', "")
    file_list[j] = file_list[j].replace('2', "")
    if j > 0:
        if file_list[j] != file_list[j - 1]:
            if "Giscard" in file_list[j]:
                file_list[j] = "valery " + file_list[j]
            if "Hollande" in file_list[j]:
                file_list[j] = "francois " + file_list[j]
            if "Macron" in file_list[j]:
                file_list[j] = "emmanuel " + file_list[j]
            if "Mitterrand" in file_list[j]:
                file_list[j] = "francois " + file_list[j]
            if "Sarkozy" in file_list[j]:
                file_list[j] = "nicolas " + file_list[j]
            print(file_list[j])

def occurrence(chaine):
    dico = {}
    phrase = chaine.split()
    for mot in phrase:
        if mot in dico:
            dico[mot] += 1
        else:
            dico[mot] = 1
    return dico

