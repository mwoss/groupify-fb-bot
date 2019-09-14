from os import environ

from flask import Blueprint, request, jsonify

auth_api = Blueprint('auth_api', __name__, url_prefix='/webhook')


@auth_api.route('/', methods=['GET', 'POST'])
def verify():
    hub_challenge = request.args.get('hub.challenge')
    hub_mode = request.args.get('hub.mode')
    is_verified = request.args.get('hub.verify_token') == environ.get("GROUPIFY_TOKEN")

    if hub_mode and is_verified:
        return hub_challenge, 200

    return jsonify({'error': 'Non authorized'}), 403
