class Mahasiswa:
    def __init__(self, nama, nim, tugas, uts, uas):
        self.nama = nama
        self.nim = nim
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def tampilkan(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}, Tugas: {self.tugas}, UTS: {self.uts}, UAS: {self.uas}")

    def tambah(data):
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        tugas = int(input("Masukkan nilai tugas: "))
        uts = int(input("Masukkan nilai UTS: "))
        uas = int(input("Masukkan nilai UAS: "))
        mahasiswa_baru = Mahasiswa(nama, nim, tugas, uts, uas)
        data.append(mahasiswa_baru)
        print("Data mahasiswa berhasil ditambahkan")

    def ubah(data):
        nim_cari = input("Masukkan NIM yang ingin diubah: ")
        for i, mahasiswa in enumerate(data):
            if mahasiswa.nim == nim_cari:
                # Ubah data mahasiswa
                mahasiswa.nama = input("Masukkan nama baru: ")
                # ... dan seterusnya
                print("Data mahasiswa berhasil diubah")
                return
        print("NIM tidak ditemukan")

    def hapus(data):
        nim_cari = input("Masukkan NIM yang ingin dihapus: ")
        for i, mahasiswa in enumerate(data):
            if mahasiswa.nim == nim_cari:
                del data[i]
                print("Data mahasiswa berhasil dihapus")
                return
        print("NIM tidak ditemukan")

    def cari(data):
        nim_cari = input("Masukkan NIM yang dicari: ")
        for mahasiswa in data:
            if mahasiswa.nim == nim_cari:
                mahasiswa.tampilkan()
                return
        print("NIM tidak ditemukan")
    
    def lihat_data(data):
        if not data:
            print("Data mahasiswa masih kosong")
        else:
            for i, mahasiswa in enumerate(data):
                print(f"Mahasiswa ke-{i+1}")
                mahasiswa.tampilkan()


# Inisialisasi data mahasiswa
data = []

# Looping menu
while True:
    print("\n1. lihat data\n2. tambah data\n3. Ubah data\n4. Hapus data\n5. Cari data\n6. keluar")
    pilihan = input("Masukkan pilihan (1-6): ")
    if pilihan == '1':
        Mahasiswa.lihat_data(data)
    elif pilihan == '2':
        Mahasiswa.tambah(data)
    elif pilihan == '3':
        Mahasiswa.ubah(data)
    elif pilihan == '4':
        Mahasiswa.hapus(data)
    elif pilihan == '5':
        Mahasiswa.cari(data)
    elif pilihan == '6':
        print("Terima kasih")
        break
    else:
        print("Pilihan tidak valid. Masukkan angka 1-6")