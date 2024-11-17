from flask import Flask, request, jsonify
from flask_restful import Api
from thing_operations import ThingDatabase
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
api = Api(app)
api.init_app(app)
db = ThingDatabase()

@app.route('/thing', methods=['POST'])
def create_user():
    data = request.get_json()
    thing_name = data.get('thing_name')

    if not thing_name:
        return jsonify({"detail": "user_name and user_surname are required"}), 400

    try:
        db.add_thing(thing_name)
        return jsonify({"message": "User created successfully"}), 201
    except SQLAlchemyError as e:
        return jsonify({"detail": str(e)}), 500


@app.route('/thing', methods=['GET'])
def read_users():
    thing_id = request.args.get('thing_id', None)
    try:
        if thing_id:
            user = db.get_thing(thing_id)
            if user:
                return jsonify({"user": user.to_dict()})
            else:
                return jsonify({"detail": "User not found"}), 404
        else:
            users = db.get_things()
            return jsonify({"users": users})
    except SQLAlchemyError as e:
        return jsonify({"detail": str(e)}), 500


@app.route('/thing', methods=['DELETE'])
def delete_user():
    thing_id = request.args.get('thing_id')
    if not thing_id:
        return jsonify({"detail": "user_id is required"}), 400

    try:
        db.delete_thing(thing_id)
        return jsonify({"message": "User deleted successfully"}), 200
    except SQLAlchemyError as e:
        return jsonify({"detail": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8001)