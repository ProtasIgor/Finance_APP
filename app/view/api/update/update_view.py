from flask import request
from app.app import app
from ..handler_request import Handler_Request
from app.model.model import Model_Api
from app.model.table_enum import TableEnum

handler_request = Handler_Request()
model = Model_Api()

@app.route('/api/family.update', methods=['POST'])
def api_update_family():
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.update_family,
        TableEnum.family.value,
        'id', 'balance', 'address'
    )

@app.route('/api/family.balance.update', methods=['POST'])
def api_update_family_balance():
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.update_family_balance,
        TableEnum.family.value,
        'id', 'balance'
    )

@app.route('/api/family.address.update', methods=['POST'])
def api_update_family_address():
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.update_family_address,
        TableEnum.family.value,
        'id', 'address'
    )