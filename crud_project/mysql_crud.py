
import mysql.connector
from mysql.connector import Error

def get_connection():
    """Crée et retourne une connexion à la base de données MySQL."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='crud_db',  
            user='root',
            password='',
            port=3306  
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Erreur de connexion MySQL", e)
    return None

def create_table():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    quantity INT NOT NULL,
                    price DECIMAL(10,2) NOT NULL
                )
            """)
            connection.commit()
        finally:
            cursor.close()
            connection.close()

def add_product(name, quantity, price):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            sql = "INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, quantity, price))
            connection.commit()
            print("Produit ajouté avec succès.")
        finally:
            cursor.close()
            connection.close()

def get_products():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
            return products
        finally:
            cursor.close()
            connection.close()

def update_product(product_id, name, quantity, price):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            sql = "UPDATE products SET name=%s, quantity=%s, price=%s WHERE id=%s"
            cursor.execute(sql, (name, quantity, price, product_id))
            connection.commit()
            print("Produit mis à jour.")
        finally:
            cursor.close()
            connection.close()

def delete_product(product_id):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            sql = "DELETE FROM products WHERE id=%s"
            cursor.execute(sql, (product_id,))
            connection.commit()
            print("Produit supprimé.")
        finally:
            cursor.close()
            connection.close()