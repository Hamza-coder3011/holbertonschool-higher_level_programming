#!/usr/bin/python
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_products(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            products = []
            for prod in data:
                products.append({
                    "id": int(prod.get("id", 0)),
                    "name": str(prod.get("name", "")),
                    "category": str(prod.get("category", "")),
                    "price": float(prod.get("price", 0))
                })
            return products
    except Exception as e:
        print("JSON read error:", e)
        return []

def read_csv_products(filename):
    products = []
    try:
        with open(filename, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                products.append({
                    "id": int(row.get("id", 0)),
                    "name": row.get("name", ""),
                    "category": row.get("category", ""),
                    "price": float(row.get("price", 0))
                })
        return products
    except Exception as e:
        print("CSV read error:", e)
        return []

def read_sql_products(db_filename):
    products = []
    try:
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": int(row[0]),
                "name": row[1],
                "category": row[2],
                "price": float(row[3])
            })
        conn.close()
        return products
    except Exception as e:
        print("SQL read error:", e)
        return []

@app.route('/products')
def display_products():
    src = request.args.get('source')
    id_param = request.args.get('id')
    error = None
    products = []

    if src == "json":
        products = read_json_products("products.json")
    elif src == "csv":
        products = read_csv_products("products.csv")
    elif src == "sql":
        products = read_sql_products("products.db")
    else:
        error = "Wrong source"
        return render_template("product_display.html", error=error, products=[])

    
    if id_param:
        try:
            id_val = int(id_param)
        except Exception:
            error = "Invalid id parameter."
            return render_template("product_display.html", error=error, products=[])
        filtered = [p for p in products if p["id"] == id_val]
        if not filtered:
            error = "Product not found"
            return render_template("product_display.html", error=error, products=[])
        products = filtered

    return render_template("product_display.html", products=products, error=error)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception:
        return []

def read_csv_file(file_path):
    try:
        with open(file_path, newline='') as file:
            reader = csv.DictReader(file)
            return [
                {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                }
                for row in reader
            ]
    except Exception:
        return []

def read_sqlite_db(db_path):
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # pour récupérer un dict-like
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        # Convertir les rows en liste de dicts
        products = []
        for row in rows:
            products.append({
                "id": row["id"],
                "name": row["name"],
                "category": row["category"],
                "price": row["price"]
            })
        return products
    except Exception:
        return []

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None
    products = []

    if source == 'json':
        products = read_json_file("products.json")
    elif source == 'csv':
        products = read_csv_file("products.csv")
    elif source == 'sql':
        products = read_sqlite_db("products.db")
    else:
        error = "Wrong source. Please specify 'json', 'csv' or 'sql'."
        return render_template("product_display.html", error=error)

    if product_id is not None:
        filtered = [p for p in products if p["id"] == product_id]
        if not filtered:
            error = "Product not found"
            products = []
        else:
            products = filtered

    return render_template("product_display.html", products=products, error=error)


if __name__ == '__main__':
    app.run(debug=True)
