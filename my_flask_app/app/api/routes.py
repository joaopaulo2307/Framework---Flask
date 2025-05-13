from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required

api_bp = Blueprint('api', __name__)

@api_bp.route('/token', methods=['POST'])
def get_token():
    username = request.json.get('username')
    if username == 'admin':
        token = create_access_token(identity=username)
        return jsonify(access_token=token)
    return jsonify(msg='Credenciais inválidas'), 401

@api_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message='Você acessou uma rota protegida!')