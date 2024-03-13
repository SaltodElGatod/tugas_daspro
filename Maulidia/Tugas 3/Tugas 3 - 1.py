data_kamus = {
    "Ifa": "Ifa123","Caca": "Caca456","Acha": "Acha789","Nia": "Nia123","Titin": "Titin456",
    "Manda": "Manda789","Fika": "Fika123","Hasna": "Hasna456","Rizka": "Rizka789","Nabila": "Nabila123"
}

def login():
    username = input("Nama Pengguna Anda: ")
    kata_sandi = input("Kata Sandi: ")

    if username in data_kamus and kata_sandi == data_kamus[username]:
        print("Selamat Datang!")
    else:
        print("Mohon masukkan data Anda dengan benar!")

login()