#base mongodb
#characters : name, atk, defense, hp
#monsters : name, atk, defense, hp
#scores : pseudo, equipe, vague

#fonction get_base()
# se connecter a mongodb localhost
# retourner la base "jeu_video" 

#fonction recuperer les perso dans le dictionnaire mongodb
#   retourner la liste des perso de la listedb characters

#fonction sauvegardé_score avec base pseudo score
#   inserer dictionnaire dans la liste scores

#fonction monstre aleatoire
#   recuperer la liste des monstres de la listeddb "monsters"
#   retourner un monstre au hasard

#fonction recuperer le top 3 score
#   triee les scores du plus grand au plus petit
#   garder les 3 meilleures scores les plus grand 
#   retourner la liste

#Recuperer un choix valide parmi les options
#   tant que infini
#       afficher les options numerotees
#           pour chaque option dans enumerate(options, start=1)
#               afficher {i}, {option}
#       demander un choix a l'utilisateur
#       si le choix est valide
#           retourner le choix valide
#       afficher un messaage d'erreur  

#choix est valide
#    si le choix n'est pas isdigit()
#       retourner False
#   convertir le choix en entier
#   si le choix est inferieur au minimun ou superieur au maximum
#       retourner False
#   retourner True

#fonction attendre entree
#   demander et afficher "appuie sur entree pour continuer"