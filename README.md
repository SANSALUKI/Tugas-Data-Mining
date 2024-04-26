# Tugas-Data-Mining
Data Mining-Pertemuan 6 (Regresi Logistik) 
<hr>

# Tujuan Kode
Tujuan dari kode ini adalah untuk melakukan analisis dan prediksi kemungkinan seseorang mengalami serangan jantung berdasarkan berbagai atribut klinis. Dengan menggunakan regresi logistik, kita dapat memprediksi probabilitas seseorang mengalami serangan jantung berdasarkan atribut seperti usia, jenis kelamin, tekanan darah, kadar kolesterol, dan lainnya.
Kode ini juga bertujuan untuk memberikan pemahaman yang lebih dalam tentang faktor-faktor risiko yang berkaitan dengan serangan jantung serta untuk membantu dalam pengambilan keputusan klinis yang lebih baik dalam mengidentifikasi individu yang berisiko tinggi.
Dengan menganalisis data yang relevan dan membangun model prediksi yang akurat, diharapkan kode ini dapat memberikan kontribusi dalam upaya pencegahan dan penanganan penyakit jantung yang lebih efektif.
<hr>
Dataset terdiri dari 303 record dengan 13 atribut independen dan 1 target.
<br>
<br>Atribut:
<br>• Usia : Usia pasien
<br>• Jenis Kelamin : Jenis kelamin pasien (1=laki2, 0=perempuan)
<br>• exang: angina akibat olahraga (1 = ya; 0 = tidak)
<br>• caa: jumlah pembuluh arteri (0-3)
<br>• cp : Tipe nyeri dada
<br> Nilai 1 : angina tipikal
<br> Nilai 2: angina atipikal
<br> Nilai 3: nyeri non-angina
<br> Nilai 4: tanpa gejala
<br>• trtbps : tekanan darah istirahat (dalam mm Hg)
<br>• chol : kolestoral dalam mg/dl diambil melalui sensor BMI
<br>• fbs : (gula darah puasa >120 mg/dl)
<br>(1 = benar; 0 = salah)
<br>• rest_ecg : hasil elektrokardiografi istirahat
<br> Nilai 0: biasa
<br> Nilai 1 : mengalami kelainan gelombang ST-T (inversi
<br>gelombang T dan/atau elevasi atau depresi ST > 0,05mV)
<br> Nilai 2: menunjukkan kemungkinan atau pasti
<br>hipertrofi ventrikel kiri menurut kriteria Estes
<br>• thalach : tercapai denyut jantung maksimal
<br>Output (Target)
<br>0= lebih kecil kemungkinan terkena serangan jantung
<br>1= lebih besar kemungkinan terkena serangan jantung
<br>

## Unduh kode:

```

git clone https://github.com/SANSALUKI/Tugas-Data-Mining.git

```

### Alternative

```

wget https://github.com/SANSALUKI/Tugas-Data-Mining.git

```



## Pindahkan ke Direktori Kode: 
Gunakan perintah cd untuk berpindah ke direktori di mana kode Anda disimpan. Misalnya:

```
cd /mnt/c/path/to/heart_analysis

```

## Buat dan Aktifkan Lingkungan Virtual (Opsional): 
Jika Anda ingin mengisolasi dependensi kode ini, Anda dapat membuat dan mengaktifkan lingkungan virtual Python di WSL. Gunakan perintah yang sama seperti di lingkungan Linux biasa.

## Instal Dependensi: 
Setelah berpindah ke direktori kode, pastikan untuk memasang dependensi yang diperlukan dari file requirements.txt. Gunakan perintah:

```
pip install -r requirements.txt
```

## Jalankan Kode: 
Setelah semua dependensi terinstal, jalankan kode Python Anda dengan perintah:

```
python tugas.py
```
<hr style="border-top: 1px solid #ccc;">

# Dataset :
##  Heart Attack Analysis & Prediction Dataset
# Sumber : 
##  https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset/data
# Tujuan : 
##  ingin memprediksi apakah seseorang kemungkinan terkena serangan jantung.


