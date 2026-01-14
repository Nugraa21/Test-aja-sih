
# SaWiT OS v1.1 - Terminal Nugra21

**SaWiT OS** adalah simulasi sistem operasi berbasis terminal (CLI) yang dibuat sepenuhnya dengan Python. Terinspirasi dari dunia perkebunan kelapa sawit, proyek ini menggabungkan nuansa Indonesia, warna-warni terminal, dan fitur-fitur seru seperti mode sudo, filesystem permanen, hingga telur paskah!

**Creator:** Ludang Prasetyo Nugroho (@nugra)  
**Versi:** 1.1 (SAWIT-ENHANCED)  
**Tanggal Rilis:** Januari 2026  
**Bahasa:** Indonesia (dengan sentuhan kreatif perkebunan sawit 🌴)

## Fitur Utama

- Terminal interaktif dengan prompt cantik (waktu, branch, role)
- Filesystem virtual permanen (disimpan di `data/sawit_fs.json`)
- Dua role pengguna: **RAKYAT** dan **PEJABAT** (dengan SUDO)
- Perintah bertema sawit: TANAM, PANEN, RAWAT, TEBANG, IRIGASI, dll
- Animasi loading, banner acak, neofetch custom
- Riwayat perintah, tree direktori, pencarian file
- Telur paskah dengan ketik `SAWIT`

## Struktur Direktori Awal

```
/ (root)
├── home/
│   ├── nugra/
│   │   ├── readme.txt
│   │   └── projects/
│   │       └── sawit.py
│   └── shared/
│       └── motivasi.txt
└── bin/
    └── help.txt
```

## Cara Install & Persiapan

### 1. Requirements
Pastikan kamu punya:
- Python 3.7 atau lebih baru
- pip (Python package manager)

### 2. Install Library yang Dibutuhkan
Buka terminal/cmd, lalu jalankan:

```bash
pip install colorama
```

> Hanya `colorama` yang wajib. Library lain (os, datetime, json, dll) sudah bawaan Python.

### 3. Download & Jalankan Code

1. Simpan kode sebagai `sawit_os.py` atau `main.py`
2. Jalankan dengan:

```bash
python sawit_os.py
```

Atau jika ingin langsung jadi file .exe (Windows):

```bash
pip install pyinstaller
pyinstaller --onefile --console --name "SaWiT-OS-v1.1" sawit_os.py
```

Hasilnya ada di folder `dist/SaWiT-OS-v1.1.exe` → tinggal double-click!

## Daftar Perintah Lengkap

| Perintah      | Alias       | Keterangan                                                                 | Akses          |
|----------------|-------------|-----------------------------------------------------------------------------|----------------|
| `LIHAT`       | `LS`        | Tampilkan isi direktori saat ini (berwarna)                                | Semua          |
| `MASUK`       | -           | Masuk ke folder (cd)                                                       | Semua          |
| `MUNDUR`      | -           | Kembali ke folder atas                                                     | Semua          |
| `POSISI`      | -           | Tampilkan path saat ini (pwd)                                              | Semua          |
| `BUKA`        | -           | Buat folder baru                                                           | Semua          |
| `BAKAR`       | -           | Hapus folder (hanya PEJABAT!)                                              | PEJABAT        |
| `KEBUN`       | -           | Tampilkan struktur pohon direktori                                         | Semua          |
| `TANAM`       | -           | Buat file kosong baru                                                      | Semua          |
| `PANEN`       | -           | Baca isi file                                                              | Semua          |
| `RAWAT`       | -           | Edit file (ketik `:simpan` untuk save, `:keluar` untuk batal)              | Semua          |
| `TEBANG`      | -           | Hapus file atau folder                                                     | Semua          |
| `CANGKOK`     | -           | Salin file (CANGKOK sumber tujuan)                                         | Semua          |
| `PINDAH`      | -           | Pindah atau rename file/folder                                             | Semua          |
| `IRIGASI`     | -           | Cari file/folder berdasarkan kata kunci                                    | Semua          |
| `BERSIHKAN`   | `CLS`       | Bersihkan layar                                                            | Semua          |
| `WAKTU`       | -           | Tampilkan waktu saat ini                                                   | Semua          |
| `SIAPA`       | -           | Lihat nama user dan role saat ini                                          | Semua          |
| `INFO_SAWIT`  | -           | Info sistem dasar                                                          | Semua          |
| `NEOFETCH`    | -           | Dashboard info sistem lengkap (uptime, stats FS, dll)                      | Semua          |
| `SUDO`        | -           | Naik ke mode PEJABAT (password default: 123)                               | RAKYAT         |
| `RAKYAT`      | `UNSU`      | Turun kembali ke mode RAKYAT                                               | PEJABAT        |
| `BANTUAN`     | -           | Tampilkan daftar semua perintah                                            | Semua          |
| `HISTORY`     | -           | Lihat 10 perintah terakhir                                                 | Semua          |
| `SAWIT`       | -           | Telur paskah spesial 🌴                                                    | Semua          |
| `EXIT`        | `PULANG`    | Keluar dari SaWiT OS (data otomatis disimpan)                              | Semua          |

## Tutorial Pemakaian (Langkah demi Langkah)

### 1. Pertama Kali Buka
- Jalankan `python sawit_os.py` atau double-click .exe
- Muncul animasi loading → banner → prompt seperti ini:

```
nugra@sawit:/home/nugra] (main) 23:22 RAKYAT -> 
```

### 2. Eksplorasi Dasar
```bash
LIHAT          # lihat isi folder saat ini
MASUK projects # masuk ke folder projects
MUNDUR         # kembali
POSISI         # lihat di mana kamu sekarang
```

### 3. Buat & Edit File
```bash
TANAM catatan.txt     # buat file baru
RAWAT catatan.txt     # edit file
>> Halo ini isi baru
>> Baris kedua
:simpan               # simpan perubahan
PANEN catatan.txt     # baca isi file
```

### 4. Buat Folder & Struktur
```bash
BUKA dokumen
MASUK dokumen
TANAM surat.txt
RAWAT surat.txt
>> Isi surat penting...
:simpan
MUNDUR
KEBUN                 # lihat struktur pohon
```

### 5. Mode PEJABAT (SUDO)
```bash
SUDO
[sudo] password untuk nugra: 123    # ketik 123 (default)
# Sekarang prompt jadi merah & role PEJABAT
BAKAR dokumen         # hanya PEJABAT yang bisa bakar folder!
RAKYAT                # kembali jadi RAKYAT
```

### 6. Fitur Keren Lain
```bash
NEOFETCH        # dashboard sistem
IRIGASI sawit   # cari semua yang ada kata "sawit"
HISTORY         # lihat riwayat perintah
SAWIT           # telur paskah 😄
```

### 7. Keluar
```bash
EXIT            # atau PULANG
# Data otomatis disimpan ke data/sawit_fs.json
```

## Catatan
- Password default user `nugra` dan `pejabat` adalah **123**
- Data tersimpan permanen di folder `data/` (otomatis dibuat)
- Semua perubahan file/folder langsung tersimpan saat eksekusi perintah

## Terima Kasih!
Selamat menanam kode dan memanen keterampilan di **SaWiT OS**!  
Semoga proyek ini menghibur dan bermanfaat.  
Jangan lupa istirahat, minum air putih, dan terus berkarya! 🌴🚀

**Sawit adalah masa depan. Terus berkembang.**

— Ludang Prasetyo Nugroho (nugra)
