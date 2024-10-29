from flask import request
from app.app import app
from ..handler_request import Handler_Request
from app.model.model import Model_Api

handler_request = Handler_Request()
model = Model_Api()

@app.route('/api/family.balance.update', methods=['POST'])
def api_update_family_balance():
    # Возвращщает make_response()
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.update_family_balance,
        'family_id', 'balance'
    )

@app.route('/api/family.address.update', methods=['POST'])
def api_update_family_address():
    # Возвращщает make_response()
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.update_family_address,
        'family_id', 'address'
    )