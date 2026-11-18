from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_video"]

#fonction base_donnees
#   recuperer choix du joueur pour equipe 
#       recuperer l'equipe dans dico mongodb
#   si la vague commence
#       recuperer monstre dans dico mongodb
#retourner

