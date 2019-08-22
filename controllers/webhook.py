from flask import Blueprint, request, jsonify

hook_api = Blueprint('hook_api', __name__, url_prefix='/message_webhook')


def process_message(event: dict) -> None:
    return None


@hook_api.route('/', methods=['GET', 'POST'])
def handle_message():
    content = request.get_json()

    if content['object'] != 'page':
        return jsonify({'error': 'Invalid data received'}), 422

    for entry in content['entry']:
        for event in entry['messaging']:
            if event['message'] and event['message']['text']:
                process_message(event)

    return jsonify({'result': 'Message parsed properly'}), 200