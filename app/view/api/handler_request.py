from flask import request, make_response, jsonify
from app.app import app
from .factory_response import Factory_Response
from app.model.model import Model_Api
from decimal import Decimal

factory_response = Factory_Response()

with app.app_context():

    class Handler_Request():

        def handle_get_request(self, data:dict, model_query, table_name:str, *property):
            """Метод для получения данных из БД.
            :param data: Исходный словарь, из которого будут извлекаться значения, получается путем "data = request.get_json()".
            :param model_query: Метод, который создает запрос к БД, метод класса Model_Api.
            :param table_name: название таблицы для запроса. С помощью данного параметра происходит проверка типа данных.
            :param property: Список ключей, значения которых нужно извлечь из data.
            :return: Обьект make_response() формат JSON.
            """
            try:
                list_property = list(property)
                # Проверка входных данных на формат json + их наличие (пустоту)
                if data is None or not isinstance(data, dict) or not request.is_json:
                    return factory_response.response_error_request_not_data
                # Проверка входных данных на наличие всех обязательных свойств
                if self.check_exist_request_data_item(data, list_property) == False:
                    return factory_response.get_response_error_request_not_data_item(
                        self.get_string_not_exist_request_data_item(data, list_property))
                # Создание словаря с параметрами для запроса к БД
                dict_prop = self.make_dict_property_from_request(data, list_property)
                # Преобразование float полей в decimal в dict
                dict_prop = self.convert_float_to_decimal_in_dict(dict_prop)
                # Проверка типа входных данных с их типов в БД
                if self.check_corrent_type_request_data_items(dict_prop, table_name) == False:
                    return factory_response.get_response_error_request_uncorrect_type_data_item(
                        self.get_string_not_corrent_type_request_data_item(dict_prop, table_name))

                # Запрос к БД
                response = make_response(model_query(dict_prop), 200)
                response.headers['Content-Type'] = 'application/json; charset=utf-8'
                return response
            except Exception as ex:
                #print(ex.with_traceback())
                return make_response(jsonify({"error": "Неизвестная ошибка"}), 400)

        def handle_delete_request(self, data:dict, model_query, table_name:str, *property):
            """Метод для удаления данных из БД.
            :param data: Исходный словарь, из которого будут извлекаться значения, получается путем "data = request.get_json()".
            :param model_query: Метод, который создает запрос к БД, метод класса Model_Api.
            :param table_name: название таблицы для запроса. С помощью данного параметра происходит проверка типа данных.
            :param property: Список ключей, значения которых нужно извлечь из data.
            :return: Обьект make_response() формат JSON.
            """
            try:
                list_property = list(property)
                # Проверка входных данных на формат json + их наличие (пустоту)
                if data is None or not isinstance(data, dict) or not request.is_json:
                    return factory_response.response_error_request_not_data
                # Проверка входных данных на наличие всех обязательных свойств
                if self.check_exist_request_data_item(data, list_property) == False:
                    return factory_response.get_response_error_request_not_data_item(
                        self.get_string_not_exist_request_data_item(data, list_property))
                # Создание словаря с параметрами для запроса к БД
                dict_prop = self.make_dict_property_from_request(data, list_property)
                # Преобразование float полей в decimal в dict
                dict_prop = self.convert_float_to_decimal_in_dict(dict_prop)
                # Проверка типа входных данных с их типов в БД
                if self.check_corrent_type_request_data_items(dict_prop, table_name) == False:
                    return factory_response.get_response_error_request_uncorrect_type_data_item(
                        self.get_string_not_corrent_type_request_data_item(dict_prop, table_name))

                # Запрос к БД
                response = make_response(model_query(dict_prop), 200)
                response.headers['Content-Type'] = 'application/json; charset=utf-8'
                return response
            except Exception as ex:
                #print(ex.with_traceback())
                return make_response(jsonify({"error": "Неизвестная ошибка"}), 400)

        def handle_update_request(self, data:dict, model_query, table_name:str, *property):
            """Метод для изменения данных в БД.
            :param data: Исходный словарь, из которого будут извлекаться значения, получается путем "data = request.get_json()".
            :param model_query: Метод, который создает запрос к БД, метод класса Model_Api.
            :param property: Список ключей, значения которых нужно извлечь из data.
            :return: Обьект make_response() формат JSON.
            """
            try:
                list_property = list(property)
                # Проверка входных данных на формат json + их наличие (пустоту)
                if data is None or not isinstance(data, dict) or not request.is_json:
                    return factory_response.response_error_request_not_data
                # Проверка входных данных на наличие всех обязательных свойств
                if self.check_exist_request_data_item(data, list_property) == False:
                    return factory_response.get_response_error_request_not_data_item(
                        self.get_string_not_exist_request_data_item(data, list_property))
                # Создание словаря с параметрами для запроса к БД
                dict_prop = self.make_dict_property_from_request(data, list_property)
                # Преобразование float полей в decimal в dict
                dict_prop = self.convert_float_to_decimal_in_dict(dict_prop)
                # Проверка типа входных данных на NULL либо тип в БД
                print('0')
                #if self.check_corrent_type_or_null_request_data_items(dict_prop, table_name) == False:
                #    return factory_response.get_response_error_request_uncorrect_type_data_item(
                #        self.get_string_not_corrent_type_or_null_request_data_item(dict_prop, table_name))

                # Запрос к БД
                response = make_response(model_query(dict_prop), 200)
                response.headers['Content-Type'] = 'application/json; charset=utf-8'
                return response
            except Exception as ex:
                print(ex.with_traceback())
                return make_response(jsonify({"error": "Неизвестная ошибка"}), 400)

        def handle_add_request(self, data:dict, model_query, table_name:str, *property):
            """Метод для создания данных в БД.
            :param data: Исходный словарь, из которого будут извлекаться значения, получается путем "data = request.get_json()".
            :param model_query: Метод, который создает запрос к БД, метод класса Model_Api.
            :param property: Список ключей, значения которых нужно извлечь из data.
            :return: Обьект make_response() формат JSON.
            """
            try:
                list_property = list(property)
                # Проверка входных данных на формат json + их наличие (пустоту)
                if data is None or not isinstance(data, dict) or not request.is_json:
                    return factory_response.response_error_request_not_data
                # Проверка входных данных на наличие всех обязательных свойств
                if self.check_exist_request_data_item(data, list_property) == False:
                    return factory_response.get_response_error_request_not_data_item(
                        self.get_string_not_exist_request_data_item(data, list_property))
                # Создание словаря с параметрами для запроса к БД
                dict_prop = self.make_dict_property_from_request(data, list_property)
                # Преобразование float полей в decimal в dict
                dict_prop = self.convert_float_to_decimal_in_dict(dict_prop)
                # Проверка типа входных данных на NULL либо тип в БД
                if self.check_corrent_type_request_data_items(dict_prop, table_name) == False:
                    return factory_response.get_response_error_request_uncorrect_type_data_item(
                        self.get_string_not_corrent_type_request_data_item(dict_prop, table_name))

                # Запрос к БД
                response = make_response(model_query(dict_prop), 200)
                response.headers['Content-Type'] = 'application/json; charset=utf-8'
                return response
            except Exception as ex:
                print(ex.with_traceback())
                return make_response(jsonify({"error": "Неизвестная ошибка"}), 400)

        def check_exist_request_data_item(self, data:dict, property:list):
            """Проверка входных данных на наличие всех обязательных свойств
                :param data: Исходный словарь, из которого будут извлекаться значения, получается путем "data = request.get_json()".
                :param property: Список ключей, значения которых нужно извлечь из data.
                :return: False, если не хватает хоть одного обязательного поля в :property.
            """
            for item in property:
                if not data.get(item) and data.get(item) != '':
                    return False
            return True

        def check_corrent_type_request_data_items(self, dict_property:dict, table_name:str):
            """ Проверка всех обязательных полей request на тип данных эквивалентный в БД
                :param dict_property: словарь со всеми обязательными полями для запроса
                :param table_name: имя таблицы в БД
                :return Возвращает False если хоть одно поле имеет неверный тип данных
            """
            for key, value in dict_property.items():
                type_column = Model_Api.get_type_table_property(table_name=table_name, column_name=key).lower()
                type_property = type(value).__name__.lower()

                if type_property == 'str' and (type_column == 'varchar' or type_column == 'text'):
                    continue;
                if type_column != type_property:
                    return False
            return True

        def check_corrent_type_or_null_request_data_items(self, dict_property:dict, table_name:str):
            """ Проверка всех обязательных полей request на NULL либо тип данных эквивалентный в БД
                :param dict_property: словарь со всеми обязательными полями для запроса
                :param table_name: имя таблицы в БД
                :return Возвращает False если хоть одно поле имеет неверный тип данных
            """
            primary_key = Model_Api.get_type_table_primary_key(table_name)
            if primary_key[1].lower() != type(dict_property[primary_key[0]]).__name__.lower():
                return False # Если тип данных первичного ключа не сходится

            for key, value in dict_property.items():
                type_column = Model_Api.get_type_table_property(table_name=table_name, column_name=key).lower()
                type_property = type(value).__name__.lower()

                if type_property == 'str' and (type_column == 'varchar' or type_column == 'text'):
                    continue;
                if not type_property or type_column != type_property:
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
                if not data.get(item):
                    list_not_exist.append(item)
            result = ", ".join(map(str, list_not_exist)) + "."

            return result

        def get_string_not_corrent_type_request_data_item(self, dict_property:dict, table_name:str):
            """Возвращает строку всех обязательных полей у которых тип данных не сходится с типов столбца в БД
                :param dict_property: словарь со всеми обязательными полями для запроса
                :param table_name: имя таблицы в БД
                :return: type str
            """
            list_not_corrent_type = []
            for key, value in dict_property.items():
                type_column = Model_Api.get_type_table_property(table_name=table_name, column_name=key).lower()
                type_property = type(value).__name__.lower()

                if type_property == 'str' and (type_column == 'varchar' or type_column == 'text'):
                    continue;
                if type_column != type_property:
                    list_not_corrent_type.append(key)

            result = ", ".join(map(str, list_not_corrent_type)) + "."
            return result

        def get_string_not_corrent_type_or_null_request_data_item(self, dict_property:dict, table_name:str):
            """Возвращает строку всех обязательных полей у которых тип данных либо NULL, либо не сходится с типов столбца в БД
                :param dict_property: словарь со всеми обязательными полями для запроса
                :param table_name: имя таблицы в БД
                :return: type str
            """
            list_not_corrent_type = []
            primary_key = Model_Api.get_type_table_primary_key(table_name)

            if primary_key[1].lower() != type(dict_property[primary_key[0]]).__name__.lower():
                list_not_corrent_type.append(primary_key[0]) # Если тип данных первичного ключа не сходится

            for key, value in dict_property.items():
                # Если не валиден тип данных первичного ключа,
                #чтобы дважды его не добавлять в result строку
                if primary_key[0] == key:
                    continue

                type_column = Model_Api.get_type_table_property(table_name=table_name, column_name=key).lower()
                type_property = type(value).__name__.lower()

                if type_property == 'str' and (type_column == 'varchar' or type_column == 'text'):
                    continue;
                if not type_property or type_column != type_property:
                    list_not_corrent_type.append(key)

            result = ", ".join(map(str, list_not_corrent_type)) + "."
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

        def convert_float_to_decimal_in_dict(self, param_dict:dict):
            # Преобразование только float в Decimal
            return {
                key: (Decimal(value) if isinstance(value, float) else value)
                for key, value in param_dict.items()
            }

        def handle_get_system_info_request(self):
            import platform
            import os
            import psutil
            import socket
            from datetime import datetime

            process = psutil.Process(os.getpid())  # Информация о текущем процессе
            boot_time = datetime.fromtimestamp(psutil.boot_time())  # Время загрузки системы

            result = {
                "boot_time": boot_time.strftime("%Y-%m-%d %H:%M:%S"),
                "process": {
                    "pid": process.pid,
                    "name": process.name(),
                    "status": process.status(),
                    "memory_info": {
                        "rss": f"{round(process.memory_info().rss / (1024**2), 2)} MB",
                        "vms": f"{round(process.memory_info().vms / (1024**2), 2)} MB"
                    },
                    "cpu_times": {
                        "user": f"{process.cpu_times().user:.2f} sec",
                        "system": f"{process.cpu_times().system:.2f} sec"
                    }
                },
                "cpu": {
                    "processor": platform.processor(),
                    "cpu_count_logical": psutil.cpu_count(logical=True),
                    "cpu_count_physical": psutil.cpu_count(logical=False),
                    "cpu_frequency": f"{psutil.cpu_freq().max:.2f} MHz",
                    "cpu_usage": f"{psutil.cpu_percent(interval=1)}%"
                },
                "memory": {
                    "total": f"{round(psutil.virtual_memory().total / (1024**2), 2)} MB",
                    "available": f"{round(psutil.virtual_memory().available / (1024**2), 2)} MB",
                    "used": f"{round(psutil.virtual_memory().used / (1024**2), 2)} MB",
                    "percent_used": f"{psutil.virtual_memory().percent}%"
                },
                "os": {
                    "name": platform.system(),
                    "version": platform.version(),
                    "release": platform.release(),
                    "architecture": platform.architecture()[0]
                },
                "disk": {
                    "total": f"{round(psutil.disk_usage('/').total / (1024**2), 2)} MB",
                    "used": f"{round(psutil.disk_usage('/').used / (1024**2), 2)} MB",
                    "free": f"{round(psutil.disk_usage('/').free / (1024**2), 2)} MB",
                    "percent_used": f"{psutil.disk_usage('/').percent}%"
                },
                "network": {
                    "hostname": socket.gethostname(),
                    "ip_address": socket.gethostbyname(socket.gethostname()),
                }
            }

            return make_response(jsonify(result), 200)
