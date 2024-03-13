print("Silahkan Masukkan Sandi Dan Kata Sandi Untuk Login")
data_kamus = {
    "Salwan": "Salwan","Gatshu": "Gatshu","Ido": "Ido","Ilham": "Ilham","Safril": "Safril",
    "Agung": "Agung","Desstito": "Desstito","Nabil": "Nabil","Mujaddid": "Mujaddid","Amir": "Amir"
}

def login():
    username = input("Nama Pengguna: ")
    kata_sandi = input("Kata Sandi: ")

    if username in data_kamus and kata_sandi == data_kamus[username]:
        print("Selamat Datang!")
    else:
        print("Mohon masukkan data Anda dengan benar!")

login()