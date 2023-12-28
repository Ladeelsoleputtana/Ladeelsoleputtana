import os
import math
from tabulate import tabulate

class Part1:
    def __init__(self,repertoir):
        self.repertoir = repertoir
        self.dico_score_tf = {}
        self.dico_score_idf = {}
        self.dico = {}
        self.dico_score_final = {}
        self.dico2 = {}


    def rename(self):
        self.file_list = os.listdir(self.repertoir) #Attribuer une liste de documents à la variable file_list venant du repertoir
        del_car1 = '.txt' #Caractere1 à supprimer
        del_car2 = 'Nomination_' #Caractere2 à supprimer
        for i in range(len(self.file_list)):
            self.file_list[i] = self.file_list[i].replace(del_car1, "")
            self.file_list[i] = self.file_list[i].replace(del_car2, "")
        for j in range(len(self.file_list)):
            self.file_list[j] = self.file_list[j].replace('1', "")
            self.file_list[j] = self.file_list[j].replace('2', "")
        for j in range(len(self.file_list)):
            if "Giscard" in self.file_list[j]:
                self.file_list[j] = "Valery " + self.file_list[j]
            if "Hollande" in self.file_list[j]:
                self.file_list[j] = "Francois " + self.file_list[j]
            if "Macron" in self.file_list[j]:
                self.file_list[j] = "Emmanuel " + self.file_list[j]
            if "Mitterrand" in self.file_list[j]:
                self.file_list[j] = "Francois " + self.file_list[j]
            if "Sarkozy" in self.file_list[j]:
                self.file_list[j] = "Nicolas " + self.file_list[j]
            if "Chirac" in self.file_list[j]:
                self.file_list[j] = "Jacques " + self.file_list[j]
        for i in range(len(os.listdir("cleaned/"))):
            print(os.listdir("cleaned/")[i].replace(".txt",""))


    def mini(self): # Fonction qui met en minuscule les fichiers et qui supprime les ponctuations qu'il faut
        liste = [",", '.', ':', ';', '!', '?', '"'] # Liste des ponctuations normales
        liste1 = ['-',"'"] # Liste de ponctuations spécifiques
        for i in range(len(os.listdir(self.repertoir))):
            if "1" in os.listdir(self.repertoir)[i]:
                with open(self.repertoir + os.listdir(self.repertoir)[i], 'r') as f, open(self.repertoir + os.listdir(self.repertoir)[i+1], 'r') as f2,open("cleaned/{}.txt".format(self.file_list[i]), 'w') as f1:  #Lecture des fichiers depuis le dossier speeches et Ecriture des nouveaux fichiers dans le dossier cleaned
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

            elif "1" not in os.listdir(self.repertoir)[i] and "2" not in os.listdir(self.repertoir)[i]:
                with open(self.repertoir+os.listdir(self.repertoir)[i],'r') as f,open("cleaned/{}.txt".format(self.file_list[i]), 'w') as f1: #Lecture des fichiers depuis le dossier speeches et Ecriture des nouveaux fichiers dans le dossier cleaned
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


    def TF(self):
        nb_total = 0 # Nombre total de mots dans le dossier
        for i in os.listdir("cleaned/"):
            with open("cleaned/" + i,'r',encoding='utf-8') as f:
                contenu = f.readlines()
                for ligne in contenu:
                    a = ligne.split()
                    for mot in a:
                        if mot in self.dico:
                            self.dico[mot] += 1
                            nb_total += 1
                        else:
                            self.dico[mot] = 1
                            nb_total += 1
        for mot in self.dico: # Chercher mot dans dico
            self.dico_score_tf[mot] = self.dico[mot]/nb_total


    def IDF(self):
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
        dico_corpus_occ = {}
        for mot in self.dico: # Boucle pour calculer le nombre de documents comportant un mot
            for president in dico_total_idf:
                if mot in dico_total_idf[president]:
                    if mot in dico_corpus_occ:
                        dico_corpus_occ[mot] += 1
                    else:
                        dico_corpus_occ[mot] = 1
        for mot in dico_corpus_occ:
            self.dico_score_idf[mot] = math.log10(len(os.listdir("cleaned/"))/dico_corpus_occ[mot]) #Appliquer la formule

    def TF_IDF(self):
        for mot in self.dico_score_tf:
            self.dico_score_final[mot] = self.dico_score_tf[mot] * self.dico_score_idf[mot]

    def TF_IDF_Chaque_Doc(self):
        dico = {}
        nb_total = 0
        for president in os.listdir("cleaned/"): # Boucle pour l'occurrence de chaque mot dans chaque fichier
            dico_Chaque_Doc = {}
            with open("cleaned/" + president, 'r', encoding='utf-8') as f:
                contenu = f.readlines()
                for ligne in contenu:
                    a = ligne.split()
                    for mot in a:
                        if mot in dico:
                            dico_Chaque_Doc[mot] += 1
                            nb_total += 1
                        else:
                            dico_Chaque_Doc[mot] = 1
                            nb_total += 1
            dico[president] = dico_Chaque_Doc #Chaque fichier a son propre dictionnaire
        dico_nb_total = {}
        for president in os.listdir('cleaned/'):
            dico_nb_mot_par_fichier = 0
            with open("cleaned/" + president, 'r', encoding='utf-8') as f:
                contenu = f.readlines()
                for ligne in contenu:
                    a = ligne.split()
                    dico_nb_mot_par_fichier += len(a)
            dico_nb_total[president] = dico_nb_mot_par_fichier
        for president in dico:
            dico1 = {}
            for mot in dico[president]: # Boucle qui calcule tf idf de chaque mot dans chaque fichier
                dico1[mot] = (dico[president][mot]/dico_nb_total[president]) * self.dico_score_idf[mot] #Calculer le tf idf d'un mot dans un fichier
            self.dico2[president] = dico1

    def matrice_tf_idf(self):
        liste = []
        liste1 = ['Mots']
        for i in os.listdir('cleaned/'):
            liste1.append(i)
        liste.append(liste1)
        for mot in self.dico:
            liste2 = [mot]
            for president in self.dico2:
                if mot in self.dico2[president]:
                    liste2.append(self.dico2[president][mot])
                else:
                    liste2.append(0)
            liste.append(liste2)
        return tabulate(liste)

    def non_important(self):
        liste = []
        for mot in self.dico_score_idf:
            if self.dico_score_idf[mot] == 0:
                liste.append(mot)
        print("Les mots dits non importants sont : ",liste)


    def repetition(self):
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

    def Nation(self):
        mots = {}
        with open("cleaned/{}",'r') as f:
            contenu = f.read()
            lignes = contenu.split()
            for mot in lignes:
                if mot == "nation":
                    mots[mot] += 1
                else:
                    mots[mot] = 1
