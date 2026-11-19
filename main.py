#fonction menu
#   utilisation base de donnees
#   tant que infini
#   effacer l'ecran

#   afficher le titre "COMBAT GAME"
#   demander le choix du joueur parmis les 3 options (jouer, top 3, quitter)

#fonction attendre entree
#   demander et afficher "appuie sur entree pour continuer"

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