from mysql.connector import *


def buka_koneksi():
    db = None
    try:
        db = connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="universitas"
        )
    except DatabaseError as e:
        print("Koneksi gagal:", e)
    return db