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

### codingan class mahasiswa ###


penggunaan class mahasiswa

1 **pertama**
__init__: Ini adalah fungsi khusus yang dijalankan saat kita membuat objek baru. Fungsi ini digunakan untuk menginisialisasi (memberi nilai awal) pada atribut-atribut objek.

2 **kedua**
tambah_data: Fungsi ini digunakan untuk menambahkan data mahasiswa baru. Ia akan meminta input dari pengguna (nama, NIM, nilai) dan kemudian menyimpan data tersebut ke dalam daftar mahasiswa.

3 **ketiga**
tampilkan_data: Fungsi ini akan menampilkan semua data mahasiswa yang sudah tersimpan.

4 **keempat**
hapus_data: Fungsi ini akan menghapus data mahasiswa berdasarkan NIM yang diberikan.

5 ** kelima**
ubah_data: Fungsi ini akan mengubah data mahasiswa berdasarkan NIM yang diberikan. Pengguna bisa memilih data mana yang ingin diubah (nilai tugas, UTS, atau UAS).

Bagian Utama Program

data_mahasiswa = Mahasiswa(...): Di sini kita membuat objek data_mahasiswa dari kelas Mahasiswa.
data_mahasiswa.daftar_mahasiswa = []: Kita membuat list kosong untuk menyimpan data mahasiswa.
while True:: Ini adalah loop yang akan terus berjalan sampai pengguna memilih untuk keluar.
Menu: Program akan menampilkan menu pilihan kepada pengguna.
Pilihan: Pengguna akan memilih menu yang ingin dijalankan.
Kondisi: Berdasarkan pilihan pengguna, program akan menjalankan fungsi yang sesuai (tambah data, tampilkan data, hapus data, atau ubah data).

Sekian dan terimakasih semoga bermanfaat