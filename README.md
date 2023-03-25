# 15-Puzzle-Solver

Tugas Kecil 3 IF2211 Strategi Algoritma <br>
Penyelesaian Persoalan 15-Puzzle dengan Algoritma _Branch and Bound_ <br>
Semester II Tahun 2021/2022 <br>

## Daftar Isi

- [Deskripsi Program](#deskripsi-program)
- [Demo Program](#demo-gui)
- [_Requirement_ Program](#requirement-program)
- [Cara Menjalankan Program](#cara-menjalankan-program)
- [Author](#dibuat-oleh)

## Deskripsi Program

Program dalam bahasa Python yang dapat menyelesaikan persoalan 15-Puzzle dengan
menggunakan Algoritma _Branch and Bound_ berdasarkan inputan file yang berisikan matriks status awal persoalan.
Nilai bound tiap simpul adalah penjumlahan cost yang diperlukan untuk sampai suatu simpul x dari akar,
dengan taksiran cost simpul x untuk sampai ke goal. Taksiran cost yang digunakan adalah
jumlah ubin tidak kosong yang tidak berada pada tempat sesuai susunan akhir (goal state). GUI program dibangun menggunakan Tkinter

Penjelasan singkat mengenai folder/file: <br>
`src` berisi source code dari program Python <br>
`test` berisi data uji <br>
`doc` berisi laporan dan spesifikasi tugas <br>
`run.bat` file untuk menjalankan program (compile and run) <br>
`README.md` file readme sebagai deskripsi keseluruhan <br>

## Demo GUI

![demo1](https://user-images.githubusercontent.com/71638224/161409246-b03d4764-192f-4bde-899b-065d9d575be5.gif)

## _Requirement_ Program

- Python 3.9 atau versi terbaru

## Cara Menjalankan Program

1. Pastikan telah mengunduh dan menginstal Python sesuai dengan _requirement_ program diatas. <br>
2. Ekstrak file Tucil3_13520139.zip ke folder yang sudah dibuat dan akses folder hasil ekstrak. <br>
3. Pengguna dapat dengan mudah menjalankan file bernama `run_cli.bat` untuk menjalankan program dalam CLI atau `run_gui.bat` untuk menjalankan program dalam GUI
4. Apabila program berhasil dijalankan, pengguna akan diminta untuk memasukkan input file matriks awal puzzle.
5. Pastikan file matriks awal puzzle yang ingin diselesaikan telah diletakkan pada folder `test`
6. Jika file berhasil dimuat, maka akan muncul pada layar fungsi Kurang(i), nilai X, dan langkah penyelesaian puzzle. Animasi penyelesaian puzzle dapat terlihat jika menjalankannya mengguna GUI.

## Dibuat oleh

Fachry Dennis Heraldi (13520139) <br>
K1 - IF2211 Strategi Algoritma <br>
Teknik Informatika <br>
Institut Teknologi Bandung <br>
2022 <br>
