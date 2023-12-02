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
    with open("speeches/Nomination_{}.txt".format(),'r') as f,open("cleaned/{}.txt", 'w') as f1: #Lecture des fichiers depuis le dossier speeches et Ecriture des nouveaux fichiers dans le dossier cleaned
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