import os
from utils import ouvrir_base, lire_top3, recuperer_choix_utilisateur, attendre_entree
from game import lancer_partie

#fonction effacer l'ecran
def effacer_ecran():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#fonction menu
def main():
#   utilisation base de donnees
    base = ouvrir_base()
#   tant que infini
    while True:
#   effacer l'ecran et afficher "COMBAT GAME"
        effacer_ecran()
        print("===COMBAT GAME===")
        choix = recuperer_choix_utilisateur(["Jouer", "Top 3", "Quitter"])
# si choix = 1 lancer la partie
        if choix == 1:
            lancer_partie(base)
# si choix = 2 afficher top 3 des scores
        elif choix == 2:
            afficher_top3(base)
# si choix = 3 quitter 
        elif choix == 3:
            break

#fonction afficher le top 3 
def afficher_top3():
#   top = lire_top3
    top = lire_top3(base)
#   si top est vide afficher aucun score
    if top == []:
        print("Aucun score pour l'instant")
#   pour chaque score afficher le rang le pseudo et le nombre de vague 
    for rang, score in enumerate(top, start=1):
        print(f"{rang}. {score['vague']}")
#   attendre_entree
    attendre_entree()

if __name__ == "__main__":
    main()