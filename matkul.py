from mysql.connector import *
from koneksi import buka_koneksi


class Matkul:
    kd_matkul: str
    nm_matkul: str
    sks: int

    def simpan(self):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = f"insert into matkul values ('{self.kd_matkul}', '{self.nm_matkul}', {self.sks})"
                cursor.execute(sql)
                cn.commit()
            print("Data berhasil disimpan")
        except IntegrityError as e:
            print(f"Data gagal disimpan: {e}")

    def ubah(self, kd_matkul):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = (f"update matkul set nm_matkul = '{self.nm_matkul}', sks = '{self.sks}' "
                       f"where kd_matkul = '{kd_matkul}'")
                cursor.execute(sql)
                cn.commit()
            print(f"Data [{kd_matkul}] berhasil diubah")
        except IntegrityError as e:
            print(f"Data [{kd_matkul}] gagal diubah: {e}")

    def hapus(self, kd_matkul):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = f"delete from matkul where kd_matkul = '{kd_matkul}'"
                cursor.execute(sql)
                cn.commit()
            print(f"Data [{kd_matkul}] berhasil dihapus")
        except IntegrityError as e:
            print(f"Data [{kd_matkul}] gagal dihapus: {e}")

    def tampil(self):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = "select * from matkul order by kd_matkul asc"
                cursor.execute(sql)
                data = cursor.fetchall()
                print("DATA MATA KULIAH")
                for baris in data:
                    print("-" * 40)
                    print(f"Kode mata kuliah: {baris[0]}")
                    print(f"Nama mata kuliah: {baris[1]}")
                    print(f"SKS: {baris[2]}")
        except IntegrityError as e:
            print(f"Data gagal ditampilkan: {e}")

    def tampil_detail(self, kd_matkul):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = f"select * from matkul where kd_matkul = '{kd_matkul}'"
                cursor.execute(sql)
                data = cursor.fetchone()
                return {"nama": data[1], "sks": data[2]} if data is not None else {}
        except IntegrityError as e:
            print(f"Data mata kuliah [{kd_matkul}] gagal ditampilkan: {e}")