print("Pengisian Data Karyawan Untuk Menentukan Gaiji")
nama = str(input("Masukkan Nama Karyawan: "))
hari_kerja = int(input("Masukkan Hari Kerja Anda Dakam Sebulan Ini: "))
hari_kerja_sebulan = int(22)
hari_lembur_sebulan = (input("Hari Lembur Anda Dalam Sebulan: "))
gaji = 5000000
uang_lembur_perhari = 200000
print("Nama Karyawan", nama)

total_gaji = int((hari_kerja/hari_kerja_sebulan)*gaji+(hari_kerja_sebulan*uang_lembur_perhari))
print("Gaji Anda Bulan Ini Adalah Sebesar Rp. {:,}".format (total_gaji))