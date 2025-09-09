from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from web_scrape import WebScraper
from db_connect import Database

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])
app.config['CORS_HEADERS'] = 'Content-Type'
app.json.ensure_ascii = False

@app.route('/')
def get_status():
    return jsonify({'Status': 'OK'})

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    text = data.get('text','')
    print('Received input:', text)
    x = WebScraper(text).get_item_info()
    return jsonify({"message": x})

@app.route('/get-products', methods=['GET','POST'])
def get_products():
    db = Database()
    result = db.custom_query('SELECT ProductName FROM products GROUP BY ProductName ORDER BY MAX(id) DESC;')
    print(jsonify({"message": result}))
    return jsonify({"message": result})