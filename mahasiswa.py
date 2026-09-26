from mysql.connector import *
from koneksi import buka_koneksi


class Mahasiswa:
    nim: str
    nm_mahasiswa: str
    
    def simpan(self):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = f"insert into mahasiswa values ('{self.nim}','{self.nm_mahasiswa}')"
                cursor.execute(sql)
                cn.commit()
                print("Data berhasil disimpan")
        except IntegrityError as e:
            print("Data gagal disimpan: {e}")
    def ubah(self, nim):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = f"update mahasiswa set nm_mahasiswa = '{self.nm_mahasiswa}' where nim = '{nim}'"
                cursor.execute(sql)
                cn.commit()
                print(f"Data [{nim}] berhasil diubah:")
        except IntegrityError as e:
            print(f"Data[{nim}] gagal diubah: {e}")

    def hapus(self, nim):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql= f"delete from mahasiswa where nim  = '{nim}'"
                cursor.execute(sql)
                cn.commit()
                print(f"Data [{nim}] berhasil dihapus")
        except IntegrityError as e:
            print(f"Data [{nim}] gagal dihapus: {e}")

    def tampil(self):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql= "select * from mahasiswa order by nim asc"
                cursor.execute(sql)
                data = cursor.fetchall()
                print("DATA MAHASISWA")
                for baris in data:
                    print("---------------------------")
                    print(f"NIM: {baris[0]}")
                    print(f"Nama mahasiswa: {baris[1]}")
        except IntegrityError as e:
            print(f"Data gagal ditampilkan: {e}")

    def ambil_data(self, nim):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = f"select * from mahasiswa where nim = '{nim}'"
                cursor.execute(sql)
                data = cursor.fetchone()
                return {"nama": data[1]} if data is not None else {}
        except IntegrityError as e:
            print(f"Data mahasiswa [{nim}] gagal ditampilkan: {e}")