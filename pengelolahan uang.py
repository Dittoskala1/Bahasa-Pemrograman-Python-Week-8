def header():
    print(" _                 _                      _   _           _                      _        ")
    print("| |               | |                    (_) (_)         | |                    (_)       ")
    print("| | _____ _ __ ___| |_ __ _    __ _ _ __  _   _ _ __   __| | ___  _ __   ___ ___ _  __ _  ")
    print("| |/ / _ | '__/ _ | __/ _` |  / _` | '_ \| | | | '_ \ / _` |/ _ \| '_ \ / _ / __| |/ _` | ")
    print("|   |  __| | |  __| || (_| | | (_| | |_) | | | | | | | (_| | (_) | | | |  __\__ | | (_| | ")
    print("|_|\_\___|_|  \___|\__\__,_|  \__,_| .__/|_| |_|_| |_|\__,_|\___/|_| |_|\___|___|_|\__,_| ")
    print("                                   | |                                                    ")
    print("                                   |_|                                                    ")

def garis():
    for i in range(80):
        print('-', end='')
    print()

def main():
    awal = True

    jalur = {
        1: {"nama": "Solo", "harga": 650000},
        2: {"nama": "Magelang", "harga": 300000},
        3: {"nama": "Yogyakarta", "harga": 2500000},
        4: {"nama": "Gombong", "harga": 400000},
        5: {"nama": "Semarang", "harga": 450000}
    }

    while awal:
        nama = input("Masukkan nama Anda: ")
        alamat = input("Masukkan alamat Anda: ")

        header()
        print("Nama       :", nama)
        print("Alamat     :", alamat)
        garis()
        print("\t\t===========================")
        print("\t\t|| TUJUAN KERETA API ||")
        print("\t\t===========================")
        garis()
        for key, value in jalur.items():
            print(f"{key}. Jalur {value['nama']}       : Rp. {value['harga']}")

        pilihan = int(input("Masukkan nomor jalur yang anda lalui: "))
        if pilihan in jalur:
            print(f"Jalur perjalanan yang anda pilih : {jalur[pilihan]['nama']}")
            print(f"Harga tiket  Rp. {jalur[pilihan]['harga']}")
            uang = float(input("Masukkanuang anda: Rp. "))
            kembalian = uang - jalur[pilihan]['harga']
            print("________________________________________________________________ -")
            print(f"Kembalian anda: Rp. {kembalian}")
            print("Hati-hati dalam perjalanan dan sampai tujuan tepat waktu !!!")
        else:
            print("Nomor jalur yang anda masukkan tidak valid.")

        jawab = input("Apakah Anda ingin melakukan perjalanan lagi? (Y/N) ")
        if jawab.upper() != 'Y':
            awal = False

    print("Silakan anda melanjutkan tujuan anda!")


if __name__ == "__main__":
    main()
