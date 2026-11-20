#fonction lancer_partie()
    #pseudo = demander un pseudo non vide
    #equipe = construire equipe
    #vague = boucle des vagues
    #sauvegarder le score avec l'equipe, le pseudo et le score
    #afficher "defaite a la vague"
    #attendre entree par le joueur

#fonction demander_pseudo
# tant que infini
#     demander le pseudo
#     si le pseudo n'est pas vide
#       retourner le pseudo
#     afficher "pseudo vide"

#fonction creer une equipe
#equipe list vide 
#   tant que l'equipe a moins de 3 personnages
#       pour chaque personnage options = texte_personnage
#       recuperer le choix du joueur 
#       retirer le personnage choisi de personnage et l'ajouter a l'equipe
#retourner l'equipe

#fonction texte_personnage
#   retourner le nom, l'attaque, l'hp, la defense 

#fonction boucle_vagues 
    #vague commence a 1
    #tant que infini
        #creer combat de monstre aleatoire
        #afficher la vague avec nouveau monstre listmongodb apparait
        #si combattre_vague est faux retourner vague
        #vague = vague + 1
 
#fonction combattre vague
#   tant que infini
#       heros attaque
#       si monstre mort 
#           affcher "monstre  vaincu"
#           retourner vrai
#       monstre attaque
#       si heros vivant est vide
#           afficher "toute l'equipe KO"
#           retourner faux

#fonction heros attaque
#   pour chaque heros dans heros vivant
#       si monstre vivant
#           heros attaque monstre
#           afficher "heros inflige des dégats"

#fonction monstres attaque
#   cible est un heros au hasard dans heros vivant
#   le monstre attaque cible

#fonction attaquer
#   degats = attaque - defense de la cible
#   si les degats inferieur a  1 mettre degat a 1
#   enlever degats aux hp de la cible
#   si les hp inferieur a 0 mettre hp a 0
#   afficher "attaquant inflige degats a la cible il reste x hp"
#   si la cible n'est pas vivante afficher "cible est KO"

#fonction est vivant 
#   retourner vrai si pv > 0

#fonction heros vivant(equipe)
#   retourner la liste des heros est_vivant est vrai