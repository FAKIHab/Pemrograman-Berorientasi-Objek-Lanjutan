from koneksi import buka_koneksi
from mahasiswa import Mahasiswa
from matkul import Matkul
from krs import KRS
from nilai import Nilai
from dosen import Dosen
from jadwal import Jadwal
from pyreportjasper import PyReportJasper
from os.path import abspath, dirname, join
from os import startfile


koneksi = buka_koneksi()
if koneksi is not None:
    print("Koneksi Berhasil")
else:
    exit()

while True:
    print("===============================")
    print("       ISB ATMA LUHUR          ")
    print("===============================")
    print("[1] Master")
    print("[2] Transaksi")
    print("[3] Laporan")
    print("[4] Keluar")

    try:
        pilihan = int(input("Masukkan Pilihan Anda (1-4): "))
    except ValueError:
        print("Input harus berupa angka!")
        continue
    print()

    match pilihan:
        case 1:
            while True:
                print("[1.1] Mahasiswa")
                print("[1.2] Mata Kuliah")
                print("[1.3] Dosen")
                print("[1.4] Kembali")
                try:
                    pilih2 = int(input("Masukkan pilihan Anda (1-4): "))
                except ValueError:
                    print("Input harus berupa angka!")
                    continue
                print()

                match pilih2:
                    case 1:
                        while True:
                            print("[1.1.1] Tambah Mahasiswa")
                            print("[1.1.2] Ubah Data Mahasiswa")
                            print("[1.1.3] Hapus Data Mahasiswa")
                            print("[1.1.4] Tampil Daftar Mahasiswa")
                            print("[1.1.5] Kembali")
                            try:
                                pilih3 = int(input("Masukkan pilihan Anda (1-5): "))
                            except ValueError:
                                print("Input harus berupa angka!")
                                continue
                            print()
                            mhs = Mahasiswa()

                            match pilih3:
                                case 1:
                                    mhs.nim = input("NIM: ")
                                    mhs.nm_mahasiswa = input("Nama mahasiswa: ")
                                    mhs.simpan()
                                case 2:
                                    while True:
                                        nim = input("NIM: ")
                                        data = mhs.ambil_data(nim)
                                        if len(data) > 0:
                                            mhs.nm_mahasiswa = input(f"Nama mahasiswa: {data['nama']} -> ")
                                            mhs.ubah(nim)
                                            break
                                        else:
                                            print(f"Data mahasiswa dengan NIM [{nim}] tidak ditemukan")
                                            ulang = input("Tekan R jika ingin mencoba lagi: ").upper() == 'R'
                                            if not ulang:
                                                break
                                case 3:
                                    while True:
                                        nim = input("NIM: ")
                                        data = mhs.ambil_data(nim)
                                        if len(data) > 0:
                                            mhs.hapus(nim)
                                            break
                                        else:
                                            print(f"Data mahasiswa dengan NIM [{nim}] tidak ditemukan")
                                            ulang = input("Tekan R jika ingin mencoba lagi: ").upper() == 'R'
                                            if not ulang:
                                                break
                                case 4:
                                    mhs.tampil()
                                case 5:
                                    break
                                case _:
                                    print("Pilihan salah!")
                            print()

                    case 2:
                        while True:
                            print("[1.2.1] Tambah Mata Kuliah")
                            print("[1.2.2] Ubah Data Mata Kuliah")
                            print("[1.2.3] Hapus Data Mata Kuliah")
                            print("[1.2.4] Tampil Daftar Mata Kuliah")
                            print("[1.2.5] Kembali")
                            try:
                                pilih3 = int(input("Masukkan pilihan Anda (1-5): "))
                            except ValueError:
                                print("Input harus berupa angka!")
                                continue
                            print()
                            mk = Matkul()

                            match pilih3:
                                case 1:
                                    mk.kd_matkul = input("Kode mata kuliah: ")
                                    mk.nm_matkul = input("Nama mata kuliah: ")
                                    while True:
                                        mk.sks = int(input("SKS (2-4): "))
                                        if 2 <= mk.sks <= 4:
                                            break
                                        print("SKS mata kuliah salah!")
                                    mk.simpan()
                                case 2:
                                    while True:
                                        kd_matkul = input("Kode mata kuliah: ")
                                        data = mk.tampil_detail(kd_matkul)
                                        if len(data) > 0:
                                            mk.nm_matkul = input(f"Nama mata kuliah: {data['nama']} -> ")
                                            while True:
                                                mk.sks = int(input(f"SKS (2-4): {data['sks']} -> "))
                                                if 2 <= mk.sks <= 4:
                                                    break
                                                print("SKS mata kuliah salah!")
                                            mk.ubah(kd_matkul)
                                            break
                                        else:
                                            print(f"Data mata kuliah dengan kode [{kd_matkul}] tidak ditemukan")
                                            ulang = input("Tekan R jika ingin mencoba lagi: ").upper() == 'R'
                                            if not ulang:
                                                break
                                case 3:
                                    while True:
                                        kd_matkul = input("Kode mata kuliah: ")
                                        data = mk.tampil_detail(kd_matkul)
                                        if len(data) > 0:
                                            mk.hapus(kd_matkul)
                                            break
                                        else:
                                            print(f"Data mata kuliah dengan kode [{kd_matkul}] tidak ditemukan")
                                            ulang = input("Tekan R jika ingin mencoba lagi: ").upper() == 'R'
                                            if not ulang:
                                                break
                                case 4:
                                    mk.tampil()
                                case 5:
                                    break
                                case _:
                                    print("Pilihan salah!")
                            print()

                    case 3:
                        while True:
                            print("[1.3.1] Tambah Dosen")
                            print("[1.3.2] Ubah Data Dosen")
                            print("[1.3.3] Hapus Data Dosen")
                            print("[1.3.4] Tampil Daftar Dosen")
                            print("[1.3.5] Kembali")
                            try:
                                pilih3 = int(input("Masukkan pilihan Anda (1-5): "))
                            except ValueError:
                                print("Input harus berupa angka!")
                                continue
                            print()
                            dos = Dosen()

                            match pilih3:
                                case 1:
                                    dos.nidn = input("NIDN: ")
                                    dos.gelar_depan = input("Gelar Depan: ")
                                    dos.nm_dosen = input("Nama Dosen: ")
                                    dos.gelar_belakang = input("Gelar Belakang: ")
                                    dos.simpan_dos()
                                case 2:
                                    while True:
                                        nidn = input("NIDN: ")
                                        data = dos.ambil_data_dos(nidn)
                                        if len(data) > 0:
                                            dos.gelar_depan = input(f"Gelar Depan: {data['gelar_depan']} -> ")
                                            dos.nm_dosen = input(f"Nama Dosen: {data['nama']} -> ")
                                            dos.gelar_belakang = input(f"Gelar Belakang: {data['gelar_belakang']} -> ")
                                            dos.ubah_dos(nidn)
                                            break
                                        else:
                                            print(f"Data dosen dengan NIDN [{nidn}] tidak ditemukan")
                                            ulang = input("Tekan R jika ingin mencoba lagi: ").upper() == 'R'
                                            if not ulang:
                                                break
                                case 3:
                                    while True:
                                        nidn = input("NIDN: ")
                                        data = dos.ambil_data_dos(nidn)
                                        if len(data) > 0:
                                            dos.hapus_dos(nidn)
                                            break
                                        else:
                                            print(f"Data dosen dengan NIDN [{nidn}] tidak ditemukan")
                                            ulang = input("Tekan R jika ingin mencoba lagi: ").upper() == 'R'
                                            if not ulang:
                                                break
                                case 4:
                                    dos.tampil_dos()
                                case 5:
                                    break
                                case _:
                                    print("Pilihan salah!")
                            print()

                    case 4:
                        break
                    case _:
                        print("Pilihan salah!")

        case 2:
            while True:
                print("[2.1] Entri KRS")
                print("[2.2] Update KRS")
                print("[2.3] Entri Nilai")
                print("[2.4] Entri Jadwal")
                print("[2.5] Update Jadwal")
                print("[2.6] Kembali")
                try:
                    pilih2 = int(input("Masukkan pilihan Anda (1-6): "))
                except ValueError:
                    print("Input harus berupa angka!")
                    continue
                print()

                mhs = Mahasiswa()
                mk = Matkul()
                kr = KRS()
                nil = Nilai()
                jdD = Jadwal()
                dos = Dosen()
                berhasil = False

                match pilih2:
                    case 1:
                        while True:
                            kr.nim = input("NIM: ")
                            data = mhs.ambil_data(kr.nim)
                            if len(data) > 0:
                                print(f"Nama mahasiswa: {data['nama']}")
                                while True:
                                    kr.kd_matkul = input("Kode mata kuliah: ")
                                    data = mk.tampil_detail(kr.kd_matkul)
                                    if len(data) > 0:
                                        print(f"Nama mata kuliah: {data['nama']}")
                                        print(f"SKS: {data['sks']}")
                                        while True:
                                            smt = input("Semester ([O] Ganjil/[E] Genap): ")
                                            match smt.upper():
                                                case 'O':
                                                    kr.semester = "Gasal"
                                                    break
                                                case 'E':
                                                    kr.semester = "Genap"
                                                    break
                                                case _:
                                                    print("Pilihan salah!")
                                        kr.thn_akademik = int(input("Tahun akademik (tahun semester gasal saja): "))
                                        kr.simpan_krs()
                                        berhasil = True
                                        break
                                    else:
                                        print(f"Data mata kuliah dengan kode [{kr.kd_matkul}] tidak ditemukan")
                            else:
                                print(f"Data mahasiswa dengan NIM [{kr.nim}] tidak ditemukan")
                            if berhasil:
                                print()
                                break

                    case 2:
                        while True:
                            nim = input("NIM: ")
                            data = mhs.ambil_data(nim)
                            if len(data) > 0:
                                print(f"Nama mahasiswa: {data['nama']}")
                                while True:
                                    kd_matkul = input("Kode mata kuliah: ")
                                    data = mk.tampil_detail(kd_matkul)
                                    if len(data) > 0:
                                        print(f"Nama mata kuliah: {data['nama']}")
                                        print(f"SKS: {data['sks']}")
                                        while True:
                                            smt = input("Semester ([O] Ganjil/[E] Genap): ")
                                            match smt.upper():
                                                case 'O':
                                                    kr.semester = "Gasal"
                                                    break
                                                case 'E':
                                                    kr.semester = "Genap"
                                                    break
                                                case _:
                                                    print("Pilihan salah!")
                                        kr.thn_akademik = int(input("Tahun akademik (tahun semester gasal saja): "))
                                        kr.ubah_krs(nim, kd_matkul)
                                        berhasil = True
                                        break
                                    else:
                                        print(f"Data mata kuliah dengan kode [{kd_matkul}] tidak ditemukan")
                            else:
                                print(f"Data mahasiswa dengan NIM [{nim}] tidak ditemukan")
                            if berhasil:
                                print()
                                break

                    case 3:
                        while True:
                            nim = input("NIM: ")
                            data = mhs.ambil_data(nim)
                            if len(data) > 0:
                                print(f"Nama mahasiswa: {data['nama']}")
                                kd_matkul = input("Kode mata kuliah: ")
                                data = mk.tampil_detail(kd_matkul)
                                if len(data) > 0:
                                    print(f"Nama mata kuliah: {data['nama']}")
                                    print(f"SKS: {data['sks']}")
                                    nil.presensi = int(input("Presensi: "))
                                    nil.tugas = int(input("Tugas: "))
                                    nil.uts = int(input("UTS: "))
                                    nil.uas = int(input("UAS: "))
                                    nil.update_khs(nim, kd_matkul)
                                    print()
                                    break
                                else:
                                    print(f"Data mata kuliah dengan kode [{kd_matkul}] tidak ditemukan")
                            else:
                                print(f"Data mahasiswa dengan NIM [{nim}] tidak ditemukan")

                    case 4:
                        while True:
                            jdD.nidn = input("NIDN/NUPTK: ")
                            data = dos.ambil_data_dos(jdD.nidn)
                            if len(data) > 0:
                                print(f"Nama dosen: {data['nama']}")
                                while True:
                                    jdD.kd_matkul = input("Kode mata kuliah: ")
                                    data = mk.tampil_detail(jdD.kd_matkul)
                                    if len(data) > 0:
                                        print(f"Nama mata kuliah: {data['nama']}")
                                        print(f"SKS: {data['sks']}")

                                        while True:
                                            smt = input("Semester ([O] Ganjil/[E] Genap): ")
                                            match smt.upper():
                                                case 'O':
                                                    jdD.semester = "Gasal"
                                                    break
                                                case 'E':
                                                    jdD.semester = "Genap"
                                                    break
                                                case _:
                                                    print("Pilihan salah!")

                                        jdD.thn_akademik = int(input("Tahun akademik (tahun semester gasal saja): "))

                                        jdD.kelompok = input("Kelompok: ")

                                        hari_map = {'1': 'Senin', '2': 'Selasa', '3': 'Rabu', '4': 'Kamis', '5': 'Jumat', '6': 'Sabtu'}
                                        while True:
                                            h = input("Hari ([1] Senin-[6] Sabtu): ")
                                            if h in hari_map:
                                                jdD.hari = hari_map[h]
                                                break
                                            else:
                                                print("Pilihan salah!")

                                        jdD.jam_mulai = input("Jam mulai (hh:mm): ")
                                        jdD.jam_selesai = input("Jam selesai (hh:mm): ")
                                        jdD.ruang = input("Ruang: ")

                                        jdD.simpan_jadwal_dos()
                                        print("Data jadwal berhasil disimpan")
                                        print()
                                        berhasil = True
                                        break
                                    else:
                                        print(f"Data mata kuliah dengan kode [{jdD.kd_matkul}] tidak ditemukan")
                            else:
                                print(f"Data dosen dengan NIDN [{jdD.nidn}] tidak ditemukan")

                            if berhasil:
                                break

                    case 5:
                        while True:

                            nidn_cari = input("NIDN/NUPTK: ")

                            data_dos = dos.ambil_data_dos(nidn_cari)
                            if len(data_dos) == 0:
                                print(f"Data dosen dengan NIDN [{nidn_cari}] tidak ditemukan")
                                ulang = input("Tekan R jika ingin mencoba lagi: ").upper() == 'R'
                                if not ulang: break
                                continue

                            print(f"Nama dosen: {data_dos['nama']}")

                            data_jadwal = jdD.ambil_data_jadwal_dos(nidn_cari)

                            if len(data_jadwal) > 0:
                                print(f"Kode mata kuliah: {data_jadwal['kd_matkul']}")
                                print(f"Nama mata kuliah: {data_jadwal['nm_matkul']}")
                                print(f"SKS: {data_jadwal['sks']}")

                                while True:
                                    smt = input("Semester ([O] Ganjil/[E] Genap): ")
                                    match smt.upper():
                                        case 'O':
                                            jdD.semester = "Gasal"
                                            break
                                        case 'E':
                                            jdD.semester = "Genap"
                                            break
                                        case _:
                                            print("Pilihan salah!")

                                jdD.thn_akademik = int(input("Tahun akademik (tahun semester gasal saja): "))

                                jdD.kelompok = input(f"Kelompok ({data_jadwal['kelompok']}): ") or data_jadwal[
                                    'kelompok']

                                hari_map = {'1': 'Senin', '2': 'Selasa', '3': 'Rabu', '4': 'Kamis', '5': 'Jumat', '6': 'Sabtu'}
                                while True:
                                    h = input(f"Hari ([1] Senin-[6] Sabtu) [{data_jadwal['hari']}]: ")
                                    if h in hari_map:
                                        jdD.hari = hari_map[h]
                                        break
                                    elif h == "":
                                        jdD.hari = data_jadwal['hari']
                                        break
                                    else:
                                        print("Pilihan salah!")

                                jdD.jam_mulai = input(f"Jam mulai (hh:mm) [{data_jadwal['jam_mulai']}]: ") or \
                                                 data_jadwal['jam_mulai']

                                jdD.jam_selesai = input(f"Jam selesai (hh:mm) [{data_jadwal['jam_selesai']}]: ") or \
                                                 data_jadwal['jam_selesai']

                                jdD.ruang = input(f"Ruang [{data_jadwal['ruang']}]: ") or data_jadwal['ruang']

                                jdD.ubah_jadwal_dos(data_jadwal['kd_jadwal'])
                                print(f"Data jadwal [{data_jadwal['kd_jadwal']}] berhasil diubah")
                                print()
                                berhasil = True
                                break
                            else:
                                print(f"Data jadwal untuk NIDN [{nidn_cari}] tidak ditemukan")
                                ulang = input("Tekan R jika ingin mencoba lagi: ").upper() == 'R'
                                if not ulang: break

                            if berhasil: break
                    case 6:
                        break
                    case _:
                        print("Pilihan salah!")
        case 3:
            while True:
                print("[3.1] Cetak KHS")
                print("[3.2] Cetak Jadwal")
                print("[3.3] Kembali")
                try:
                    pilih2 = int(input("Masukkan Pilihan Anda (1-3): "))
                except ValueError:
                    print("Input harus berupa angka!")
                    continue
                print()
                match pilih2:
                    case 1:
                        while True:
                            nim = input("NIM: ")
                            mhs = Mahasiswa()
                            data = mhs.ambil_data(nim)
                            if len(data) > 0:
                                print(f"Nama Mahasiswa: {data['nama']}")
                                while True:
                                    smt = input("Semester ([O] Ganjil/[E] Genap): ")
                                    match smt.upper():
                                        case 'O':
                                            semester = "Gasal"
                                            break
                                        case 'E':
                                            semester = "Genap"
                                            break
                                        case _:
                                            print("Pilihan salah!")
                                thn_akademik = int(input("Tahun akademik (tahun semester gasal saja): "))

                                reports_dir = abspath(dirname(__file__))
                                input_file = join(reports_dir, "khs.jasper")
                                output_file = join(reports_dir, "khs")
                                prj = PyReportJasper()
                                params = {"nim": nim, "semester": semester, "thn_akademik": thn_akademik}

                                mysql_conf = {
                                    "driver": "mysql",
                                    "username": "root",
                                    "password": "",
                                    "host": "localhost",
                                    "database": "universitas",
                                    "port": "3306",
                                    "jdbc_driver": "com.mysql.cj.jdbc.Driver",
                                    "jdbc_dir": reports_dir
                                }

                                print("Membuat KHS...")
                                prj.config(input_file, output_file, parameters=params, db_connection=mysql_conf)
                                prj.process_report()
                                print("KHS selesai dibuat! Membuka KHS...")
                                startfile(f"{output_file}.pdf")
                                print()
                                break
                            else:
                                print(f"Data mahasiswa dengan NIM [{nim}] tidak ditemukan")
                    case 2:
                        while True:
                            nidn = input("NIDN/NUPTK: ")
                            dos = Dosen()
                            data = dos.ambil_data_dos(nidn)
                            if len(data) > 0:
                                print(f"Nama Dosen: {data['nama']}")
                                while True:
                                    smt = input("Semester ([O] Ganjil/[E] Genap): ")
                                    match smt.upper():
                                        case 'O':
                                            semester = "Gasal"
                                            break
                                        case 'E':
                                            semester = "Genap"
                                            break
                                        case _:
                                            print("Pilihan salah!")
                                thn_akademik = int(input("Tahun akademik (tahun semester gasal saja): "))
                                reports_dir = abspath(dirname(__file__))
                                input_file = join(reports_dir, "jdwl_kuliah_dosen.jasper")
                                output_file = join(reports_dir, "jdwl_kuliah_dosen")
                                prj = PyReportJasper()
                                params = {"nidn": nidn, "semester": semester, "thn_akademik": thn_akademik}
                                mysql_conf = {
                                    "driver": "mysql",
                                    "username": "root",
                                    "password": "",
                                    "host": "localhost",
                                    "database": "universitas",
                                    "port": "3306",
                                    "jdbc_driver": "com.mysql.cj.jdbc.Driver",
                                    "jdbc_dir": reports_dir
                                }
                                print("Membuat Laporan Jadwal...")
                                prj.config(input_file, output_file, parameters=params, db_connection=mysql_conf)
                                prj.process_report()
                                print("Laporan selesai dibuat! Membuka file...")
                                startfile(f"{output_file}.pdf")
                                print()
                                break
                            else:
                                print(f"Data dosen dengan NIDN [{nidn}] tidak ditemukan")
                    case 3:
                        break
                    case _:
                            print("Pilihan salah!")
        case 4:
            print("Terima kasih!")
            exit()
        case _:
                print("Pilihan salah!")