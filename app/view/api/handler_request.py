from flask import request, make_response, jsonify
from app.app import app
from .factory_response import Factory_Response

factory_response = Factory_Response()

with app.app_context():

    class Handler_Request():

        def handle_get_request(self, data:dict, model_query, *property):
            """Метод для получения данных из БД.
            :param data: Исходный словарь, из которого будут извлекаться значения, получается путем "data = request.get_json()".
            :param model_query: Метод, который создает запрос к БД, метод класса Model_Api.
            :param property: Список ключей, значения которых нужно извлечь из data.
            :return: Обьект make_response() формат JSON.
            """
            try:
                list_property = list(property)
                import os
                os.system('cls')
                # Проверка входных данных на формат json + их наличие (пустоту)
                if data is None or not isinstance(data, dict) or not request.is_json:
                    return factory_response.response_error_request_not_data
                # Проверка входных данных на наличие всех обязательных свойств
                if self.check_exist_request_data_item(data, list_property) == False:
                    return factory_response.get_response_error_request_not_data_item(
                        self.get_string_not_exist_request_data_item(data, list_property))
                # Создание словаря с параметрами для запроса к БД
                dict_prop = self.make_dict_property_from_request(data, list_property)


                from app.model.model import Model_Api
                #print(Model_Api.get_type_table_property('family', 'id')) доделать метод для проверки request на тип данных +
                # Запрос к БД
                response = make_response(model_query(dict_prop), 200)
                response.headers['Content-Type'] = 'application/json; charset=utf-8'
                return response
            except Exception as ex:
                print(ex.with_traceback())
                return make_response(jsonify({"error": "Неизвестная ошибка"}), 400)

        def handle_update_request(self, data:dict, model_query, *property):
            """Метод для изменения данных в БД.
            :param data: Исходный словарь, из которого будут извлекаться значения, получается путем "data = request.get_json()".
            :param model_query: Метод, который создает запрос к БД, метод класса Model_Api.
            :param property: Список ключей, значения которых нужно извлечь из data.
            :return: Обьект make_response() формат JSON.
            """
            try:
                list_property = list(property)
                import os
                os.system('cls')
                # Проверка входных данных на формат json + их наличие (пустоту)
                if data is None or not isinstance(data, dict) or not request.is_json:
                    return factory_response.response_error_request_not_data
                # Проверка входных данных на наличие всех обязательных свойств
                if self.check_exist_request_data_item(data, list_property) == False:
                    print('o')
                    return factory_response.get_response_error_request_not_data_item(
                        self.get_string_not_exist_request_data_item(data, list_property))
                # Создание словаря с параметрами для запроса к БД
                dict_prop = self.make_dict_property_from_request(data, list_property)
                # Запрос к БД
                response = make_response(model_query(dict_prop), 200)
                response.headers['Content-Type'] = 'application/json; charset=utf-8'
                return response
            except Exception as ex:
                return make_response(jsonify({"error": "Неизвестная ошибка"}), 400)

        def check_exist_request_data_item(self, data:dict, property:list):
            """Проверка входных данных на наличие всех обязательных свойств
                :param data: Исходный словарь, из которого будут извлекаться значения, получается путем "data = request.get_json()".
                :param property: Список ключей, значения которых нужно извлечь из data.
                :return: False, если не хватает хоть одного обязательного поля в :property.
            """
            print(type(data))
            print(type(property))
            for item in property:
                print(item)
                print(type(item))
                #print(data.get(item))
                if not data.get(item):
                    print('oK')
                    return False
            return True

        def get_string_not_exist_request_data_item(self, data:dict, property:list):
            """Возвращает строку отсутствующих обязательных свойств
                :param data: Исходный словарь, из которого будут извлекаться значения, получается путем "data = request.get_json()".
                :param property: Список ключей, значения которых нужно извлечь из data.
                :return: type str.
            """
            list_not_exist = []
            for item in property:
                print(item)
                if not data.get(item):
                    list_not_exist.append(item)
            result = ", ".join(map(str, list_not_exist)) + "."
            print(result)
            return result

        def make_dict_property_from_request(self, data: dict, property: list):
            """Создает словарь полей и их значений
                :param data: Исходный словарь, из которого будут извлекаться значения, получается путем "data = request.get_json()".
                :param property: Список ключей, значения которых нужно извлечь из data.
                :return: type dict.
            """
            new_dict = dict()
            for item in property:
                new_dict[item] = data.get(item)
            return new_dict