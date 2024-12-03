from flask import request
from app.app import app
from ..handler_request import Handler_Request
from app.model.model import Model_Api
from app.model.table_enum import TableEnum

handler_request = Handler_Request()
model = Model_Api()

@app.route('/api/account_status.delete', methods=['POST'])
def api_delete_account_status():
    return handler_request.handle_delete_request(
        request.get_json(silent=True),
        model.delete_account_status,
        TableEnum.personaccountstatus.value,
        'id'
    )

@app.route('/api/category_operation.delete', methods=['POST'])
def api_delete_category_operation():
    return handler_request.handle_delete_request(
        request.get_json(silent=True),
        model.delete_category_operation,
        TableEnum.operationcategory.value,
        'id'
    )

@app.route('/api/family.delete', methods=['POST'])
def api_delete_family():
    return handler_request.handle_delete_request(
        request.get_json(silent=True),
        model.delete_family,
        TableEnum.family.value,
        'id'
    )

@app.route('/api/gender.delete', methods=['POST'])
def api_delete_gender():
    return handler_request.handle_delete_request(
        request.get_json(silent=True),
        model.delete_gender,
        TableEnum.gender.value,
        'id'
    )

@app.route('/api/operation.delete', methods=['POST'])
def api_delete_operation():
    return handler_request.handle_delete_request(
        request.get_json(silent=True),
        model.delete_operation,
        TableEnum.operation.value,
        'id'
    )

@app.route('/api/operation_type.delete', methods=['POST'])
def api_delete_operation_type():
    return handler_request.handle_delete_request(
        request.get_json(silent=True),
        model.delete_operation_type,
        TableEnum.operationtype.value,
        'id'
    )

@app.route('/api/person_goal.delete', methods=['POST'])
def api_delete_person_goal():
    return handler_request.handle_delete_request(
        request.get_json(silent=True),
        model.delete_person_goal,
        TableEnum.persongoal.value,
        'id'
    )

@app.route('/api/secret_key_person.delete', methods=['POST'])
def api_delete_secret_key_person():
    return handler_request.handle_delete_request(
        request.get_json(silent=True),
        model.delete_secret_key_person,
        TableEnum.personsecretkey.value,
        'id'
    )