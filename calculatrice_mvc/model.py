"""
Module Model : contient les fonctions de calcul de la calculatrice.
"""

def addition(a, b):
    """Renvoie la somme de a et b."""
    return a + b

def soustraction(a, b):
    """Renvoie la différence de a et b."""
    return a - b

def multiplication(a, b):
    """Renvoie le produit de a et b."""
    return a * b

def division(a, b):
    """Renvoie la division de a par b. Gère la division par zéro."""
    if b == 0:
        return "Erreur : Division par zéro"
    return a / b