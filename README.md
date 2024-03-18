# Tugas Kecil II Strategi Algoritma (IF2211)
## Anggota :
- Ahmad Mudabbir Arif   (13522072)
- Muhammad Naufal Aulia (13522074)


## Table of Contents
* [Tentang Program](#bezier)
* [Screenshots](#screenshots)
* [Dependencies](#dependencies)
* [How to Use](#how-to-use)


## BJIR Bézier Curve Generator <a href="bezier"></a>
>  Kurva Bézier adalah adalah kurva halus yang sering digunakan dalam desain grafis, animasi, dan manufaktur. Kurva ini dibuat dengan menghubungkan beberapa titik kontrol, yang menentukan bentuk dan arah kurva.

Pada program ini, dilakukan pembangkitan kurva Bézier dengan menggunakan pendekatan algoritma _Divide and Conquer_ yang akan membagi persoalan titik kontrol menjadi dua bagian, menyelesaikan masing-masing bagian secara rekursif, dan menggabungkan hasilnya. Hasil kurva beserta waktu eksekusinya akan ditampilkan pada GUI yang ada di program ini.


## Screenshots <a href="screenshots"></a>
![Example screenshot](./test/bjir.gif)

## Dependencies <a href="dependencies"></a>
- Python 3.x

## How to Use <a href="how-to-use"></a>
1. Clone repository ini dengan 
    ```
    git clone https://github.com/NopalAul/Tucil2_13522072_13522074.git
    ```
2. Buka file directory/location tempat repository berada, buka folder `bin`, buka folder `dist`, hingga ditemukan file `bjir.exe`
    ```
    \Tucil2_13522072_13522074\bin\dist\bjir.exe
    ```
3. Jalankan program dengan double click pada file `bjir.exe`, tunggu hingga terbuka tampilan awal GUI program. Klik tombol `TRY ME` untuk memulai
4. Pada program, masukkan input pada kolom putih yang tersedia. Langkahnya adalah sebagai berikut:
    - Ketik nilai untuk absis X
    - Ketik nilai untuk ordinat Y
    - Klik `add point` untuk memasukkan titik tersebut
    - Ketik nilai untuk jumlah iterasi
    - Klik `GENERATE` untuk menghasilkan kurva Bézier
5. Jika ingin melakukan generate ulang, klik tombol `R E S E T` dan masukkan kembali input yang diinginkan
6. Close program untuk mengakhiri
7. Untuk melakukan perbandingan dengan algoritma _brute force_, dapat dijalankan file `bruteforce.py` pada folder `src`
   * _catatan: tinggal masukan iterasi yang sama dengan iterasi pada algoritma DnC, akan otomatis dibuat ekivalensi titiknya pada algoritma brute force_
