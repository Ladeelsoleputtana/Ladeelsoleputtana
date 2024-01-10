import os
import math
from tabulate import tabulate
from math import *
from math import sqrt


class Part1:
    def __init__(self,repertoir):
        self.repertoir = repertoir
        self.dico_score_tf = {}  # Dictionnaire des scores tf
        self.dico_score_idf = {}  # Dictionnaire des scores idf
        self.dico = {}  #Calculer l'occurrence de chaque mot dans le corpus
        self.dico_score_final = {}  #Score tf idf du corpus
        self.dico2 = {}  #Score tf idf de chaque mot dans chaque document
        self.dico3 = {}  #Calculer l'occurrence de chaque mot dans chaque document


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
                        nb_total += 1
                        if mot in self.dico:
                            self.dico[mot] += 1
                        else:
                            self.dico[mot] = 1
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
        nb_total = 0
        for president in os.listdir("cleaned/"): # Boucle pour l'occurrence de chaque mot dans chaque fichier
            dico_Chaque_Doc = {}
            with open("cleaned/" + president, 'r', encoding='utf-8') as f:
                contenu = f.readlines()
                for ligne in contenu:
                    a = ligne.split()
                    for mot in a:
                        if mot in dico_Chaque_Doc:
                            dico_Chaque_Doc[mot] += 1
                            nb_total += 1
                        else:
                            dico_Chaque_Doc[mot] = 1
                            nb_total += 1
            self.dico3[president] = dico_Chaque_Doc #Chaque fichier a son propre dictionnaire
        dico_nb_total = {}
        for president in os.listdir('cleaned/'):
            dico_nb_mot_par_fichier = 0
            with open("cleaned/" + president, 'r', encoding='utf-8') as f:
                contenu = f.readlines()
                for ligne in contenu:
                    a = ligne.split()
                    dico_nb_mot_par_fichier += len(a)
            dico_nb_total[president] = dico_nb_mot_par_fichier
        for president in self.dico3:
            dico1 = {}
            for mot in self.dico3[president]: # Boucle qui calcule tf idf de chaque mot dans chaque fichier
                dico1[mot] = (self.dico3[president][mot]/dico_nb_total[president]) * self.dico_score_idf[mot] #Calculer le tf idf d'un mot dans un fichier
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

    def score_haut(self):
        liste = []
        mots_importants = sorted(self.dico_score_final.items(),key=lambda item:item[1],reverse=True) #
        liste.append(mots_importants[0])
        for i in range(len(mots_importants)):
            if mots_importants[i] == mots_importants[0]:
                liste.append(mots_importants[i])
        liste.pop(0)
        print("Le mot ayant le score TF IDF le plus élevé est :", liste)

    def repetition(self):
        president = input("Enter a name of a president : ")
        while president != "Chirac":
            president = input("Enter a name of a president : ")

        a = 0
        b = " "
        liste = []

        for mot in self.dico3[os.listdir('cleaned/')[3]]:
            if self.dico_score_idf[mot] != 0:
                liste.append(mot)
        for mot in liste:
            if self.dico3[os.listdir('cleaned/')[3]][mot] > a:
                a = self.dico3[os.listdir('cleaned/')[3]][mot]
                b = mot
        print(b,a)

    def Nation(self):
        print("Les présidents qui ont parlé de nation sont ")
        for president in os.listdir('cleaned/'):
            if "nation" in self.dico3[president]:
                print(president, ":", self.dico3[president]["nation"])

    def climat_eco(self):
        for president in os.listdir('cleaned/'):
            if 'climat' in self.dico3[president]:
                print("Les présidents qui ont parlé de climat sont ",president, ":", self.dico3[president]['climat'])
            elif 'écologie' in self.dico3[president]:
                print("Les présidents qui ont parlé de écologie sont ",president,':', self.dico3[president]['écologie'])
                
class Part2:

    def __init__(self): #Fonction pour tout initialiser à 0
        self.nv_contenu = ""
        self.liste_v = [] #Liste de mot dans la question
        self.noms = []  #
        self.dico_occur = {}
        self.dict_occ = {}
        self.vecteur_question = [] #Liste pour
        self.Liste_Vec_Chaque_Doc = []  #Liste des vecteurs de chaque doc
        self.Liste_produit_scalaire = []  #Liste des produits scalaires de chaque vecteur
        self.Liste_Norme_Vecteur = [] #Liste des normes de chaque vecteur
        self.Liste_similarite_cos = []




    def trav(self,question): #Fonction pour mettre en minuscule les majuscules et supprimer les ponctuations ou remplacer par des espaces
        self.question = question
        for lettre in self.question :
            if lettre in ["'","-","_",","]:
                self.nv_contenu += " "
            elif lettre not in ['?','!',".",":",'"',';']:
                self.nv_contenu += lettre.lower()


    def tokenisation(self): #Fonction qui sépare la question et met tout dans une liste
        question_trav = self.nv_contenu
        liste = question_trav.split()
        for val in liste:
            if val not in self.liste_v:
                self.liste_v.append(val)

    def MotQuestionCorpus(self,dico): #Fonction pour supprimer les mots de la question qui ne sont pas dans le corpus
        self.Liste = []
        ListeVerif = self.liste_v
        for mot in ListeVerif:
            if mot not in dico:
                self.Liste.append(mot)

    def liste_fichier(self): #Fonction pour afficher la liste du répertoir
        for nom in os.listdir("cleaned"):
            if nom.endswith('.txt'):
                self.noms.append(nom)

    def occur(self):
        liste_mot = self.nv_contenu.split()
        for val in liste_mot:
            if val not in self.dico_occur.keys():
                self.dico_occur[val] = 1
            else: 
                self.dico_occur[val] += 1

    def tf(self):
        self.nb = len(self.liste_v)
        for cle, val in self.dico_occur.items():
            if cle in self.Liste:
                self.dict_occ[cle] = 0
            else:
                self.dict_occ[cle] = val/self.nb


    def idf(self,dico_idf_Part1): #Fonction pour chercher le score idf des mots dans la partie 1
        self.dico_idf = self.dico_occur
        for cle, val in self.dico_idf.items():
            if cle in dico_idf_Part1:
                self.dico_idf[cle] = dico_idf_Part1[cle]
            else:
                self.dico_idf[cle] = 0

    def calcul_vecteur_tf_idf(self):
        """Cette fonction renvoie le vecteur TF_IDF de la question sous forme de liste.
        On note que l'ordre des TF_IDF correspond à l'ordre de ceux de la matrice"""
        for mot in self.liste_v:
            self.vecteur_question.append(
                self.dico_idf[mot] * self.dict_occ[mot])  # On calcule le tfidf de chaque mot de la question

    def matrice_tf_idf(self,dico_occ_chaque_doc,dico_score_tfidf_chaque_doc): #
        for president in dico_occ_chaque_doc:
            Liste_Vec_president = []
            for mot in self.liste_v:
                if mot in dico_occ_chaque_doc[president]:
                    Liste_Vec_president.append(dico_score_tfidf_chaque_doc[president][mot])  #Ajouter le score tfidf de chaque mot de la question de chaque doc
                else:
                    Liste_Vec_president.append(0)
            self.Liste_Vec_Chaque_Doc.append(Liste_Vec_president)

    def produit_scalaire(self):
        for vecteur in self.Liste_Vec_Chaque_Doc:
            prod = 0
            for i in range(len(vecteur)):
                prod += vecteur[i] * self.vecteur_question[i]
            self.Liste_produit_scalaire.append(prod)


    def norme(self):
        for vecteur in self.Liste_Vec_Chaque_Doc:
            norme = 0
            for i in range(len(vecteur)):
                norme += vecteur[i] **2
            self.Liste_Norme_Vecteur.append(sqrt(norme))

        norme = 0
        for mot in self.vecteur_question:
            norme += mot **2
        self.Norme_Question = norme

    def similarite(self): #Fonction pour calculer la similarité cosinus du vecteur de la question par rapport au vecteur de chaque document
        for i in range(len(self.Liste_Norme_Vecteur)):
            if self.Liste_Norme_Vecteur[i] * self.Norme_Question == 0:
                self.Liste_similarite_cos.append(0)
            else:
                self.Liste_similarite_cos.append(self.Liste_produit_scalaire[i]/(self.Liste_Norme_Vecteur[i] * self.Norme_Question))

    def proximite(self): # Fonction pour trouver la similarité la plus haute
        similarite_haute = 0
        for i in range(len(self.Liste_similarite_cos)):
            if i == 0:
                similarite_haute = self.Liste_similarite_cos[0]
            elif self.Liste_similarite_cos[i] > similarite_haute:
                similarite_haute = self.Liste_similarite_cos[i]
        verif = 0
        for i in self.Liste_similarite_cos:
            if i == 0:
                verif += 1
        if verif == len(self.Liste_similarite_cos):
            print("Aucun document n'est pertinent.")
        else:
            nom_doc_pertinent = self.noms[self.Liste_similarite_cos.index(similarite_haute)]  # Chercher la position de la similarité la plus haute dans la liste des similarités cosinus pour trouver la position du document pertinent dans la liste des fichiers
            print("Le document le plus pertinent est : ",nom_doc_pertinent)


"""
    def transposee(self):
        r = []
        for nbCol in range(len(self[0])):
            ligneM = []
            for ligne in range(len(self)):
                ligneM.append(self[ligne][nbCol])
            r.append(ligneM)"""
