print("Pengisian Data Untuk Menentukan Gaji Anda")

nama = input("Masukkan Nama Anda: ")
hari_kerja = int(input("Masukkan Hari Kerja Anda Dalam Sebulan Ini: "))
hari_kerja_sebulan = 22
hari_lembur_perhari = int(input("Masukkan Hari lembur Anda Dalam Sebulan: "))
gaji_pokok = 8000000
uang_lembur_perhari = 200000

print("Nama Karyawan:", nama)

total_gaji = (hari_kerja/hari_kerja_sebulan)*gaji_pokok+(hari_lembur_perhari*uang_lembur_perhari)
print("Gaji Anda Bulan Ini Adalah Sebesar Rp. {:,}".format(total_gaji))