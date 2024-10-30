from flask import request
from app.app import app
from ..handler_request import Handler_Request
from app.model.model import Model_Api
from app.model.table_enum import TableEnum

handler_request = Handler_Request()
model = Model_Api()

@app.route('/api/family.update', methods=['POST'])
def api_update_family():
    return handler_request.handle_update_request(
        request.get_json(silent=True),
        model.update_family,
        TableEnum.family.value,
        'id', 'balance', 'address'
    )

@app.route('/api/family.balance.update', methods=['POST'])
def api_update_family_balance():
    return handler_request.handle_update_request(
        request.get_json(silent=True),
        model.update_family_balance,
        TableEnum.family.value,
        'id', 'balance'
    )

@app.route('/api/family.address.update', methods=['POST'])
def api_update_family_address():
    return handler_request.handle_update_request(
        request.get_json(silent=True),
        model.update_family_address,
        TableEnum.family.value,
        'id', 'address'
    )

@app.route('/api/account_status.update', methods=['POST'])
def api_update_account_status():
    return handler_request.handle_update_request(
        request.get_json(silent=True),
        model.update_account_status,
        TableEnum.personaccountstatus.value,
        'id', 'name'
    )

@app.route('/api/category_operation.update', methods=['POST'])
def api_update_category_operation():
    return handler_request.handle_update_request(
        request.get_json(silent=True),
        model.update_category_operation,
        TableEnum.operationcategory.value,
        'id', 'name', 'person_id', 'for_family_id'
    )

@app.route('/api/gender.update', methods=['POST'])
def api_update_gender():
    return handler_request.handle_update_request(
        request.get_json(silent=True),
        model.update_gender,
        TableEnum.gender.value,
        'id', 'name'
    )

@app.route('/api/operation.update', methods=['POST'])
def api_update_operation():
    return handler_request.handle_update_request(
        request.get_json(silent=True),
        model.update_operation,
        TableEnum.operation.value,
        'id', 'name', 'comment', 'operation_category_id'
    )

@app.route('/api/operation_type.update', methods=['POST'])
def api_update_operation_type():
    return handler_request.handle_update_request(
        request.get_json(silent=True),
        model.update_operation_type,
        TableEnum.operationtype.value,
        'id', 'value'
    )

@app.route('/api/operation.category.update', methods=['POST'])
def api_update_operation_category():
    return handler_request.handle_update_request(
        request.get_json(silent=True),
        model.update_operation_category,
        TableEnum.operation.value,
        'id', 'operation_category_id'
    )

@app.route('/api/operation.comment.update', methods=['POST'])
def api_update_operation_comment():
    return handler_request.handle_update_request(
        request.get_json(silent=True),
        model.update_operation_comment,
        TableEnum.operation.value,
        'id', 'comment'
    )

@app.route('/api/operation.name.update', methods=['POST'])
def api_update_operation_name():
    return handler_request.handle_update_request(
        request.get_json(silent=True),
        model.update_operation_name,
        TableEnum.operation.value,
        'id', 'name'
    )

@app.route('/api/person.update', methods=['POST'])
def api_update_person():
    return handler_request.handle_update_request(
        request.get_json(silent=True),
        model.update_person,
        TableEnum.person.value,
        'id', 'name', 'lastname', 'surname', 'age', 'phone', 'family_id', 'gender_id'
    )

@app.route('/api/secret_key_person.update', methods=['POST'])
def api_update_secret_key_person():
    return handler_request.handle_update_request(
        request.get_json(silent=True),
        model.update_secret_key_person,
        TableEnum.personsecretkey.value,
        'id', 'value'
    )