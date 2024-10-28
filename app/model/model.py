from sqlalchemy import create_engine, text
from .engine import connection

class Model_Api():

    def __init__(self):
        pass

    def get_family(self, property:dict):
        resp = connection.execute(text("SELECT family_get(:family_id)"), property)
        return resp.fetchall()[0][0]

    def update_family_balance(self, property:dict):
        resp = connection.execute(text("SELECT family_balance_update(:family_id, :balance)"), property)
        return resp.fetchall()[0][0]

    def update_family_address(self, property:dict):
        resp = connection.execute(text("SELECT family_address_update(:family_id, :address)"), property)
        return resp.fetchall()[0][0]