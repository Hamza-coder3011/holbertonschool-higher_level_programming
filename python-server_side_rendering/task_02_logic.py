#!/usr/bin/python
from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def items():
    items_list = []
    
    try:
        with open('items.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            if 'items' in data and type(data['items']) is list:
                items_list = data['items']
    except Exception as e:
        print("Erreur de lecture de items.json:", e)
        
    return render_template('items.html', items=items_list)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
