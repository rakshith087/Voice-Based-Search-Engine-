from flask import Flask, render_template, request, jsonify
from nlp_utils import load_catalog, search_products

app = Flask(__name__)
catalog = load_catalog()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = search_products(query, catalog)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
