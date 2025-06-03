"""
Module View : gère l'affichage des menus et la saisie des données utilisateur.
"""

def afficher_menu():
    """Affiche le menu principal de la calculatrice et retourne le choix de l'utilisateur."""
    print("\n=== Calculatrice MVC ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")
    choix = input("Choisissez une opération (1-5): ")
    return choix

def saisir_valeurs():
    """Demande à l'utilisateur de saisir deux nombres et retourne ces valeurs."""
    try:
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))
        return a, b
    except ValueError:
        print("Entrée invalide. Veuillez saisir des nombres.")
        return None, None

def afficher_resultat(resultat):
    """Affiche le résultat de l'opération."""
    print(f"Le résultat est : {resultat}")

def message_erreur(message):
    """Affiche un message d'erreur."""
    print(f"Erreur : {message}")