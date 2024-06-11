from os import system

# Deklarasi variabel untuk menyimpan data mahasiswa
d_nama = []
d_nim = []
d_prodi = []
d_nilai = []
b_nama = []
b_kode = []
b_jumlah = []

def judul():
    print('===========================================')
    print('|              MENU PROGRAM               |')
    print('===========================================')
    
def menu():
    system('cls') 
    judul()
    print('===========================================')
    print('|         1. DATA MAHASISWA               |')
    print('|         2. INVENTARIS BARANG            |')
    print('===========================================')
    print(' ketik 3 untuk keluar !!')
    print('===========================================')
    menupilih = input('Pilih menu : ')
    
    if menupilih == '1':
        data_mahasiswa()
    elif menupilih == '2':
        inventaris_barang()
    elif menupilih == '3':
        exit()
    else:
        menu()

# Menu Data Mahasiswa
def data_mahasiswa():
    system('cls')
    judul()
    print('=============================================')
    print('|        1. INPUT DATA MAHASISWA            |')
    print('|        2. TAMPILKAN DATA MAHASISWA        |')
    print('|        3. HITUNG RATA-RATA NILAI          |')
    print('|        4. CARI NILAI TERTINGGI & TERENDAH |')
    print('|        5. KEMBALI KE MENU                 |')
    print('=============================================')
    pilih1 = input('Pilih Menu : ')
    
    if pilih1 == '1':
        input_data_mahasiswa()
    elif pilih1 == '2':
        tampilkan_data_mahasiswa()
    elif pilih1 == '3':
        hitung_rata_rata_nilai()
    elif pilih1 == '4':
        cari_nilai_tertinggi_terendah()
    elif pilih1 == '5':
        menu()
    else:
        data_mahasiswa()

# Menginput data mahasiswa nya 
def input_data_mahasiswa():
    system('cls')
    print('Input Data Mahasiswa')
    nama = input('Nama: ')
    nim = input('NIM: ')
    prodi = input('Prodi: ')
    nilai = float(input('Nilai: '))

# Fungsi Menambahkan Data Mahasiswa 
    d_nama.append(nama)
    d_nim.append(nim)
    d_prodi.append(prodi)
    d_nilai.append(nilai)
    
    print('Data berhasil ditambahkan!')
    input('Tekan Enter untuk kembali ke menu')
    data_mahasiswa()
    
def tampilkan_data_mahasiswa():
    system('cls')
    print('Data Mahasiswa:')
    if len(d_nim) == 0:
        print("Tidak ada data mahasiswa.")
    else:
        for i in range(len(d_nim)):
            print(f'{i+1}. Nama: {d_nama[i]}')
            print(f'    NIM: {d_nim[i]}')
            print(f'    Prodi: {d_prodi[i]}')
            print(f'    Nilai: {d_nilai[i]:.2f}')
            print('---------------------------')
    input('Tekan Enter untuk kembali ke menu')
    data_mahasiswa()

def hitung_rata_rata_nilai():
    system('cls')
    if len(d_nilai) == 0:
        print("Tidak ada data nilai untuk dihitung.")
    else:
        rata_rata = sum(d_nilai) / len(d_nilai)
        # Cara perhitungannya, fungsi sum menambahkan semua nilai trus di bagi dengan jumlah data nilai mahasiswa nya  
        print(f'Rata-rata nilai mahasiswa: {rata_rata:.2f}')
    input('Tekan Enter untuk kembali ke menu')
    data_mahasiswa()
    
def cari_nilai_tertinggi_terendah():
    system('cls')
    if len(d_nilai) == 0:
        print("Tidak ada data nilai untuk dicari.")
    else:
        # Perhitungan nilai tertinggi\terendah 
        nilai_tertinggi = max(d_nilai) # max = tertinggi, max dari data nilai 
        nilai_terendah = min(d_nilai) # min = terendah, max dari data nilai 
        idx_tertinggi = d_nilai.index(nilai_tertinggi) 
        idx_terendah = d_nilai.index(nilai_terendah)
        
        # output dari nilai tertinggi\terendah 
        print('Nilai Tertinggi:')
        print(f'Nama: {d_nama[idx_tertinggi]}, NIM: {d_nim[idx_tertinggi]}, Prodi: {d_prodi[idx_tertinggi]}, Nilai: {d_nilai[idx_tertinggi]:.2f}')
        print('---------------------------')
        print('Nilai Terendah:')
        print(f'Nama: {d_nama[idx_terendah]}, NIM: {d_nim[idx_terendah]}, Prodi: {d_prodi[idx_terendah]}, Nilai: {d_nilai[idx_terendah]:.2f}')
    input('Tekan Enter untuk kembali ke menu')
    data_mahasiswa()

# Menu Inventaris Barang 
def inventaris_barang():
    system('cls')
    judul()
    print('==============================================')
    print('|           1. INPUT DATA BARANG             |')
    print('|           2. TAMPILKAN SEMUA BARANG        |')
    print('|           3. CARI BARANG DENGAN KODE       |')
    print('|           4. HAPUS BARANG DENGAN KODE      |')
    print('|           5. KEMBALI KE MENU               |')
    print('==============================================')
    
    pilih2 = input('Pilih Menu :')
    
    if pilih2 == '1':
        input_data_barang()
    elif pilih2 == '2':
        tampilkan_semua_barang()
    elif pilih2 == '3':
        cari_barang_dengan_kode()
    elif pilih2 == '4':
        hapus_barang_dengan_kode()
    elif pilih2 == '5':
        menu()
    else:
        inventaris_barang()
        
def input_data_barang():
    system('cls')
    print('input data barang :')
    nama = input('Nama Barang : ')
    kode = input('Kode Barang : ')
    jumlah = int(input('Jumlah Barang :'))
    
    # Menambakna Data Barang 
    b_nama.append(nama)
    b_kode.append(kode)
    b_jumlah.append(jumlah)
    
    print('Data barang berhasil di tambahkan !')
    input('tekan enter unutk kembali ke menu !!!')
    inventaris_barang()
    
def tampilkan_semua_barang():
    system('cls')
    print('Data Inventaris Barang :')
    if len(b_kode) == 0:
        print('Tidak ada data barang !!!')
    else:
        for i in range(len(b_kode)):
            print(f'{i+1}. Nama Barang : {b_nama[i]}')
            print(f'Kode Barang : {b_kode[i]}')
            print(f'Jumlah Barang : {b_jumlah[i]}')
            print('===================================')
    input('Tekan enter untuk kembali ke menu !!!')
    inventaris_barang()
    
def cari_barang_dengan_kode():
    system('cls')
    kode = input('Masukan Kode Barang Yang Ingin Di Cari :')
    if kode in b_kode:
        idx = b_kode.index(kode)
        print('Data Barang :')
        print(f'Nama Barang : {b_nama[idx]}')
        print(f'kode Barang : {b_kode[idx]}')
        print(f'Nama jumlah : {b_jumlah[idx]}')
        
    else:
        print('Barang Tidak Ditemukan !!')
    input('Tekan enter untuk kembali ke menu !!!')
    inventaris_barang()
    
def hapus_barang_dengan_kode():
    system('cls')
    kode = input('Masukan kode barang yang ingin di hapus :')
    if kode in b_kode:
        idx = b_kode.index(kode)
        del b_nama[idx]
        del b_kode[idx]
        del b_jumlah[idx]
        print('Data barang berhasil di hapus. Terimakasih :)')
    else :
        print('Barang Tidak Ditemukan.')
    input('Tekan enter untuk kembali ke menu ')
    inventaris_barang()
    
            
                    
    
    
    
    
menu()
