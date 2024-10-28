from sqlalchemy import create_engine, text
from .engine import connection

class Model_Api():

    def __init__(self):
        pass

    def get_family(self, family_id):
        resp = connection.execute(text("SELECT family_get(:family_id)"), {"family_id": family_id})
        return resp.fetchall()[0][0]

    def update_family_balance(self, family_id, balance):
        resp = connection.execute(text("SELECT family_balance_update(:family_id, :balance)"), {"family_id": family_id, "balance": balance})
        return resp.fetchall()[0][0]

    def update_family_address(self, family_id, address):
        resp = connection.execute(text("SELECT family_address_update(:family_id, :address)"), {"family_id": family_id, "address": address})
        return resp.fetchall()[0][0]