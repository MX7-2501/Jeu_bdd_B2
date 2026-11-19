#fonction lancer_partie()
    #pseudo = demander un pseudo non vide
    #equipe = construire equipe
    #score = boucle des vagues
    #sauvegarder le score avec l'equipe, le pseudo et le score
    #afficher top 3 scores dans le menu

#pseudo valide
#fonction demander_pseudo
# tant que infini
#     demander le pseudo
#     si le pseudo n'est pas vide
#       retourner le pseudo
#     afficher "pseudo vide"

#besoin de la liste des personnages de la DB et de l'equipe actuelle
#creer variable/un espace disponible vide 
#pour chaque personnage de la DB
#   si perso n'est pas dans l'equipe
#       ajouter le personnage a la liste disponibles
#retourner la liste disponibles

#Besoin de la liste des personnages de la base DB
#fonction creer une equipe 
#   tant que l'equipe n'est pas complete 
#       determiner la liste des personnages disponibles
#       construire la liste des options a afficher disponibles
#       recuperer le choix de l'utilisateur
#       ajouter le personnage choisi a l'equipe 
#   retourner l'equipe complete

#verifier si l'equipe est pleine
    #retourner vrai si le nombre de perso dans l'equipe >= a taille max

#fonction combattre vague
#   tant que monstre vivant et au moins un heros vivant
#       pour chaque heros dans equipe
#           si heros vivant et monstre vivant
#               heros attaque monstre
#               afficher "heros inflige des degats"
#       si le monstre est mort 
#               afficher "monstre vaincu"
#           retourner vrai
#       les heros encore en vie est egal a vivant
#           les vivants cibler au hasard est egal a cible
#           un monstre attaque cible
#           afficher "monstre inflige des degats a la cible"
#        si la cible est morte 
#               afficher "le hero est KO"
#       si toute l'equipe est morte
#    retourner faux   

#cree les vagues 
#fonction vague_de_combat(equipe, monstre)
#   pour chaque heros vivant tant que le monstre est vivant
#       afficher "heros inflige degats" heros attaquer monstre
#   vivants est un heros encore en vie 
#   cible est un vivant au hasard
#   afficher "monstre inflige degats" monstre attaquer cible

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