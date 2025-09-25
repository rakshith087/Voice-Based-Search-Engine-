import json

def load_catalog():
    with open('product_catalog.json') as f:
        return json.load(f)

def search_products(query, catalog):
    query = query.lower()
    results = []
    for product in catalog:
        if query in product['name'].lower() or query in product['description'].lower():
            results.append(product)
    return results
