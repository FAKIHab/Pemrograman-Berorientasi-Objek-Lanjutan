from mysql.connector import *
from koneksi import buka_koneksi


class KRS:
    nim: str
    kd_matkul: str
    semester: str
    thn_akademik: int

    def simpan_krs(self):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = (f"insert into ambil values ('{self.nim}', '{self.kd_matkul}', '{self.semester}', "
                       f"'{self.thn_akademik}', '0', '0', '0', '0')")
                cursor.execute(sql)
                cn.commit()
            print("Data KRS berhasil disimpan")
        except IntegrityError as e:
            print(f"Data KRS gagal disimpan: {e}")

    def ubah_krs(self, nim, kd_matkul):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = (f"update ambil set semester = '{self.semester}', thn_akademik = '{self.thn_akademik}' "
                       f"where nim = '{nim}' and kd_matkul = '{kd_matkul}'")
                cursor.execute(sql)
                cn.commit()
            print(f"Data KRS [{nim} - {kd_matkul}] berhasil diubah")
        except IntegrityError as e:
            print(f"Data KRS [{nim} - {kd_matkul}] gagal diubah: {e}")