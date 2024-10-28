from sqlalchemy import create_engine, text
from .engine import connection

class Model_Api():

    def __init__(self):
        pass

    def get_family(self, property:dict):
        response = connection.execute(text("SELECT get_family(:family_id)"), property)
        print(property)
        return response.fetchall()[0][0]

    def update_family_balance(self, property:dict):
        response = connection.execute(text("SELECT update_family_balance(:family_id, :balance)"), property)
        return response.fetchall()[0][0]

    def update_family_address(self, property:dict):
        response = connection.execute(text("SELECT update_family_address(:family_id, :address)"), property)
        return response.fetchall()[0][0]

    @staticmethod
    def get_type_table_property(table_name:str, column_name:str):
        response = connection.execute(text(
            """SELECT DATA_TYPE
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_NAME = :table_name
                AND COLUMN_NAME = :column_name;"""), {'table_name': table_name, 'column_name': column_name}).fetchone()
        return str(response[0]) if response else None