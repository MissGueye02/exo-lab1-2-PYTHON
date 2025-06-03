
import sys
from mysql_crud import create_table, add_product, get_products, update_product, delete_product
from tinydb_crud import add_product_tiny, get_products_tiny, update_product_tiny, delete_product_tiny

def display_menu():
    print("\nMenu Principal :")
    print("1. Gestion de stock avec MySQL")
    print("2. Gestion de stock avec TinyDB")
    print("3. Quitter")
    return input("Choix (1/2/3) : ")

def mysql_menu():
    while True:
        print("\n-- Menu MySQL --")
        print("1. Ajouter un produit")
        print("2. Afficher tous les produits")
        print("3. Mettre à jour un produit")
        print("4. Supprimer un produit")
        print("5. Retour au menu principal")
        choice = input("Choix : ")
        if choice == '1':
            name = input("Nom du produit : ")
            quantity = int(input("Quantité : "))
            price = float(input("Prix unitaire : "))
            add_product(name, quantity, price)
        elif choice == '2':
            products = get_products()
            print("Liste des produits :")
            for prod in products:
                print(prod)
        elif choice == '3':
            product_id = int(input("ID du produit à mettre à jour : "))
            name = input("Nouveau nom du produit : ")
            quantity = int(input("Nouvelle quantité : "))
            price = float(input("Nouveau prix : "))
            update_product(product_id, name, quantity, price)
        elif choice == '4':
            product_id = int(input("ID du produit à supprimer : "))
            delete_product(product_id)
        elif choice == '5':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def tinydb_menu():
    while True:
        print("\n-- Menu TinyDB --")
        print("1. Ajouter un produit")
        print("2. Afficher tous les produits")
        print("3. Mettre à jour un produit")
        print("4. Supprimer un produit")
        print("5. Retour au menu principal")
        choice = input("Choix : ")
        if choice == '1':
            name = input("Nom du produit : ")
            quantity = int(input("Quantité : "))
            price = float(input("Prix unitaire : "))
            add_product_tiny(name, quantity, price)
        elif choice == '2':
            products = get_products_tiny()
            print("Liste des produits :")
            for prod in products:
                print(prod)
        elif choice == '3':
            product_id = int(input("ID du produit à mettre à jour (doc_id) : "))
            name = input("Nouveau nom du produit : ")
            quantity = int(input("Nouvelle quantité : "))
            price = float(input("Nouveau prix : "))
            update_product_tiny(product_id, name, quantity, price)
        elif choice == '4':
            product_id = int(input("ID du produit à supprimer (doc_id) : "))
            delete_product_tiny(product_id)
        elif choice == '5':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def main():
    # Pour MySQL, on crée la table si elle n'existe pas
    create_table()
    while True:
        choice = display_menu()
        if choice == '1':
            mysql_menu()
        elif choice == '2':
            tinydb_menu()
        elif choice == '3':
            print("Fin du programme.")
            sys.exit(0)
        else:
            print("Choix invalide. Veuillez choisir 1, 2 ou 3.")

if __name__ == "__main__":
    main()