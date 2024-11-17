from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from user_operations import UserDatabase
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
api = Api(app)
api.init_app(app)
db = UserDatabase()

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    user_name = data.get('user_name')
    user_surname = data.get('user_surname')

    if not user_name or not user_surname:
        return jsonify({"detail": "user_name and user_surname are required"}), 400

    try:
        db.add_user(user_name, user_surname)
        return jsonify({"message": "User created successfully"}), 201
    except SQLAlchemyError as e:
        return jsonify({"detail": str(e)}), 500


@app.route('/user', methods=['GET'])
def read_users():
    user_id = request.args.get('user_id', None)
    try:
        if user_id:
            user = db.get_user(user_id)
            if user:
                return jsonify({"user": user.to_dict()})
            else:
                return jsonify({"detail": "User not found"}), 404
        else:
            users = db.get_users()
            return jsonify({"users": users})
    except SQLAlchemyError as e:
        return jsonify({"detail": str(e)}), 500


@app.route('/user', methods=['DELETE'])
def delete_user():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"detail": "user_id is required"}), 400

    try:
        db.delete_user(user_id)
        return jsonify({"message": "User deleted successfully"}), 200
    except SQLAlchemyError as e:
        return jsonify({"detail": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)