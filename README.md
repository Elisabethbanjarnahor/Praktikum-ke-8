Tugas Praktikum

Buat program sederhana dengan mengaplikasikan penggunaan class. Buatlah class untuk menampilkan daftar nilai mahasiswa, dengan ketentuan:

• Method tambah() untuk menambah data

• Method tampilkan() untuk menampilkan data

• Method hapus(nama) untuk menghapus data berdasarkan nama

• Method ubah(nama) untuk mengubah data berdasarkan nama

• Buat diagram class, flowchart dan penjelasan programnya pada README.md.

• Commit dan push repository ke github.

Hay kenalin nama saya Elisabeth banjarnahor disini saya akan menjelaslan cara mengaplikasikan penggunaan class secara sederhana. 


## flowchart code class ##
![](https://github.com/Elisabethbanjarnahor/Praktikum-ke-8/blob/9e3da96ddb4132291e59a756a31566070e488e58/flowchart.jpg)



penggunaan class mahasiswa

1 **pertama**
__init__: Ini adalah fungsi khusus yang dijalankan saat kita membuat objek baru. Fungsi ini digunakan untuk menginisialisasi (memberi nilai awal) pada atribut-atribut objek.
![](https://github.com/Elisabethbanjarnahor/Praktikum-ke-8/blob/70b13b0773a208e75a42d698cc4a51511f462dd4/393561224-bb33f7eb-67fa-45f7-89b3-d11394820d07.png)


2 **kedua**
tambah_data: Fungsi ini digunakan untuk menambahkan data mahasiswa baru. Ia akan meminta input dari pengguna (nama, NIM, nilai) dan kemudian menyimpan data tersebut ke dalam daftar mahasiswa.
![](https://github.com/Elisabethbanjarnahor/Praktikum-ke-8/blob/28251d09560fbd69b43fd304ea36b917503a5b66/393561751-d3ff80bd-b503-49ca-a7a9-e3b73ef68e10.png)


3 **ketiga**
tampilkan_data: Fungsi ini akan menampilkan semua data mahasiswa yang sudah tersimpan.
![](https://github.com/Elisabethbanjarnahor/Praktikum-ke-8/blob/1b7ff3491b22b521a0a900acfee8cf951f61267b/393561563-ea3fb839-cf15-437c-aaf3-87df4667d21e.png)


4 **keempat**
hapus_data: Fungsi ini akan menghapus data mahasiswa berdasarkan NIM yang diberikan.
![](https://github.com/Elisabethbanjarnahor/Praktikum-ke-8/blob/5a5b7dbba05c526782b2563f0b9aef790d24c025/393561821-5625562f-c942-4655-afa8-820ea4d2f0e1.png)


5 ** kelima**
ubah_data: Fungsi ini akan mengubah data mahasiswa berdasarkan NIM yang diberikan. Pengguna bisa memilih data mana yang ingin diubah (nilai tugas, UTS, atau UAS).
![](https://github.com/Elisabethbanjarnahor/Praktikum-ke-8/blob/f66b6b6e29ba0d9517142533062485d84f8cefa2/393561766-cde4e49a-bed6-4530-9ccf-8d8015f6b36c.png)

6 **cari**
Fungsi mencari dan menampilkan data mahasiswa berdasarka NIM
![](https://github.com/Elisabethbanjarnahor/Praktikum-ke-8/blob/4494ba6002916bd00a637f864fbe88c4e1c5a064/393561829-5cef06d8-9e9e-4023-b1d9-caa9e7770a3f.png)


7 **menu utama**



8 **hasil** 
![](https://github.com/Elisabethbanjarnahor/Praktikum-ke-8/blob/dd1130b74bf558242fd9a3d462684637cb326cc0/393561907-31f09554-180c-4b53-8e54-830c5e996615.png)

Bagian Utama Program
data_mahasiswa = Mahasiswa(...): Di sini kita membuat objek data_mahasiswa dari kelas Mahasiswa.
data_mahasiswa.daftar_mahasiswa = []: Kita membuat list kosong untuk menyimpan data mahasiswa.
while True:: Ini adalah loop yang akan terus berjalan sampai pengguna memilih untuk keluar.
Menu: Program akan menampilkan menu pilihan kepada pengguna.
Pilihan: Pengguna akan memilih menu yang ingin dijalankan.
Kondisi: Berdasarkan pilihan pengguna, program akan menjalankan fungsi yang sesuai (tambah data, tampilkan data, hapus data, atau ubah data).

Sekian dan terimakasih semoga bermanfaat
