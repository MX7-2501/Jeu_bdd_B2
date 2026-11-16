from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_video"]

#.... Affichage titre
def afficher_titre():
    print("=" * 20)
    print("JEU VIDEO")
    print("=" * 20)

#afficher option/afficher les choix
def affichage_options(options):
    for i, option in enumerate(option, 1)
        print("f{i}. {option}")

afficher_titre()
affichage_options(["Créer une equipe", "voir les personnages", "Quitter"])
#acquerir des choix valide
#choix du joueur
#afficher personnages 
#afficher statistiques
#creation d'equipe
    #pour les numeros faire des choix avec les options existante
        #ecrire les options 

# Acquerir des choix valide
# Acquerir de l'exp
# Debut de vague
# input crash -> isdigit("")