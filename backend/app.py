from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS
import os
from bson import ObjectId
# Instantiation
app = Flask(__name__)

# MongoDB configuration (use environment variables for security)
app.config['MONGO_URI'] = os.getenv(
    'MONGO_URI',
    'mongodb+srv://jassercherif:xXoqLKh76ktsIxHP@cluster0.4n47d.mongodb.net/mydatabase?retryWrites=true&w=majority&appName=Cluster0'
)

# Initialize PyMongo
try:
    mongo = PyMongo(app)
    db = mongo.db  # Reference to the database
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    db = None

# Settings
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


# Routes

@app.route('/users', methods=['POST'])
def create_user():
    try:
        # Récupérer les données envoyées dans le corps de la requête
        data = request.json
        
        # Vérifier que toutes les informations nécessaires sont présentes
        if not data.get('name') or not data.get('email') or not data.get('password'):
            return jsonify({'message': 'Missing required fields'}), 400
        
        # Créer un nouvel utilisateur dans la base de données
        new_user = {
            'name': data['name'],
            'email': data['email'],
            'password': data['password']
        }
        
        # Insérer l'utilisateur dans la collection 'users'
        result = db.users.insert_one(new_user)
        
        # Retourner un message de succès avec l'ID du nouvel utilisateur
        return jsonify({
            'message': 'User Created',
            'user_id': str(result.inserted_id)
        }), 201
    
    except Exception as e:
        # Gérer les erreurs et renvoyer un message d'erreur
        return jsonify({'error': str(e)}), 500



@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    try:
        # Assuming you're getting JSON data in the body
        data = request.json
        
        # Check if the document exists
        result = db.users.update_one(
            {'_id': ObjectId(id)}, 
            {"$set": {
                'name': data['name'],
                'email': data['email'],
                'password': data['password']
            }}
        )
        
        # Check if any document was modified
        if result.modified_count == 0:
            return jsonify({'message': 'No changes made to the user'}), 400
        
        return jsonify({'message': 'User Updated', 'user_id': id})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    try:
        # Tentative de suppression de l'utilisateur
        result = db.users.delete_one({'_id': ObjectId(id)})
        
        # Vérifier si l'utilisateur a été trouvé et supprimé
        if result.deleted_count == 0:
            return jsonify({'message': 'User not found'}), 404
        
        # Retourner un message de succès si l'utilisateur a été supprimé
        return jsonify({'message': 'User Deleted'}), 200
    
    except Exception as e:
        # Gérer les erreurs et renvoyer un message d'erreur
        return jsonify({'error': str(e)}), 500

@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for doc in db.users.find():
        users.append({
            '_id': str(ObjectId(doc['_id'])),
            'name': doc['name'],
            'email': doc['email'],
            'password': doc['password']
        })
    return jsonify(users)

@app.route('/users/<id>', methods=['GET'])
def getUser(id):
    try:
        # Recherche de l'utilisateur par son ObjectId
        user = db.users.find_one({'_id': ObjectId(id)})
        
        # Vérifier si l'utilisateur existe
        if user is None:
            return jsonify({'message': 'User not found'}), 404
        
        # Retourner les informations de l'utilisateur sous forme de JSON
        return jsonify({
            '_id': str(user['_id']),
            'name': user['name'],
            'email': user['email'],
            'password': user['password']
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
