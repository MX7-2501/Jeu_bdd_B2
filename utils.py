#base mongodb
#characters : name, atk, defense, hp
#monsters : name, atk, defense, hp
#scores : pseudo, equipe, vague

from pymongo import MongoClient
import random

#fonction get_base()
def ouvrir_base():
# se connecter a mongodb localhost
    client = MongoClient("mongodb://localhost:27017/")
# retourner la base "jeu_video" 
    return client["jeu_video"]

#fonction recuperer les perso dans le dictionnaire mongodb
def lire_personnage(base):
#   retourner la liste des perso de la listedb characters
    return list(base["characters"].find({}, {"_id": 0}))

#fonction sauvegardé_score avec base pseudo score
def sauvegarder_score(base, pseudo, equipe, vague):
    noms = [perso["name"] for perso in equipe]
    base["scores"].insert_one({"pseudo": pseudo, "equipe": noms, "vague": vague})

#fonction monstre aleatoire
def monstre_aleatoire(base):
#   recuperer la liste des monstres de la listeddb "monsters"
    monstres = list(base["monsters"].find({}, {"id_": 0}))
#   retourner un monstre au hasard
    return random.choice(monstres)

#fonction recuperer le top 3 score
def lire_top3(base):
#   retourner la liste triee les scores du plus grand au plus petit garder les 3 meilleures scores les plus grand 
    return list(base["scores"].find({}, {"_id"}).sort("vague", -1).limit(3))

#Recuperer un choix utilisateur valide parmi les options
def recuperer_choix_utilisateur(options):
#   tant que infini
    while True:
#       afficher les options numerotees
        afficher_options_numerotees(options)
#       demander un choix a l'utilisateur
        choix = input("Entrez votre choix")
#       si le choix est valide
        if est_choix_valide(choix, 1, len(options)):
#           retourner le choix valide
            return int(choix)
#       afficher un messaage d'erreur 
        print("Choix invalide")

#fonction afficher options umerotees
def afficher_options_numerotees(options):
#   pour chaque option dans enumerate
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

#choix est valide
def est_choix_valide(choix, minimun, maximun):
#    si le choix n'est pas isdigit()
    if not choix.isdigit():
#       retourner False
        return False
#   convertir le choix en entier
    nombre = int(choix)
#   si le choix est inferieur au minimun ou superieur au maximum
    if nombre < minimun or nombre > maximun:
#       retourner False
        return False
#   retourner True
    return True

#fonction attendre entree
def attendre_entree():
#   demander et afficher "appuie sur entree pour continuer"
    input("Appuie sur entree pour continuer")