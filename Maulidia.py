print("======SELAMAT DATANG !!!======")
print("Isilah Data Dibawah Ini Untuk Menentukan Gaji Anda: ")
nama = str(input("Masukkan Nama Anda: "))
hari_kerja_sebulan = int(30)
hari_kerja = int(input("Berapa Hari Anda Masuk Kerja Dalam Sebulan: "))
hari_lembur = int(input("Berapa Hari Lembur Anda Masuk Dalam Sebulan: "))
upah_kerja_lembur = 150000
gaji_pokok = 2000000
print("Nama Karyawan", nama)
total_gaji = int((hari_kerja/hari_kerja_sebulan)*gaji_pokok+(hari_kerja_sebulan*upah_kerja_lembur))
print("Selamat Gaji Bulan Anda Pada Bulan Ini Sebesar Rp. {:,}".format (total_gaji))    