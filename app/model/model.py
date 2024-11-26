from sqlalchemy import text
from .engine import connection

class Model_Api():

    def __init__(self):
        pass

    # GET
    def get_family(self, property:dict):
        response = connection.execute(text("SELECT get_family(:id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def get_gender(self, property:dict):
        response = connection.execute(text("SELECT get_gender(:id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def get_operation_type(self, property:dict):
        response = connection.execute(text("SELECT get_operation_type(:id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def get_operation(self, property:dict):
        response = connection.execute(text("SELECT get_operation(:id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def get_secret_key_person(self, property:dict):
        response = connection.execute(text("SELECT get_secret_key_person(:id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def get_account_status(self, property:dict):
        response = connection.execute(text("SELECT get_account_status(:id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def get_category_operation(self, property:dict):
        response = connection.execute(text("SELECT get_category_operation(:id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def get_person(self, property:dict):
        response = connection.execute(text("SELECT get_person(:id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def get_person_by_family_id(self, property:dict):
        response = connection.execute(text("SELECT get_person_by_family_id(:family_id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def get_person_account(self, property:dict):
        response = connection.execute(text("SELECT get_person_account(:id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def get_person_goal(self, property:dict):
        response = connection.execute(text("SELECT get_person_goal(:id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def get_registration(self, property:dict):
        response = connection.execute(text("SELECT get_registration(:login, :password)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    # ADD
    def add_gender(self, property:dict):
        response = connection.execute(text("SELECT add_gender(:name)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def add_operation_type(self, property:dict):
        response = connection.execute(text("SELECT add_operation_type(:value)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def add_operation(self, property:dict):
        response = connection.execute(text("SELECT add_operation(:name, :comment, :operation_type_id, :operation_category_id, :person_account_id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def add_person(self, property:dict):
        response = connection.execute(text("SELECT add_person(:name, :lastname, :surname, :age, :phone, :gender_id, :family_id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def add_person_account(self, property:dict):
        response = connection.execute(text("SELECT add_person_account(:person_id, :status_id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def add_person_goal(self, property:dict):
        response = connection.execute(text("SELECT add_person_goal(:person_id, :name, :comment, :sum_total)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def add_secret_key_person(self, property:dict):
        response = connection.execute(text("SELECT add_secret_key_person(:value)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def add_account_status(self, property:dict):
        response = connection.execute(text("SELECT add_account_status(:name)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def add_category_operation(self, property:dict):
        response = connection.execute(text("SELECT add_category_operation(:name, :person_id, :for_family_id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def add_registration(self, property:dict):
        response = connection.execute(text("SELECT add_registration(:login, :password, :email)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    # UPDATE
    def update_family(self, property:dict):
        response = connection.execute(text("SELECT update_family(:id, :balance, :address)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def update_family_balance(self, property:dict):
        response = connection.execute(text("SELECT update_family_balance(:id, :balance)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def update_family_address(self, property:dict):
        response = connection.execute(text("SELECT update_family_address(:id, :address)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def update_gender(self, property:dict):
        response = connection.execute(text("SELECT update_gender(:id, :name)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def update_person(self, property:dict):
        response = connection.execute(text("SELECT update_person(:id, :name, :lastname, :surname, :age, :phone, :family_id, :gender_id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def update_operation_type(self, property:dict):
        response = connection.execute(text("SELECT update_operation_type(:id, :value)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def update_operation(self, property:dict):
        response = connection.execute(text("SELECT update_operation(:id, :name, :comment, :operation_category_id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def update_operation_category(self, property:dict):
        response = connection.execute(text("SELECT update_operation_category(:id, :operation_category_id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def update_operation_comment(self, property:dict):
        response = connection.execute(text("SELECT update_operation_comment(:id, :comment)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def update_operation_name(self, property:dict):
        response = connection.execute(text("SELECT update_operation_name(:id, :name)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def update_secret_key_person(self, property:dict):
        response = connection.execute(text("SELECT update_secret_key_person(:id, :value)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def update_account_status(self, property:dict):
        response = connection.execute(text("SELECT update_account_status(:id, :name)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def update_category_operation(self, property:dict):
        response = connection.execute(text("SELECT update_category_operation(:id, :name, :person_id, :for_family_id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    # DELETE
    def delete_family(self, property:dict):
        response = connection.execute(text("SELECT delete_family(:id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def delete_gender(self, property:dict):
        response = connection.execute(text("SELECT delete_gender(:id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def delete_operation_type(self, property:dict):
        response = connection.execute(text("SELECT delete_operation_type(:id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def delete_operation(self, property:dict):
        response = connection.execute(text("SELECT delete_operation(:id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def delete_secret_key_person(self, property:dict):
        response = connection.execute(text("SELECT delete_secret_key_person(:id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def delete_account_status(self, property:dict):
        response = connection.execute(text("SELECT delete_account_status(:id)"), property)
        connection.commit()
        return response.fetchall()[0][0]

    def delete_category_operation(self, property:dict):
        response = connection.execute(text("SELECT delete_category_operation(:id)"), property)
        connection.commit()
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
