#### CAP STONE PROJECT 1 YOSUA PRATAMA WIJAYA ####

#### MENU LIST ####
menuList = [
    ' ',
    '=============================',
    '',
    '1. Menampilkan Data Siswa',
    '2. Menambah Data Siswa',
    '3. Mengubah Data Siswa',
    '4. Menghapus Data Siswa',
    '5. Keluar Aplikasi',
    '',
    '============================='
    ' '
]

#=============================================================#
# KELOMPOK NILAI

# A > 80
# B 75 - 80
# C 70-75
# TIDAK LULUS <70

#=============================================================#
### DATA SET TYPE LIST###
nomorInduk = ['001', '002', '003','004','005']
namaDepanSiswa = ['Alice', "Bob", 'Charlie','David',' Frank',]
namaBelakangSiswa = ['Cole', 'Palmer', 'Bird', 'Heat', 'Core']
nilaiSiswa = ['80', '75', '70', '82', '79']
gradeNilai = ['A','B', 'C', 'A', 'B']

DatabaseSiswa = []

for i in range(len(nomorInduk)): #menampilkan data siswa sesuai urutan list nomor induk
    DataSiswa = {
        'NIS' : nomorInduk[i], # unique
        'NamaDepan' : namaDepanSiswa[i],
        'NamaBelakang' : namaBelakangSiswa[i],
        'Nilai' : nilaiSiswa[i],
        'Grade' : gradeNilai[i]
    }
    DatabaseSiswa.append(DataSiswa)

for DataSiswa in DatabaseSiswa:
    print(DataSiswa)

print(type(DatabaseSiswa))
#=============================================================#
# Grading menurut Input Nilai User
def Grading(nilai):
    """Menghitung Grade berdasarkan nilai yang diberikan"""
    if nilai >= 80:
        return "A"
    elif 75 <= nilai < 80:
        return "B"
    elif 70 <= nilai < 75:
        return "C"
    else:
        return "Tidak Lulus"
#=============================================================#
# Tampilkan NIS yang ada di Database
def DataTerbaru():
    print("NIS yang sudah terdaftar di database:")
    if DatabaseSiswa:  # Mengecek apakah database tidak kosong
        for siswa in DatabaseSiswa:
            print("-", siswa["NIS"])


#=============================================================#
## (1) LIST MENU READ
def menu1():
    print()
    print("======= MENU MELIHAT DATA SISWA =======\n")
    print("1. Menu Melihat Semua Data Siswa")
    print("2. Menu Melihat Data Siswa Tertentu")
    print("3. Menu Ranking Siswa Sementara")
    print("4. Kembali")
    subMenu = input("Masukkan menu yang dituju [1-4]: ")
    if subMenu == '1':
        ReadAllData(siswa = DatabaseSiswa)
    elif subMenu == '2':
        SearchSiswa()
    elif subMenu == '3':
        RankingSiswa()
    elif subMenu == '4':
        quit # kembali ke menu sebelumnya
        mainMenu() # kembali ke menu sebelumnya
    else:
        print("Input Anda tidak sesuai!")

# (1.1) FUNGSI READ * belum ditambahkan fitur sort
def ReadAllData(siswa):
    print('\n====================DATA SISWA=========================\n')
    for siswa in sorted(DatabaseSiswa, key=lambda x: x['NIS']):
        print(f'NIS : {siswa['NIS']}')
        print(f'Nama Depan : {siswa['NamaDepan']}')
        print(f'Nama Belakang : {siswa['NamaBelakang']}')
        print(f'Nilai {siswa['Nilai']}')
        print(f'Grade : {siswa['Grade']}')
        print('=' * 50)
    menu1()

# (1.2) FUNGSI READ SELECTION
def SearchSiswa():
    NIS_Input = input("Masukkan NIS siswa yang: ")

    NIS_ditemukan = None
    for siswa in DatabaseSiswa:
        if siswa['NIS'] == NIS_Input:
            NIS_ditemukan = siswa
            break
    
    if NIS_ditemukan:
        print(f"\nData Ditemukan: \n NIS: {NIS_ditemukan['NIS']}\n Nama Depan: {NIS_ditemukan['NamaDepan']}\n Nama Belakang :{NIS_ditemukan['NamaBelakang']}\n Nilai : {NIS_ditemukan['Nilai']}\n Grade : {NIS_ditemukan['Grade']}")
    else:
        print("\nNIS tidak ditemukan!")
    menu1()

# (1.3) FUNGSI RANK 
def RankingSiswa():
    print('\n====================DATA SISWA=========================\n')
    for siswa in sorted(DatabaseSiswa, key=lambda x: int(x['Nilai']), reverse= True):
        print(f'NIS : {siswa['NIS']}')
        print(f'Nama Depan : {siswa['NamaDepan']}')
        print(f'Nama Belakang : {siswa['NamaBelakang']}')
        print(f'Nilai {siswa['Nilai']}')
        print(f'Grade : {siswa['Grade']}')
        print('=' * 50)
    menu1()



#=============================================================#

## (2) LIST MENU CREATE 
def menu2():
    print()
    print("======= MENU MELIHAT TAMBAH SISWA =======")
    print("1. Menu Tambah Data Siswa")
    print("2. Kembali")
    subMenu = input("Masukkan menu yang dituju [1-2]: ")
    if subMenu == '1':
       NIS_terdaftar()
       inputdata()
    elif subMenu == '2':
        quit # kembali ke menu sebelumnya
        mainMenu() # kembali ke menu sebelumnya
    else:
        print("Input Anda tidak sesuai!")

# (2.1.1) MENAMPILKAN NIS
def NIS_terdaftar():
    DataTerbaru()
    #loop untuk memastikan input y/n
    while True:
        Konfirmasi = input(" Ingin menambahkan data (y/n) : ").lower()
        if Konfirmasi == "y":
            inputdata()
            break
        elif Konfirmasi == "n":
            print("Proses penambahan data dibatalkan")
            break
        else:
            print("\nInput tidak valid!,Silahkan input 'y' untuk melanjutkan dan 'n' untuk batal!\n")
    else:
        print("Belum ada data NIS yang terdaftar.")
  

# (2.1.2) MEMBUAT DATA BARU
def inputdata():
    while True:
        createNIS = input("Masukkan NIS: ")
        # Cek input NIS apakah duplikat
        if any(siswa["NIS"] == createNIS for siswa in DatabaseSiswa):
            print("NIS sudah ada, silakan masukkan NIS yang berbeda.")
        else:
            break  # Jika NIS unik, lanjutkan ke tahap berikutnya

    CreateNamaDepan = input("Masukkan Nama Depan: ")
    CreateNamaBelakang = input("Masukkan Nama Belakang: ")
    CreateNilai = int(input("Masukkan Nilai: "))  # Konversi ke integer
    
    CreateGrade = Grading(CreateNilai)

    siswa_baru = {"NIS": createNIS, "NamaDepan": CreateNamaDepan, "NamaBelakang": CreateNamaBelakang, "Nilai": CreateNilai, "Grade": CreateGrade}
    print("Draft Data yang anda input:")
    print(siswa_baru)

    while True :
        konfirmasiInput = input('Apakah anda yakin menambahkan data diatas? (y/n) : ').lower()
        if konfirmasiInput == 'y':
            DatabaseSiswa.append(siswa_baru)  # Menambahkan data ke dalam database
            print("Data berhasil ditambahkan!") #Konfirmasi update
        
            print("Data terupdate: ") #Menampilkan data terbaru
            for siswa in DatabaseSiswa:
                print(siswa)
            menu2() # kembali ke submenu Read
            break

        elif konfirmasiInput == 'n':
            print("\nProses penambahan data dibatalkan!")
            menu2()
            break
        else:
            print("\nInput tidak valid! Hanya isi 'y' untuk melanjutkan dan 'n' untuk batal.")

#=============================================================#
## (3) UPDATE MENU
def menu3():
    DataTerbaru()
    while True:
        print("======= MENU MENGUBAH DATA SISWA =======")
        print("1. Menu Mengubah Data Siswa")
        print("2. Kembali")    
        submenu = input("\nMasukkan menu yang dituju [1-2]: ")
        if submenu == '1':
            SearchSiswa2()
        elif submenu == '2':
            break
        else:
            print("Input Anda tidak sesuai!")

# (3.1) UPDATE DATA SISWA
def SearchSiswa2():
    # mencari data siswa berbasis NIS
    NIS_Input = input("\nMasukkan NIS siswa yang ingin diupdate: ")

    NIS_ditemukan = None
    for siswa in DatabaseSiswa:
        if siswa['NIS'] == NIS_Input:
            NIS_ditemukan = siswa
            break

    if NIS_ditemukan:
        print(f"\nData Ditemukan:\nNIS: {NIS_ditemukan['NIS']}\nNama Depan: {NIS_ditemukan['NamaDepan']}\nNama Belakang: {NIS_ditemukan['NamaBelakang']}\nNilai: {NIS_ditemukan['Nilai']}\nGrade: {NIS_ditemukan['Grade']}\n")
        
        pilihan = input("Apakah ingin mengupdate data siswa? (y/n): ").lower() # konfirmasi user akan melakukan update data# bisa dengan input lain
        if pilihan == "y":
            draft_update =menuUpdate(NIS_ditemukan) # menyimpan draft sementara

            if draft_update:
                print("\n=== Draft Data yang Akan Diperbarui ===")
                for key in ["NamaDepan", "NamaBelakang", "Nilai", "Grade"]:
                    print(f"{key}: {NIS_ditemukan[key]} ➝ {draft_update[key]}")

                konfirmasi = input("\nApakah ingin menyimpan perubahan ini? (y/n): ").lower()
                if konfirmasi == 'y':
                    NIS_ditemukan.update(draft_update)  # Menyimpan perubahan ke data asli
                    print("\nData berhasil diperbarui!")
                    print("\nDatabase setelah pembaruan:")
                    for siswa in DatabaseSiswa:
                        print(siswa)
                else:
                    print("\nPerubahan dibatalkan, tidak ada perubahan pada Database.")

        else:
            print("\nTidak ada perubahan pada data.\n")
            menu3()
         
    else:
        print("\nNIS tidak ditemukan!\n")

      

# (3.1.1) UPDATE BERDASARKAN VARIABEL

def menuUpdate(NIS_ditemukan):
    print("======= UPDATE DATA SISWA =======")
    print("1. Nama Depan Siswa")
    print("2. Nama Belakang Siswa")
    print("3. Nilai")
    print("4. Kembali")
    submenu = input ("Masukan jenis data yang akan diupdate:")

    draft_update = NIS_ditemukan.copy()  # membuat draft yang akan di update

    if submenu == '1':
         draft_update["NamaDepan"] = input("Masukkan Nama Depan baru: ")
    elif submenu == '2':
         draft_update["NamaBelakang"] = input("Masukkan Nama Belakang baru: ")
    elif submenu == '3':
         draft_update["Nilai"] = int(input("Masukkan Nilai baru: "))  # Konversi ke integer
         draft_update["Grade"] = Grading(draft_update["Nilai"]) # Grading otomatis dari User Input
    elif submenu == '4':
        return
    else:
        print("Pilihan tidak ditemukan, silahkan pilih ulang!")
    
    return draft_update

#=============================================================#
# (4.) DELETE MENU
def menu4():
    print()
    print("======= MENU MENGHAPUS DATA SISWA =======")
    print("1. Menu Hapus Data Siswa")
    print("2. Kembali")
    subMenu = input("Masukkan menu yang dituju [1-2]: ")
    if subMenu == '1':
        NIS_terdaftar2()
        hapusData()
    elif subMenu == '2':
        quit # kembali ke menu sebelumnya
        mainMenu() # kembali ke menu sebelumnya
    else:
        print("Input Anda tidak sesuai!")

# (4.1) 
def NIS_terdaftar2():
    print("NIS yang sudah terdaftar di database:")
    if DatabaseSiswa:  # Mengecek apakah database tidak kosong
        for siswa in DatabaseSiswa:
            print("-", siswa["NIS"])
        while True: 
            Konfirmasi = input(" Ingin menghapus data (y/n) : ").lower()# bisa dengan input lain
            while True:
                if Konfirmasi == "y":
                    hapusData()
                    break
                elif Konfirmasi == "n":
                    print("Proses hapus data dibatalkan!")
                    break
                else:
                    print("Input tidak valid! Hanya isi 'y' untuk melanjutkan dan 'n' untuk batal.")
                    break
    else:
        print("Belum ada data NIS yang terdaftar.")

# (4.2) 
def hapusData():
    NIS_Input = input("Masukkan NIS siswa yang ingin dihapus: ") 

    # Mencari siswa berdasarkan NIS
    siswa_ditemukan = None
    for siswa in DatabaseSiswa:
        if siswa['NIS'] == NIS_Input:
            siswa_ditemukan = siswa
            break

    if siswa_ditemukan:
        # Menampilkan data yang akan dihapus
        print("\n=== Data yang akan dihapus ===")
        print(f"NIS: {siswa_ditemukan['NIS']}")
        print(f"Nama Depan: {siswa_ditemukan['NamaDepan']}")
        print(f"Nama Belakang: {siswa_ditemukan['NamaBelakang']}")
        print(f"Nilai: {siswa_ditemukan['Nilai']}")
        print(f"Grade: {siswa_ditemukan['Grade']}\n")

        konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ").lower()
        
        if konfirmasi == 'y':
            DatabaseSiswa.remove(siswa_ditemukan)  # Hapus data dari database
            print("\nData siswa telah dihapus!\n")

            # Menampilkan data yang tersisa dalam database
            print("=== Data siswa yang masih ada ===")
            if DatabaseSiswa:
                for siswa in DatabaseSiswa:
                    print(f"NIS: {siswa['NIS']}, Nama: {siswa['NamaDepan']} {siswa['NamaBelakang']}, Nilai: {siswa['Nilai']}, Grade: {siswa['Grade']}")
            else:
                print("(Database kosong)")
        else:
            print("\nPenghapusan dibatalkan, data tetap ada dalam database.")
    
    else:
        print("\nNIS tidak ditemukan dalam database.")
    menu4()


#=============================================================#
## FLOW PROGRAM
def mainMenu():
    userInput = 5

    while userInput != '5':
        for menu in menuList:
            print(menu)
        userInput = input("Masukkan menu yang dituju [1-5]: ")
        if userInput == '1':
            menu1()
        elif userInput == '2':
            menu2()
        elif userInput == '3':
            menu3()
        elif userInput == '4':
            menu4()
        elif userInput == '5':
            print("Anda telah keluar dari aplikasi.")
            break
        else:
            print("Menu yang Anda pilih tidak sesuai!\n")
mainMenu()







