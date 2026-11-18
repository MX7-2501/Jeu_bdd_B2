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
#    retourner equipe

#fonction choisir_equipe
#   cree un emplacement vide
#       recuperer l'equipe
#       mettre equipe dans emplacement libre 
#   retourner 

#cree les vagues 
#fonction vague_de_combat(equipe, monstre)
#   pour chaque heros vivant tant que le monstre est vivant
#       afficher "heros inflige degats" (heros.attaquer(monstre))
#   vivants = heros encore en vie 
#   cible = un vivant au hasard
#   afficher "monstre inflige degats" (monstre.attaquer(cible))

#fonction boucle_vagues 
    #score commence a zero
    #commencement boucle
        #creer combat de monstre aleatoire
        #afficher la vague avec score +1 nouveau monstre listmongodb apparait
        #si combattre_vague en equipe ne peux plus combattre
            #afficher "defaite" et sortir
        #si combattre_vague en equipe peut combattre
    #retourner score

#fonction sauvegarder_top(base)
#   recuperer les 3 meilleures scores (tri décroissant, limite 3)
#   si aucun afficher "aucun score"
#   sinon afficher "rang. pseudo X vague"