
from tinydb import TinyDB, Query


db = TinyDB('tinydb_db.json')

def add_product_tiny(name, quantity, price):
    db.insert({'name': name, 'quantity': quantity, 'price': price})
    print("Produit ajouté à TinyDB.")

def get_products_tiny():
    return db.all()

def update_product_tiny(product_id, name, quantity, price):
    db.update({'name': name, 'quantity': quantity, 'price': price}, doc_ids=[product_id])
    print("Produit mis à jour dans TinyDB.")

def delete_product_tiny(product_id):
    db.remove(doc_ids=[product_id])
    print("Produit supprimé de TinyDB.")