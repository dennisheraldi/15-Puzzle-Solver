# Tucil1_13520139

Tugas Kecil 3 IF2211 Strategi Algoritma <br>
Penyelesaian Persoalan 15-Puzzle dengan Algoritma _Branch and Bound_ <br>
Semester II Tahun 2021/2022 <br>

## Daftar Isi

- [Deskripsi Program](#deskripsi-program)
- [_Requirement_ Program](#requirement-program)
- [Cara Menjalankan Program](#cara-menjalankan-program)
- [Author](#dibuat-oleh)

## Deskripsi Program

Program dalam bahasa Python yang dapat menyelesaikan persoalan 15-Puzzle dengan
menggunakan Algoritma _Branch and Bound_ berdasarkan inputan file yang berisikan matriks status awal persoalan. 
Nilai bound tiap simpul adalah penjumlahan cost yang diperlukan untuk sampai suatu simpul x dari akar,
dengan taksiran cost simpul x untuk sampai ke goal. Taksiran cost yang digunakan adalah
jumlah ubin tidak kosong yang tidak berada pada tempat sesuai susunan akhir (goal state). 

Penjelasan singkat mengenai folder/file: <br>
`src` berisi source code dari program Python <br>
`test` berisi data uji <br>
`doc` berisi laporan dan spesifikasi tugas <br>
`run.bat` file untuk menjalankan program (compile and run) <br>
`README.md` file readme sebagai deskripsi keseluruhan <br>

## _Requirement_ Program

- Python 3.9 atau versi terbaru

## Cara Menjalankan Program

1. Pastikan telah mengunduh dan menginstal Python sesuai dengan _requirement_ program diatas. <br>
2. Ekstrak file Tucil3_13520139.zip ke folder yang sudah dibuat. <br>
<!-- 3. Jalankan Visual Studio Code dan arahkan pada folder hasil ekstraksi. <br>
4. Pada Visual Studio Code, buka Terminal, masuk ke folder yang sudah dibuat, dan jalankan file `run.bat`. Dapat secara langsung mengeksekusi perintah `run` kemudian enter. <br>
5. Jika sudah berhasil menjalankan program, maka akan muncul tampilan menu utama. <br>
6. File puzzle yang akan diselesaikan dapat diletakkan pada folder `test`, pastikan format telah sesuai dengan ketentuan (dapat dicontoh pada file test yang telah ada.
   <br>
7. Puzzle siap untuk diselesaikan, pilih menu "1. Selesaikan Puzzle" dan masukkan file puzzle yang akan diselesaikan. <br>
8. Program akan menampilkan hasil pencarian kata yang dicari. -->

## Dibuat oleh

Fachry Dennis Heraldi (13520139) <br>
K1 - IF2211 Strategi Algoritma <br>
Teknik Informatika <br>
Institut Teknologi Bandung <br>
2022 <br>
