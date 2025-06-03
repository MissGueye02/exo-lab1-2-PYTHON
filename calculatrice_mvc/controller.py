"""
Module Controller : coordonne la logique de la calculatrice.
"""

from model import addition, soustraction, multiplication, division
from view import afficher_menu, saisir_valeurs, afficher_resultat, message_erreur

def lancer_calculatrice():
    """Fonction principale qui lance la calculatrice."""
    while True:
        choix = afficher_menu()
        if choix == '5':
            print("Au revoir !")
            break
        a, b = saisir_valeurs()
        if a is None or b is None:
            continue  # Si la saisie est invalide, redemander les valeurs
        if choix == '1':
            resultat = addition(a, b)
        elif choix == '2':
            resultat = soustraction(a, b)
        elif choix == '3':
            resultat = multiplication(a, b)
        elif choix == '4':
            resultat = division(a, b)
        else:
            message_erreur("Choix invalide")
            continue
        afficher_resultat(resultat)