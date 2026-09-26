from mysql.connector import *
from koneksi import buka_koneksi


class Nilai:
    presensi: int
    tugas: int
    uts: int
    uas: int

    def update_khs(self, nim, kd_matkul):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = (f"update ambil set presensi = '{self.presensi}', tugas = '{self.tugas}', uts = {self.uts}, "
                       f"uas = {self.uas} where nim = '{nim}' and kd_matkul = '{kd_matkul}'")
                cursor.execute(sql)
                cn.commit()
            print("Data nilai berhasil disimpan")
        except IntegrityError as e:
            print(f"Data nilai gagal disimpan: {e}")