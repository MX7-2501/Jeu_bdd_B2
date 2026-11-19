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

#Cree les vagues 
#fonction combattre vague
#   tant que vrai
#       heros attaque
#       si monstre mort 
#           affcher "monstre  vaincu"
#           retourner vrai
#       monstre attaque
#       si heros vivant est vide
#           afficher "toute l'equipe KO"
#           retourner faux

#fonction heros vivant(equipe)
#   retourner la liste des heros est_vivant est vrai

#fonction heros attaque
#   pour chaque heros dans heros vivant
#       si monstre vivant
#           heros attaque monstre
#           afficher "heros inflige des dégats"

#fonction monstres attaque
#   cible est un heros au hasard dans heros vivant
#   le monstre attaque cible
#   afficher "monstre inflige des degats a la cible"
#   si la cible est morte 
#       afficher "le heros est KO"

#fonction boucle_vagues 
    #score commence a zero
    #commencement boucle
        #creer combat de monstre aleatoire
        #afficher la vague avec score +1 nouveau monstre listmongodb apparait
        #si combattre_vague en equipe ne peux plus combattre
            #afficher "defaite" et sortir
        #si combattre_vague en equipe peut combattre
    #retourner score

#fonction est vivant 
#   retourner vrai si pv > 0

#fonction attaquer
#   degats egale attaquant moins defense de la cible
#   si les degats inferieur a  1 mettre degat a 1
#   enlever degats aux pv de la cible
#   si les pv inferieur a 0 mettre pv a 0
#retourner degats

#fonction sauvegarder_top(base)
#   recuperer les 3 meilleures scores (tri décroissant, limite 3)
#   si aucun afficher "aucun score"
#   sinon afficher "rang. pseudo X vague"