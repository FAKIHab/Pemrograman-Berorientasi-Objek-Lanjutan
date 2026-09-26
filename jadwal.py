from mysql.connector import *
from koneksi import buka_koneksi


class Jadwal:
    kd_jadwal: str
    semester: str
    thn_akademik: int
    nidn: str
    kd_matkul: str
    kelompok: str
    hari: str
    jam_mulai: str
    jam_selesai: str
    ruang: str

    def simpan_jadwal_dos(self):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = (
                    f"insert into jadwal "
                    f"(semester, thn_akademik, nidn, kd_matkul, kelompok, hari, "
                    f"jam_mulai, jam_selesai, ruang) "
                    f"values ('{self.semester}', {int(self.thn_akademik)}, "
                    f"'{self.nidn}', '{self.kd_matkul}', '{self.kelompok}', "
                    f"'{self.hari}', '{self.jam_mulai}', "
                    f"'{self.jam_selesai}', '{self.ruang}')"
                )
                cursor.execute(sql)
                cn.commit()
            print("Data Jadwal Dosen berhasil disimpan")
        except IntegrityError as e:
            print(f"Data Jadwal Dosen gagal disimpan: {e}")

    def ubah_jadwal_dos(self, kd_jadwal):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = (
                    f"update jadwal set "
                    f"semester='{self.semester}', "
                    f"thn_akademik={int(self.thn_akademik)}, "
                    f"hari='{self.hari}', "
                    f"jam_mulai='{self.jam_mulai}', "
                    f"jam_selesai='{self.jam_selesai}', "
                    f"ruang='{self.ruang}', "
                    f"kelompok='{self.kelompok}' "
                    f"where kd_jadwal='{kd_jadwal}'"
                )
                cursor.execute(sql)
                cn.commit()
            print(f"Data [{kd_jadwal}] berhasil diubah")
        except IntegrityError as e:
            print(f"Data [{kd_jadwal}] gagal diubah: {e}")

    def hapus_jadwal_dos(self, kd_jadwal):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = f"delete from jadwal where kd_jadwal = '{kd_jadwal}'"
                cursor.execute(sql)
                cn.commit()
            print(f"Data [{kd_jadwal}] berhasil dihapus")
        except IntegrityError as e:
            print(f"Data [{kd_jadwal}] gagal dihapus: {e}")

    def tampil_jadwal_dos(self):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = (
                    "select j.*, d.nm_dosen, m.nm_matkul from jadwal j "
                    "join dosen d on j.nidn = d.nidn "
                    "join matkul m on j.kd_matkul = m.kd_matkul "
                    "order by field(j.hari, 'Senin', 'Selasa', 'Rabu', "
                    "'Kamis', 'Jumat', 'Sabtu'), j.jam_mulai asc"
                )
                cursor.execute(sql)
                data = cursor.fetchall()

                print("DATA JADWAL DOSEN")
                for baris in data:
                    print("-" * 50)
                    print(f"Kode Jadwal : {baris[0]}")
                    print(f"Semester    : {baris[1]} {baris[2]}")
                    print(f"Dosen       : {baris[10]}")
                    print(f"Mata Kuliah : {baris[11]}")
                    print(f"Hari/Jam    : {baris[6]}, {baris[7]} - {baris[8]}")
                    print(f"Ruang       : {baris[9]} | Kelompok: {baris[5]}")
        except IntegrityError as e:
            print(f"Data gagal ditampilkan: {e}")

    def ambil_data_jadwal_dos(self, nidn):
        try:
            with buka_koneksi() as cn:
                cursor = cn.cursor()
                sql = (
                    "select j.*, d.nm_dosen, m.nm_matkul, m.sks from jadwal j "
                    "join dosen d on j.nidn = d.nidn "
                    "join matkul m on j.kd_matkul = m.kd_matkul "
                    f"where j.nidn = '{nidn}'"
                )
                cursor.execute(sql)
                data = cursor.fetchone()

                if data is not None:
                    return {
                        "kd_jadwal": data[0],
                        "nidn": data[3],
                        "nm_dosen": data[10],
                        "kd_matkul": data[4],
                        "nm_matkul": data[11],
                        "sks": data[12],
                        "kelompok": data[5],
                        "hari": data[6],
                        "jam_mulai": str(data[7]),
                        "jam_selesai": str(data[8]),
                        "ruang": data[9],
                    }
                else:
                    return {}
        except IntegrityError as e:
            print(f"Data jadwal untuk NIDN [{nidn}] gagal ditampilkan: {e}")
            return {}