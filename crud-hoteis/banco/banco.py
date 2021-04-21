import pymongo
import pandas as pd

pd.set_option("display.max_columns", None)


class Banco:

    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb://localhost:27017/")
        self.hoteis = self.conn.crudhoteis_db.hotel

    def insert_hotel(self, hotel: dict):
        self.hoteis.insert_one(hotel)

    def get_all(self) -> list:
        # cursor = self.hoteis.find()
        cursor = self.hoteis.find()
        return list(cursor)

    def remove_hotel(self, nome):
        self.hoteis.delete_one({"nome": nome})

    def update_hotel(self, filtro, **args):
        self.hoteis.update_one({"nome": filtro}, {"$set": args})
