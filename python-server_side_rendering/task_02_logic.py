from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except FileNotFoundError:
        print("File items.json not found.")
        items_list = []
    except json.JSONDecodeError:
        print("Error decoding JSON file.")
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
