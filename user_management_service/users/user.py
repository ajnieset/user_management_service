from flask import abort, Blueprint, jsonify, request

bp = Blueprint("user", __name__, url_prefix="/user")

@bp.get("/<user_id>")
def get_user(user_id: str):
    return jsonify({"id": user_id})