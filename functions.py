import os
import math
from tabulate import tabulate
from math import *
from math import sqrt


class Part1:
    def __init__(self,repertoir):
        self.repertoir = repertoir
        self.dico_score_tf = {}
        self.dico_score_idf = {}
        self.dico = {}
        self.dico_score_final = {}
        self.dico2 = {}
        self.dico3 = {}


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

    def trav(contenu):
        nv_contenu = ""
        for lettre in contenu :
            if 65 <= ord(lettre) <=  90 :
                nv_contenu += chr(ord(lettre)+32)
            elif (33 <= ord(lettre) <= 47) or (58 <= ord(lettre) <= 63) or (91 <= ord(lettre) <= 96) or (123 <= ord(lettre) <= 126):
                nv_contenu += " "
            else:
                nv_contenu += lettre
        return nv_contenu 

    def tokenisation(question):
        question_trav = trav(question)
        liste = question_trav.split()
        liste_v=[]
        for val in liste:
            if val not in liste_v:
                liste_v.append(val)
        return liste_v

    def liste_fichier(repertoir,extension):
        noms=[]
        for nom in os.listdir(repertoir):
            if nom.endswith(extension):
                noms.append(nom)
        return noms
    
    if not os.path.exists('cleaned'):
        os.mkdir('cleaned')
        cleaned_dir='cleaned'
        liste=liste_fichier('speeches','txt')
        for nom in liste:
            nv_fichier=os.path.join(cleaned_dir,nom)
            with open(os.path.join("speeches",nom),"r") as speeches, open(nv_fichier,"w") as cleaned_fichier:
                for ligne in speeches:
                    nv_ligne=trav(ligne)
                    cleaned_fichier.write(nv_ligne)
    
    
    def occur(texte):
        liste_mot=texte.split()
        dico_occur={}
        for val in liste_mot:
            if val not in dico_occur.keys():
                dico_occur[val]=1
            else: 
                dico_occur[val]+=1
        return dico_occur
    
    def tf(fichier):
        with open(fichier,"r",encoding='utf-8') as f:
            txt = f.read()
            nb= len(txt.split())
            dict_occ = occur(txt)
            for cle, val in dict_occ.items():
                dict_occ[cle]= val/nb
        return dict_occ
    
    def idf(repertoir):
        fichiers= os.listdir(repertoir)
        dico_idf={}
        liste_texte=[]
        liste_bis=[]
        nb=len(fichiers)
        for nom in fichiers:
            with open(os.path.join(repertoir,nom),"r",encoding='utf-8')as f:
                contenu= f.read()
                liste_mot=contenu.split()
            liste_texte.append(liste_mot)
        for liste in liste_texte:
            nvliste=[]
            for val in liste:
                if val not in nvliste:
                    nvliste.append(val)
            liste_bis.append(nvliste)
        for liste in liste_bis:
            for mot in liste:
                if mot not in dico_idf.keys():
                    dico_idf[mot]=1
                else:
                    dico_idf[mot]+=1
    
        for cle, val in dico_idf.items():
            dico_idf[cle]=log((nb/val),10)
        return dico_idf
    
    
    def transposee(matrice): 
        r=[]
        for nbCol in range(len(matrice[0])):
            ligneM=[]
            for ligne in range(len(matrice)):
                ligneM.append(matrice[ligne][nbCol])
            r.append(ligneM)
        return r
    
    def matrice_tf_idf(repertoir):
        matrice=[]
        mots = list(idf(repertoir).keys())
        ligne_mot=["mots:"]
        for mot in mots:
            ligne_mot.append(mot)
        matrice.append(ligne_mot)
        s_idf = idf(repertoir)
        for fichier in liste_fichier(repertoir,extension="txt"):
            colonne=[fichier]
            fichier='cleaned/'+fichier
            s_tf=tf(fichier)
            s_tf_idf={}
            for mot in s_idf.keys():
                if mot in s_tf.keys():
                    s_tf_idf[mot]=s_tf[mot]*s_idf[mot]
                else:
                    s_tf_idf[mot]= 0.0
            ligne_tf_idf=colonne
            for score in s_tf_idf.values():
                ligne_tf_idf.append(score)
            matrice.append(ligne_tf_idf)
        return matrice
    
    def tokenisation(question):
        question_trav = trav(question)
        liste = question_trav.split()
        liste_v=[]
        for val in liste:
            if val not in liste_v:
                liste_v.append(val)
        return liste_v
    
    
    
    def motquestioncorpus(question,repertoir):
        liste_v = tokenisation(question)
        fichiers= os.listdir(repertoir)
        liste_texte=[]
        contenu_global=[]
        liste_mot_commun =[]
        for nom in fichiers:
            with open(os.path.join(repertoir,nom),"r",encoding='utf-8') as f:
                contenu = f.read()
                liste_texte = contenu.split()
            contenu_global += liste_texte
        for i in range(len(liste_v)):
            if liste_v[i] in contenu_global:
                liste_mot_commun.append(liste_v[i])
        return liste_mot_commun
      
    
    
    
    def tf_question(question):
        dico_tf=occur(question)
        nb = len(question.split())
        for key, val in dico_tf.items():
            dico_tf[key]=val/nb
        return dico_tf
    
    
    def calcul_vecteur_tf_idf(question,matrice): #renvoie le vecteur sous forme de liste
        """Cette fonction prend en paramètre la question et la matriceTFIDF du répertoire et renvoie le vecteur TF_IDF
        de la question sous forme de liste. On note que l'ordre des TF_IDF correspond à l'ordre de ceux de la matrice"""
        dico_idf = idf('cleaned') # Dictionnaire contenant l'IDF des mots du répetoire cleaned
        dico_tf = tf_question(trav(question)) # Dictionnaire contenant le TF des mots de la question convertie en minuscule et sans caractère spéciaux
        vecteur_question=[]
        liste_question= tokenisation(question) # Liste contenant tous les mots de la question (en minuscule)
        for i in range(1,len(matrice)):
            if matrice[i][0] in liste_question: # Si le premier terme de la sous liste de la matrice soit le mot est dans la liste de mot de la question
                tfidf= dico_tf[matrice[i][0]]*dico_idf[matrice[i][0]] # La variable tfidf prend la valeur du du tf du mot dans la question multiplié par le idf du mot dans le corpus
            else:
                tfidf= 0.0 # Sinon la variable prend la valeur 0.0
            vecteur_question.append(tfidf) # On ajoute la valeur de la variable tfidf au vecteur de la question
        return vecteur_question
    
    def produit_scalaire(A,B):
        prod = 0
        for i in range(len(A)):
            prod += A[i] * B[i]
        return prod
    
    def norme(L):
        norme = 0
        for i in range(len(L)):
            norme += L[i] **2
        norme = sqrt(norme)
        return norme
    
    def similarite(A, B):
        prod = produit_scalaire(A,B)
        norme_A = norme(A)
        norme_B = norme(B)
        similariter = prod/(norme_A * norme_B)
        return similariter
    
    def proximite(question,repertoir):
        matrice=matrice_tf_idf('cleaned')
        vecteur_q = calcul_vecteur_tf_idf(question,transposee(matrice))
        max=0
        for ligne in range(1,len(matrice)): #On ne parcourt pas la première sous liste car elle contient tous les mots du corpus
            vrai_ligne= matrice[ligne][1:] # On ne prend pas le 1er el de la sous liste car il correspond au nom du fichier
            simil=similarite(vecteur_q,vrai_ligne)
            if simil > max:
                max=simil
                i_max=ligne
        return matrice[i_max][0]
    
    def mot_question_important(question, repertoir):
        matrice=transposee(matrice_tf_idf(repertoir))
        tf_idf_question = calcul_vecteur_tf_idf(question,transposee(matrice_tf_idf(repertoir)))
        max=0
        for i in range(len(tf_idf_question)):
            if tf_idf_question[i]>max:
                max=tf_idf_question[i]
                indice= i+1
        return matrice[indice][0]
    
    def phrase_reponse(question):
        mot_pertinent=mot_question_important(question,'cleaned')
        doc_pertinent=proximite(question,'cleaned')
        liste_phrase=[]
        contenu_vrai=""
        phrase_pertinente=[]
        with open(os.path.join('speeches',doc_pertinent),"r",encoding='utf-8') as doc:
            contenu = doc.read()
            for car in contenu:
                if car != '\n':
                    contenu_vrai+=car
            phrases=contenu_vrai.split(".")
            for phrase in phrases:
                if mot_pertinent in phrase:
                    phrase_pertinente.append(phrase)
        return phrase_pertinente[0]
    
    def affiner_reponse(question):
        question_deca = trav(question)
        reponse_base = phrase_reponse(question)
        if reponse_base[len(reponse_base) -1] != '.':
            reponse_base += '.'
        if 'comment' in question_deca:
            reponse_affine = 'Après analyse,'
        if 'pourquoi' in question_deca:
            reponse_affine = 'Car'
        if 'peux tu' in question_deca:
            reponse_affine = 'Oui, bien-sûr!'
