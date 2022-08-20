from typing import Collection
import pymongo
import uuid

client = pymongo.MongoClient("mongodb+srv://projectZero:8566423@cluster0.c0gm834.mongodb.net/?retryWrites=true&w=majority")
db = client.databes
collection = db.lokasi

def test(kecepatan,latitude,longitude,timestamp):
    data = {
        "ID transaksi": str(uuid.uuid4()),
        "kecepatan": kecepatan,
        "latitude": latitude,
        "longitude": longitude,
        "timestamp": timestamp
    }
    records = collection.insert_one(data)
    print("data tersimpan",records)