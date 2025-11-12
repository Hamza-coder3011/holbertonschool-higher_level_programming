from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_data():
    try:
        with open('products.json', 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return None

def read_csv_data():
    try:
        products = []
        with open('products.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None

def read_sqlite_data():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [{'id': r[0], 'name': r[1], 'category': r[2], 'price': r[3]} for r in rows]
    except Exception as e:
        print(f"Error reading SQLite DB: {e}")
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error_message = None

    if source == 'json':
        products = read_json_data()
        if products is None:
            error_message = "Error loading JSON data."
    elif source == 'csv':
        products = read_csv_data()
        if products is None:
            error_message = "Error loading CSV data."
    elif source == 'sql':
        products = read_sqlite_data()
        if products is None:
            error_message = "Error loading data from database."
    else:
        error_message = "Wrong source. Please use ?source=json, ?source=csv, or ?source=sql."

    # filtrer par id si fourni
    if not error_message and product_id:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            error_message = "Product not found."

    return render_template('product_display.html',
                           products=products,
                           error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
