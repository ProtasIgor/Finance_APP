
from flask import jsonify, make_response
from app.app import app

with app.app_context():
    class List_Response():
        response_error_request_not_data = make_response(
            jsonify({'status':'error',
                     'error': 'Тело запроса должно содержать JSON. Неверный формат JSON'}),
                       400)

        def get_response_error_request_not_data(self):
            return self.response_error_request_not_data

        def get_response_error_request_not_data_item(self, error_message):
            return make_response( jsonify({'status':'error',
                     'error': 'В теле запроса отсутствуют обязательные поля: {}'.format(error_message)}), 400)
