from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_video"]

#lancer la partie, cree equipe, boucle vague, score
#fonction lancer_partie()
    #pseudo = demander un pseudo non vide
    #equipe = construire equipe
    #score = boucle des vagues
    #sauvegarder le score avec l'equipe, le pseudo et le score
    #afficher top 3 scores dans le menu

#Fonction construire equipe
    #perso disponible = tous les personnages du camps
    #tant que equipe < 3 héros
        #afficher les personnages disponible avec les stats
        #choix du joueur peut être 1 ou un 
        #si perso choisi est le meme retirer
    #retourner equipe

#cree les vagues 
#fonction boucle_vagues 
    #score commence a zero
    #systeme boucle
        #creer combat de monstre aleatoire
        #afficher la vague avec score +1 nouveau monstre listmongodb apparait
        #si combattre_vague en equipe ne peux plus combattre
            #afficher "defaite" et sortir
        #si combattre_vague en equipe peut combattre
    #retourner score



#.... Affichage titre
def afficher_titre():
    print("=" * 20)
    print("      JEU VIDEO")
    print("=" * 20)

#afficher option/afficher les choix
def affichage_options(options):
    for i, option in enumerate(options, 1):
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