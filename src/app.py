from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
   { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    lista_length = len(todos)
    if position >= lista_length or position < 0:
        return jsonify({"message": "That position doesn't exist in the list"}), 404
    print("This is the position to delete:", position)
    todos.pop(position)
    return jsonify(todos), 200

# Estas dos líneas siempre deben estar al final de tu archivo app.py
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)