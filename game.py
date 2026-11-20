#fonction lancer_partie()
def lancer_partie(base):
    #pseudo = demander un pseudo non vide
    pseudo = demander_pseudo()
    #equipe = construire equipe
    equipe = creer_equipe(lire_personnages(base))
    #vague = boucle des vagues
    vague = boucle_vagues(base, equipe)
    #sauvegarder le score avec l'equipe, le pseudo et le score
    sauvegarder_score(base, pseudo, equipe, vague)
    #afficher "defaite a la vague"
    print("Defaite a la vague {vague} !")
    #attendre entree par le joueur
    attendre_entree()

#fonction demander_pseudo
def demander_pseudo():
# tant que infini
    while True:
#     demander le pseudo
        pseudo = input("Ton pseudo : ").strip()
#     si le pseudo n'est pas vide
        if pseudo != ""
#       retourner le pseudo
            return pseudo
#     afficher "pseudo vide"
        print("Le pseudo est vide")

#fonction creer une equipe
def creer_equipe(personnage):
#equipe list vide 
    equipe = []
#   tant que l'equipe a moins de 3 personnages
    while len(equipe)
#       pour chaque personnage options = texte_personnage
        options = [texte_personnage(perso) for perso in personnages]
#       recuperer le choix du joueur 
        choix = recuperer_choix_utilisateur(options)
#       retirer le personnage choisi de personnage et l'ajouter a l'equipe
        equipe.append(personnages.pop(choix-1))
#retourner l'equipe
return equipe

#fonction texte_personnage
def texte_personnage(perso):
#   retourner le nom, l'attaque, l'hp, la defense
    return f"{perso['name']} HP {perso['hp']} ATK {perso['atk']} DEF {perso['defense']}"

#fonction boucle_vagues 
def boucle_vagues(base, equipe):
    #vague commence a 1
    vague = 1
    #tant que infini
    while True:
        #creer combat de monstre aleatoire
        monstre = monstre_aleatoire(base)
        #afficher la vague avec nouveau monstre listmongodb apparait
        print(f"\n=== VAGUE X {vague} : {monstre['name']} apparait ! ===")
        #si combattre_vague est faux retourner vague
        if not combattre_vague(equipe, monstre):
        #vague = vague + 1
        vague = vague + 1
 
#fonction combattre vague
def combattre_vague(equipe, monstre):
#   tant que infini
    while True:
#       heros attaque
        heros_attaquant(equipe, monstre)
#       si monstre mort 
        if not est_vivant(monstre):
#           affcher "monstre  vaincu"
            print(f"{monstre['name']} est vaincu !")
#           retourner vrai
            return True
#       monstre attaque
        monstre_attaque(monstre, equipe)
#       si heros vivant est vide
        if heros_vivants(equipe) == []:
#           afficher "toute l'equipe KO"
            print("Toute l'equipe est KO !")
#           retourner faux
            return False

#fonction heros attaque
def heros_attaquant(equipe, monstre):
#   pour chaque heros dans heros vivant
    for heros in heros_vivants(equipe):
#       si monstre vivant
        if est_vivant(monstre):
#           heros attaque monstre
            attaquer(heros, monstre)
#           afficher "heros inflige des dégats"

#fonction monstres attaque
def monstre_attaque(monstre, equipe):
#   cible est un heros au hasard dans heros vivant
    cible = random.choice(heros_vivants(equipe))
#   le monstre attaque cible
    attaquer(monstre, cible)

# fonction attaquer(attaquant, cible)
def attaquer(attaquant, cible):
    # degats = atk de l'attaquant - defense de la cible
    degats = attaquant["atk"] - cible["defense"]
    # si les degats sont inferieurs a 1 : mettre les degats a 1
    if degats < 1:
        degats = 1
    # enlever les degats aux hp de la cible
    cible["hp"] = cible["hp"] - degats
    # si les hp sont inferieurs a 0 : mettre les hp a 0
    if cible["hp"] < 0:
        cible["hp"] = 0
    # afficher "attaquant inflige X degats a cible, il reste Y hp"
    print(f"{attaquant['name']} inflige {degats} dégâts à {cible['name']}, il reste {cible['hp']} hp")
    # si la cible n'est pas vivante : afficher "cible est KO"
    if not est_vivant(cible):
        print(f"{cible['name']} est KO !")


# fonction est_vivant(perso)
def est_vivant(perso):
    # retourner vrai si hp > 0
    return perso["hp"] > 0


# fonction heros_vivants(equipe)
def heros_vivants(equipe):
    # retourner les heros de l'equipe ou est_vivant est vrai
    return [heros for heros in equipe if est_vivant(heros)]