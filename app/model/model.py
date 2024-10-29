from sqlalchemy import create_engine, text
from .engine import connection

class Model_Api():

    def __init__(self):
        pass

    # GET
    def get_family(self, property:dict):
        response = connection.execute(text("SELECT get_family(:id)"), property)
        return response.fetchall()[0][0]

    def get_gender(self, property:dict):
        response = connection.execute(text("SELECT get_gender(:id)"), property)
        return response.fetchall()[0][0]

    def get_operation_type(self, property:dict):
        response = connection.execute(text("SELECT get_operation_type(:id)"), property)
        return response.fetchall()[0][0]

    def get_secret_key_person(self, property:dict):
        response = connection.execute(text("SELECT get_secret_key_person(:id)"), property)
        return response.fetchall()[0][0]

    # ADD
    def add_gender(self, property:dict):
        response = connection.execute(text("SELECT add_gender(:id)"), property)
        return response.fetchall()[0][0]

    def add_operation_type(self, property:dict):
        response = connection.execute(text("SELECT get_operation_type(:id)"), property)
        return response.fetchall()[0][0]

    def add_secret_key_person(self, property:dict):
        response = connection.execute(text("SELECT get_secret_key_person(:id)"), property)
        return response.fetchall()[0][0]

    # UPDATE
    def update_family(self, property:dict):
        response = connection.execute(text("SELECT update_family(:id, :balance, :address)"), property)
        return response.fetchall()[0][0]

    def update_family_balance(self, property:dict):
        response = connection.execute(text("SELECT update_family_balance(:id, :balance)"), property)
        return response.fetchall()[0][0]

    def update_family_address(self, property:dict):
        response = connection.execute(text("SELECT update_family_address(:id, :address)"), property)
        return response.fetchall()[0][0]

    def update_gender(self, property:dict):
        response = connection.execute(text("SELECT update_gender(:id, :name)"), property)
        return response.fetchall()[0][0]

    def update_orepation_type(self, property:dict):
        response = connection.execute(text("SELECT update_orepation_type(:id, :value)"), property)
        return response.fetchall()[0][0]

    def update_secret_key_person(self, property:dict):
        response = connection.execute(text("SELECT update_secret_key_person(:id, :value)"), property)
        return response.fetchall()[0][0]

    # DELETE
    def delete_family(self, property:dict):
        response = connection.execute(text("SELECT delete_family(:id)"), property)
        return response.fetchall()[0][0]

    def delete_gender(self, property:dict):
        response = connection.execute(text("SELECT delete_gender(:id)"), property)
        return response.fetchall()[0][0]

    def delete_orepation_type(self, property:dict):
        response = connection.execute(text("SELECT delete_orepation_type(:id)"), property)
        return response.fetchall()[0][0]

    def delete_secret_key_person(self, property:dict):
        response = connection.execute(text("SELECT delete_secret_key_person(:id)"), property)
        return response.fetchall()[0][0]

    @staticmethod
    def get_type_table_property(table_name:str, column_name:str):
        """Возвращает тип данных столбца таблицы как строку
        """
        response = connection.execute(text(
            """SELECT DATA_TYPE
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_NAME = :table_name
                AND COLUMN_NAME = :column_name;"""), {'table_name': table_name, 'column_name': column_name}).fetchone()
        return str(response[0]) if response else None

    @staticmethod
    def get_type_table_primary_key(table_name:str):
        """Возвращает кортеж - (имя первичного ключа, его тип в строке)
        """
        response = connection.execute(text(
            """SELECT COLUMN_NAME, DATA_TYPE
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_NAME = :table_name
                AND COLUMN_NAME IN (
                    SELECT COLUMN_NAME
                    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
                    WHERE TABLE_NAME = :table_name
                    AND CONSTRAINT_NAME = 'PRIMARY'
                );"""), {'table_name': table_name}).fetchall()[0]
        return response if response else None
