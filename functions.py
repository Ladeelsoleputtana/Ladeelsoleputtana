import os
import math

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def rename(repertoir):

    file_list = os.listdir(repertoir) #Attribuer une liste de documents à la variable file_list venant du repertoir
    del_car1 = '.txt' #Caractere1 à supprimer
    del_car2 = 'Nomination_' #Caractere2 à supprimer
    for i in range(len(file_list)):
        file_list[i] = file_list[i].replace(del_car1, "")
        file_list[i] = file_list[i].replace(del_car2, "")
    for j in range(len(file_list)):
        file_list[j] = file_list[j].replace('1', "")
        file_list[j] = file_list[j].replace('2', "")
    for j in range(len(file_list)):
        if "Giscard" in file_list[j]:
            file_list[j] = "Valery " + file_list[j]
        if "Hollande" in file_list[j]:
            file_list[j] = "Francois " + file_list[j]
        if "Macron" in file_list[j]:
            file_list[j] = "Emmanuel " + file_list[j]
        if "Mitterrand" in file_list[j]:
            file_list[j] = "Francois " + file_list[j]
        if "Sarkozy" in file_list[j]:
            file_list[j] = "Nicolas " + file_list[j]
        if "Chirac" in file_list[j]:
            file_list[j] = "Jacques " + file_list[j]
    for i in range(len(os.listdir("cleaned/"))):
        print(os.listdir("cleaned/")[i].replace(".txt",""))


def mini(repertoir, file_list): # Fonction qui met en minuscule les fichiers et qui supprime les ponctuations qu'il faut
    liste = [",", '.', ':', ';', '!', '?', '"'] # Liste des ponctuations normales
    liste1 = ['-',"'"] # Liste de ponctuations spécifiques
    for i in range(len(os.listdir(repertoir))):
        if "1" in os.listdir(repertoir)[i]:
            with open(repertoir + os.listdir(repertoir)[i], 'r') as f, open(repertoir + os.listdir(repertoir)[i+1], 'r') as f2,open("cleaned/{}.txt".format(file_list[i]), 'w') as f1:  #Lecture des fichiers depuis le dossier speeches et Ecriture des nouveaux fichiers dans le dossier cleaned
                contenu = f.readlines() + f2.readlines()  # Lire chaque ligne
                for ligne in contenu:  # Boucle pour que "ligne" soit dans le "contenu"
                    for caractere in ligne:  # Boucle pour que "caractere" soit dans le "ligne"
                        if caractere in liste1:  # Si caractere dans liste1 alors
                            f1.write(" ")  # Mettre un espace
                        elif caractere in liste:  # Et si caractere dans liste alors
                            f1.write("")  # Rien écrire
                        else:
                            minuscule = caractere.lower()  # Fonction qui convertit en minuscule
                            f1.write(minuscule)  # Ecriture de la variable "caractere"

        elif "1" not in os.listdir(repertoir)[i] and "2" not in os.listdir(repertoir)[i]:
            with open(repertoir+os.listdir(repertoir)[i],'r') as f,open("cleaned/{}.txt".format(file_list[i]), 'w') as f1: #Lecture des fichiers depuis le dossier speeches et Ecriture des nouveaux fichiers dans le dossier cleaned
                contenu = f.readlines() #Lire chaque ligne
                for ligne in contenu: #Boucle pour que "ligne" soit dans le "contenu"
                    for caractere in ligne: #Boucle pour que "caractere" soit dans le "ligne"
                        if caractere in liste1: #Si caractere dans liste1 alors
                            f1.write(" ") #Mettre un espace
                        elif caractere in liste: #Et si caractere dans liste alors
                            f1.write("") #Rien écrire
                        else:
                            minuscule = caractere.lower()  # Fonction qui convertit en minuscule
                            f1.write(minuscule) #Ecriture de la variable "caractere"


def TF():
    dico = {}
    dico_tf = {}
    nb_total = 0
    for i in os.listdir("cleaned/"):
        with open("cleaned/" + i,'r',encoding='utf-8') as f:
            contenu = f.readlines()
            for ligne in contenu:
                a = ligne.split()
                for mot in a:
                    if mot in dico:
                        dico[mot] += 1
                        nb_total += 1
                    else:
                        dico[mot] = 1
                        nb_total += 1
    for j in dico:
        dico_tf[j] = dico[j]/nb_total
    return dico_tf

def IDF():
    dico_total_idf = {}
    for i in os.listdir("cleaned/"): # Boucle pour calculer tous les mots pour chaque fichier
        dico_idf = {} #Dictionnaire vide
        with open("cleaned/"+ i,'r',encoding='utf-8') as f: # Lire chaque fichier dans le dossier cleaned
            contenu = f.readlines()
            for ligne in contenu:
                a = ligne.split() # Variable pour faire une liste de mots pour chaque ligne
                for mot in a:
                    if mot in dico_idf:
                        dico_idf[mot] += 1
                    else:
                        dico_idf[mot] = 1
        dico_total_idf[i] = dico_idf
    dico = {}
    for i in os.listdir("cleaned/"): #Boucle pour calculer tous les mots différents dans tous le corpus
        with open("cleaned/" + i,'r',encoding='utf-8') as f:
            contenu = f.readlines()
            for ligne in contenu:
                a = ligne.split()
                for mot in a:
                    if mot in dico:
                        dico[mot] += 1
                    else:
                        dico[mot] = 1
    dico_corpus_occ = {}
    for i in dico:
        for president in dico_total_idf:
            if i in dico_total_idf[president]:
                if i in dico_corpus_occ:
                    dico_corpus_occ[i] += 1
                else:
                    dico_corpus_occ[i] = 1
    dico_score_idf = {}
    for i in dico_corpus_occ:
        dico_score_idf[i] = math.log10(len(os.listdir("cleaned/"))/dico_corpus_occ[i])
    return dico_score_idf



def repetition():
    mots = {}
    president = input("Enter a name of a president : ")
    while president != "Chirac":
        president = input("Enter a name of a president : ")

    with open("cleaned/Jacques Chirac.txt",'r',encoding='utf-8') as f3:
        contenu = f3.read()
        lignes = contenu.split()
        for mot in lignes:
            if mot in mots:
                mots[mot] += 1
            else:
                mots[mot] = 1
    dico = dict(sorted(mots.items(), key=lambda item: item[1], reverse=True))
    print(next(iter(dico.items())))
    return mots

def Nation():
    mots = {}
    with open("cleaned/{}",'r') as f:
        contenu = f.read()
        lignes = contenu.split()
        for mot in lignes:
            if mot == "nation":
                mots[mot] += 1
            else:
                mots[mot] = 1
