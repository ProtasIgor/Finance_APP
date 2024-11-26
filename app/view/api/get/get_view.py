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

@app.route('/api/account_status.get', methods=['POST'])
def api_get_account_status():
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.get_account_status,
        TableEnum.personaccountstatus.value,
        'id'
    )

@app.route('/api/category_operation.get', methods=['POST'])
def api_get_category_operation():
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.get_category_operation,
        TableEnum.operationcategory.value,
        'id'
    )

@app.route('/api/gender.get', methods=['POST'])
def api_get_gender():
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.get_gender,
        TableEnum.gender.value,
        'id'
    )

@app.route('/api/operation.get', methods=['POST'])
def api_get_operation():
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.get_operation,
        TableEnum.operation.value,
        'id'
    )

@app.route('/api/operation_type.get', methods=['POST'])
def api_get_operation_type():
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.get_operation_type,
        TableEnum.operationtype.value,
        'id'
    )

@app.route('/api/person.get', methods=['POST'])
def api_get_person():
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.get_person,
        TableEnum.person.value,
        'id'
    )

@app.route('/api/person_account.get', methods=['POST'])
def api_get_person_account():
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.get_person_account,
        TableEnum.personaccount.value,
        'id'
    )

@app.route('/api/person_goal.get', methods=['POST'])
def api_get_person_goal():
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.get_person_goal,
        TableEnum.persongoal.value,
        'id'
    )

@app.route('/api/secret_key_person.get', methods=['POST'])
def api_get_secret_key_person():
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.get_secret_key_person,
        TableEnum.personsecretkey.value,
        'id'
    )

@app.route('/api/registration.get', methods=['POST'])
def api_get_registration():
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.get_registration,
        TableEnum.registration.value,
        'login', 'password'
    )

@app.route('/api/person_by_family.get', methods=['POST'])
def api_get_person_by_family_id():
    return handler_request.handle_get_request(
        request.get_json(silent=True),
        model.get_person_by_family_id,
        TableEnum.person.value,
        'family_id'
    )

@app.route('/api/system_info.get', methods=['GET'])
def api_get_system_info():
    return handler_request.handle_get_system_info_request()