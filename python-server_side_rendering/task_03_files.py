from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

DATA_JSON = 'products.json'
DATA_CSV = 'products.csv'

def read_products_from_json(path=DATA_JSON):
    """Retourne une liste de dicts ou lève des exceptions si erreur."""
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # s'assurer d'une liste de dicts
    products = []
    for p in data:
        # Normaliser types
        try:
            pid = int(p.get('id'))
        except Exception:
            pid = None
        products.append({
            'id': pid,
            'name': p.get('name', ''),
            'category': p.get('category', ''),
            'price': float(p.get('price')) if p.get('price') not in (None, '') else None
        })
    return products

def read_products_from_csv(path=DATA_CSV):
    """Lit le CSV et renvoie une liste de dicts normalisés."""
    products = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                pid = int(row.get('id')) if row.get('id') not in (None, '') else None
            except Exception:
                pid = None
            try:
                price = float(row.get('price')) if row.get('price') not in (None, '') else None
            except Exception:
                price = None
            products.append({
                'id': pid,
                'name': row.get('name', ''),
                'category': row.get('category', ''),
                'price': price
            })
    return products

@app.route('/products')
def products():
    """
    Query params:
      - source: 'json' or 'csv'  (required)
      - id: optional (integer) to filter a single product
    """
    source = request.args.get('source', '').lower()
    id_param = request.args.get('id', None)

    error = None
    products_list = []

    # validate source
    if source not in ('json', 'csv'):
        error = "Wrong source"
        return render_template('product_display.html', products=[], error=error, source=source, requested_id=id_param)

    # try to read data
    try:
        if source == 'json':
            if not os.path.exists(DATA_JSON):
                raise FileNotFoundError(f"{DATA_JSON} not found")
            products_list = read_products_from_json(DATA_JSON)
        else:  # csv
            if not os.path.exists(DATA_CSV):
                raise FileNotFoundError(f"{DATA_CSV} not found")
            products_list = read_products_from_csv(DATA_CSV)
    except FileNotFoundError as e:
        error = f"Data file not found: {e}"
        return render_template('product_display.html', products=[], error=error, source=source, requested_id=id_param)
    except json.JSONDecodeError:
        error = "Error decoding JSON file."
        return render_template('product_display.html', products=[], error=error, source=source, requested_id=id_param)
    except Exception as e:
        error = f"Error reading data: {e}"
        return render_template('product_display.html', products=[], error=error, source=source, requested_id=id_param)

    # If id param provided -> filter
    if id_param is not None:
        try:
            requested_id = int(id_param)
        except ValueError:
            error = "Invalid id value"
            return render_template('product_display.html', products=[], error=error, source=source, requested_id=id_param)

        # find product
        filtered = [p for p in products_list if p.get('id') == requested_id]
        if not filtered:
            error = "Product not found"
            return render_template('product_display.html', products=[], error=error, source=source, requested_id=id_param)
        # else show single product (pass list with single element)
        return render_template('product_display.html', products=filtered, error=None, source=source, requested_id=id_param)

    # no id -> show all
    return render_template('product_display.html', products=products_list, error=None, source=source, requested_id=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
