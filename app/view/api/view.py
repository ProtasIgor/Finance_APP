from flask import jsonify, make_response, request
from app.app import app
from .factory_response import List_Response # будет из handler !!!!!!!!!!
from .handler_request import HandlerRequest
from app.model.model import Model_Api

handler_request = HandlerRequest()
list_response = List_Response()
model = Model_Api()

@app.route('/api/family', methods=['POST'])
def api_get_family():
    try:
        data = request.get_json(silent=True)
        # Проверка входных данных на формат json + их наличие
        if data is None or not request.is_json:
            return list_response.response_error_request_not_data
        # Проверка входных данных на наличие всех обязательных свойств
        if check_exist_request_data_item(data, 'family_id') == False:
            return list_response.get_response_error_request_not_data_item(
                get_string_not_exist_request_data_item(data, 'family_id'))
        # Запрос к БД
        response = make_response(model.get_family(data.get('family_id')), 200)
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    except Exception:
        return jsonify({"error": "Неизвестная ошибка"}), 400


@app.route('/api/family.balance', methods=['GET', 'POST'])
def api_update_family_balance():
    response = make_response()
    if request.method == 'POST':
        data = request.get_json()
        family_id = data.get('family_id')
        balance = data.get('balance')

        if not family_id:
            response = make_response(jsonify({'status':'error', 'error': 'Не указан family_id'}), 400) # Bad Request
        elif not balance:
            response = make_response(jsonify({'status':'error', 'error': 'balance'}), 400) # Bad Request
        else:
            response = make_response(model.update_family_balance(family_id, balance), 200)
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

@app.route('/api/family.address', methods=['GET', 'POST'])
def api_update_family_address():
    response = make_response()
    if request.method == 'POST':
        data = request.get_json()
        family_id = data.get('family_id')
        address = data.get('address')

        if not family_id:
            response = make_response(jsonify({'status':'error', 'error': 'Не указан family_id'}), 400) # Bad Request
        elif not address:
            response = make_response(jsonify({'status':'error', 'error': 'Не указан family_id'}), 400) # Bad Request
        else:
            response = make_response(model.update_family_address(family_id, address), 200)
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response





def check_exist_request_data_item(data, *properties):
    for property in properties:
        print(data)
        print(type(property))
        if not data.get(property):
            return False
    return True

def get_string_not_exist_request_data_item(data, *properties):
    list_not_exist = []
    for property in properties:
        if not data.get(property):
            list_not_exist.append(property)
    result = ", ".join(map(str, list_not_exist)) + "."
    print(result)
    return result