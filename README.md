Notre groupe est composé de :
  - DION Edouard
  - LI Hélène

Avant de faire le code, nous avons d'abord un dossier zippé avec les discours (sous forme de fichier .txt) des différents présidents de France . 
Il faut extraire ce dossier et à l'aide des fonctions qu'on va développer, on aura un chatBot qui pourra répondre aux questions en dépendant de la fréquence des mots dans le corpus.
Le code est réparti en 3 parties: 
- Partie 1 : Développement des fonctions de base.
Dans cette première partie, on doit d'abord créer des fonctions de bases qui permettent de remplacer les fichiers de base en des fichiers n'ayant plus de majuscules, ni de ponctuations telles que les virgules, les points, etc.
Une fois modifié, il faut déplacer ces nouveaux fichiers dans un nouveau dossier nommé "cleaned" en faisant attention aux doublons et afficher les noms prénoms des présidents dans la console.
La fonction qui jouera un rôle majeur dans ce projet est le TF-IDF. Cette fonction est d'abord séparé en 2:
  - La fonction TF permet de mesurer la fréquence de chaque mot dans le corpus, c'est-à-dire, le nombre de fois que le mot apparaît dans chaque document du corpus. Plus le mot apparaît, plus son score TF est          élevé.
  - La fonction IDF permet de mesurer l'importance du mot dans tout le corpus. Plus le mot apparaît dans le corpus, plus son score IDF est faible. Tandis que, plus le mot apparaît peu de fois dans le corpus, plus     son score IDF est élevé.
  - La fonction TF_IDF est donc le produit du score TF par le score IDF. Elle permet de mesurer l'importance du document dans le corpus. On a besoin pour CHAQUE document, donc la fonction TF_IDF_Chaque_Doc est        fait pour cela.
  - Pour l'affichage, cela sera sous forme de matrice qui sera la fonction matrice TF-IDF. Dans cette matrice, chaque ligne correspond à un mot et chaque colonne correspond à un fichier du corpus. Cela affiche        donc le score TF-IDF de chaque mot dans chaque fichier.
Ensuite, on passe aux fonctionnalités à développer. C'est aussi ici où on crée le menu pour laisser à l'utilisateur de choisir parmi les propositions suivantes :
  - La fonction non_important sert à mettre dans une liste, les mots soi-disant non importants, c'est-à-dire, les mots ayant un score TF-IDF = 0.
  - La fonction score_haut permet d'afficher le mot ayant le score TF-IDF le plus élevé.
  - La fonction repetition permet d'afficher les mots les plus répéter par le président Jacques Chirac sans prendre en compte les mots dits non importants (les mots ayant un score TF-IDF = 0).
  - La fonction Nation permet d'afficher les présidents ayant prononcé le mot "nation" et celui qui a répété le plus de fois.
  - La fonction climat_eco permet d'afficher le premier président ayant prononcé le mot "climat" et/ou "écologie".
En fonction des numéros attribués à chaque fonction cité ci-dessus, l'utilisateur pourra donc entrer le numéro pour avoir la réponse qu'il souhaite.

- Partie 2 : Calcul de la matrice de similarité et la génération de réponses automatiques.
  
- La fonction trav sert à retirer les caractèress spéciaux des textes afin qu'il soit compatible pour la tokenisation.
- La fonction tokenisation nous permet de traiter la question comme pour les documents du corpus.
- la fonction motquestioncorpus sert à faire a faire une liste des mots présent a la fois dans le corpus et dans la question.
- la fonction idf permet de chercher le score idf des mots dans la partie 1.
- la fonction occur nous permet de savoir combien de fois un mot apparait dans le corpus.
- la fonction tf permet de calcuer le score tf de chaque mot dans une question.
- la fonction matrice_tf_idf sert a créer une mmatruce qui regroupe les scores des mots présent dans le corpus
- La fonction calcul_vecteur_tf_idf prend en paramètre la question et la matrice TF-IDF du répertoire et renvoie le vecteur TF_IDF de la question sous forme de liste. On note que l'ordre des TF_IDF correspond à l'ordre de ceux de la matrice.
- La fonction produit_scalaire sert à calculer le produit scalaire entre deux corpus.
- La fonction norme sert à calculer la norme entre deux corpus.
- La fonction similarite sert à calculer la similarité de cosinus entre deux corpus à l'aide de la fonction norme et de la fonction produit scalaire.
- La fonction proximite permet de savoir quel texte est le plus apte à répondre à la question.
- La fonction mot_question_important permet de trouver le mot ayant le meilleur score tf-idf.
- La fonction phrase_reponse sert à trouver une réponse à partir de la fonction proximite et la fonction mot_question_important.
- La fonction affiner_reponse sert à mieux firmuler la réponse.
- Partie 3 : Généralisation de l'application pour couvrir divers thèmes.
Cette partie ne sera pas réaliser.
