from flask import request
from app.app import app
from ..handler_request import Handler_Request
from app.model.model import Model_Api
from app.model.table_enum import TableEnum

handler_request = Handler_Request()
model = Model_Api()

@app.route('/api/account_status.add', methods=['POST'])
def api_add_account_status():
    return handler_request.handle_add_request(
        request.get_json(silent=True),
        model.add_account_status,
        TableEnum.personaccountstatus.value,
        'name'
    )

@app.route('/api/category_operation.add', methods=['POST'])
def api_add_category_operation():
    return handler_request.handle_add_request(
        request.get_json(silent=True),
        model.add_category_operation,
        TableEnum.operationcategory.value,
        'name', 'person_id', 'for_family_id'
    )

@app.route('/api/gender.add', methods=['POST'])
def api_add_gender():
    return handler_request.handle_add_request(
        request.get_json(silent=True),
        model.add_gender,
        TableEnum.gender.value,
        'name'
    )

@app.route('/api/operation.add', methods=['POST'])
def api_add_operation():
    return handler_request.handle_add_request(
        request.get_json(silent=True),
        model.add_operation,
        TableEnum.operation.value,
        'name', 'comment', 'operation_type_id', 'operation_category_id', 'person_account_id', 'sum'
    )

@app.route('/api/operation_type.add', methods=['POST'])
def api_add_operation_type():
    return handler_request.handle_add_request(
        request.get_json(silent=True),
        model.add_operation_type,
        TableEnum.operationtype.value,
        'value'
    )

@app.route('/api/person.add', methods=['POST'])
def api_add_person():
    return handler_request.handle_add_request(
        request.get_json(silent=True),
        model.add_person,
        TableEnum.person.value,
        'name', 'lastname', 'surname', 'age', 'phone', 'gender_id', 'family_id'
    )

@app.route('/api/person_account.add', methods=['POST'])
def api_add_person_account():
    return handler_request.handle_add_request(
        request.get_json(silent=True),
        model.add_person_account,
        TableEnum.personaccount.value,
        'person_id', 'status_id'
    )

@app.route('/api/person_goal.add', methods=['POST'])
def api_add_person_goal():
    return handler_request.handle_add_request(
        request.get_json(silent=True),
        model.add_person_goal,
        TableEnum.persongoal.value,
        'person_id', 'name', 'comment', 'sum_total'
    )

@app.route('/api/secret_key_person.add', methods=['POST'])
def api_add_secret_key_person():
    return handler_request.handle_add_request(
        request.get_json(silent=True),
        model.add_secret_key_person,
        TableEnum.personsecretkey.value,
        'value'
    )

@app.route('/api/registration.add', methods=['POST'])
def api_add_registration():
    return handler_request.handle_add_request(
        request.get_json(silent=True),
        model.add_registration,
        TableEnum.registration.value,
        'login', 'password', 'email'
    )