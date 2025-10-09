"""
Task:
- make a dict to store data
- make some CRUD routes
- make CRUD func associated with those routes
- func to create and delete item list take json data as input
- all CRUD unc yield JSON response
- write logics inside the func to CRUD data from the dict


Test:
- Create new item record
- Fetch item list to see the new item added
- Fetch item detail by ID
- update an item!
- fetch the updated item detail to see the change

- delete an item
- fetch item list to see changed
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Storage data menggunakan dictionary
items = {}
current_id = 1

# CREATE - tambah item baru
@app.route('/items', methods=['POST'])
def create_item():
    global current_id
    data = request.get_json()
    items[current_id] = data
    response = {'id': current_id, 'data': data}
    current_id += 1
    return jsonify(response), 201

# READ - ambil semua item
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# READ - ambil detail item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = items.get(item_id)
    if item:
        return jsonify({item_id: item})
    return jsonify({'error': 'Item not found'}), 404

# UPDATE - update item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    if item_id in items:
        items[item_id] = data
        return jsonify({item_id: data})
    return jsonify({'error': 'Item not found'}), 404

# DELETE - hapus item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in items:
        del items[item_id]
        return jsonify({'message': 'Item deleted'})
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
