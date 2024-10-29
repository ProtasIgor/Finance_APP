from flask import request
from app.app import app
from ..handler_request import Handler_Request
from app.model.model import Model_Api
from app.model.table_enum import TableEnum

handler_request = Handler_Request()
model = Model_Api()

@app.route('/api/family.get', methods=['POST'])
def api_get_family():
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.get_family,
        TableEnum.family.value,
        'id'
    )