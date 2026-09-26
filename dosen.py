from mysql.connector import *
from koneksi import buka_koneksi


class Dosen:
    nidn: str
    gelar_depan: str
    nm_dosen: str
    gelar_belakang: str

    def simpan_dos(self):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = (
                    f"insert into dosen values "
                    f"('{self.nidn}', '{self.gelar_depan}', "
                    f"'{self.nm_dosen}', '{self.gelar_belakang}')"
                )
                cursor.execute(sql)
                cn.commit()
            print("Data berhasil disimpan")
        except IntegrityError as e:
            print(f"Data gagal disimpan: {e}")

    def ubah_dos(self, nidn):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = (
                    f"update dosen set "
                    f"gelar_depan = '{self.gelar_depan}', "
                    f"nm_dosen = '{self.nm_dosen}', "
                    f"gelar_belakang = '{self.gelar_belakang}' "
                    f"where nidn = '{nidn}'"
                )
                cursor.execute(sql)
                cn.commit()
            print(f"Data [{nidn}] berhasil diubah")
        except IntegrityError as e:
            print(f"Data [{nidn}] gagal diubah: {e}")

    def hapus_dos(self, nidn):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = f"delete from dosen where nidn = '{nidn}'"
                cursor.execute(sql)
                cn.commit()
            print(f"Data [{nidn}] berhasil dihapus")
        except IntegrityError as e:
            print(f"Data [{nidn}] gagal dihapus: {e}")

    def tampil_dos(self):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = "select * from dosen order by nidn asc"
                cursor.execute(sql)
                data = cursor.fetchall()

                print("DATA DOSEN")
                for baris in data:
                    print("-" * 40)
                    print(f"NIDN            : {baris[0]}")
                    print(f"Gelar Depan     : {baris[1]}")
                    print(f"Nama Dosen      : {baris[2]}")
                    print(f"Gelar Belakang  : {baris[3]}")
        except IntegrityError as e:
            print(f"Data gagal ditampilkan: {e}")

    def ambil_data_dos(self, nidn):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = f"select * from dosen where nidn = '{nidn}'"
                cursor.execute(sql)
                data = cursor.fetchone()

                return (
                    {
                        "nama": data[2],
                        "gelar_depan": data[1],
                        "gelar_belakang": data[3],
                    }
                    if data is not None
                    else {}
                )
        except IntegrityError as e:
            print(f"Data dosen [{nidn}] gagal ditampilkan: {e}")