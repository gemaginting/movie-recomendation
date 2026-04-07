# BAB 1 PENDAHULUAN

---

## 1.1. Latar Belakang

Era digital telah memicu ledakan informasi (*information overload*) yang menuntut adanya penyaringan informasi yang efektif [8]. Kondisi ini sering membuat pengguna merasa kewalahan menghadapi volume informasi yang sangat besar dalam berbagai platform digital [11]. Dalam berbagai bidang, khususnya pada platform hiburan digital seperti layanan *streaming* film, pengguna dihadapkan pada ribuan pilihan konten [10]. Banyaknya pilihan ini menimbulkan kebingungan atau *consumer confusion* dalam menentukan tontonan yang sesuai dengan preferensi mereka [4]. Kondisi ini menjadikan Sistem Rekomendasi bukan sekadar fitur tambahan, melainkan elemen bisnis penting untuk personalisasi konten pengguna [3]. Penerapan sistem rekomendasi yang efektif juga terbukti dapat meningkatkan retensi pengguna pada suatu platform [8].

Pendekatan umum yang digunakan dalam sistem rekomendasi adalah *Collaborative Filtering* (CF) [4]. Namun, beberapa penelitian menunjukkan bahwa metode CF murni memiliki kelemahan ketika dihadapkan pada kondisi data yang tidak ideal [1]. Dua masalah yang paling sering muncul adalah *Data Sparsity*, yakni kondisi di mana matriks *user-item* memiliki terlalu banyak nilai kosong [2], dan *Cold Start Problem* (CSP), yaitu kesulitan sistem dalam memberikan rekomendasi bagi pengguna baru yang belum memiliki riwayat interaksi [8]. Masalah ini juga menjadi kendala utama ketika item baru diperkenalkan ke dalam sistem [10]. Permasalahan tersebut berdampak langsung pada penurunan akurasi dan kualitas rekomendasi, sehingga pengguna mengalami ketidakpuasan (*poor recommendations*) [2]. Ketidakpuasan ini dapat menyebabkan pengguna meninggalkan platform jika tidak ditangani dengan baik [8].

Untuk mengatasi keterbatasan tersebut, penelitian di bidang sistem rekomendasi mulai beralih ke pendekatan *Hybrid Filtering* yang menggabungkan beberapa metode rekomendasi [6]. Pendekatan ini memungkinkan berbagai sumber data yang terintegrasi untuk menghasilkan akurasi yang lebih tinggi dibanding metode tunggal [3]. Selain itu, pendekatan *hybrid* juga terbukti lebih efektif dalam menangani skenario yang kompleks dibandingkan metode konvensional [13].

Penelitian ini menggunakan teknik *Model-Based Collaborative Filtering*, khususnya *Matrix Factorization* (MF). Sebagaimana dijelaskan oleh Wang (2022) [7], MF khususnya varian *Singular Value Decomposition* (SVD) lebih unggul dalam menangani *data sparsity*. Studi terbaru dari Rini et al. (2025) [12] juga menunjukkan bahwa SVD memberikan hasil prediksi yang lebih akurat (nilai MAE/RMSE lebih rendah) dibandingkan metode *neighborhood-based* seperti KNN. Pendekatan serupa juga diadopsi oleh Patro et al. (2020) [1] melalui penggunaan mekanisme *hybrid* pada dataset MovieLens untuk mengatasi masalah *sparsity*.

Meskipun demikian, metode MF/SVD murni masih menghadapi tantangan pada kasus *user cold start*, karena model ini membutuhkan data interaksi awal untuk membangun representasi pengguna yang akurat [9]. Di sisi lain, berbagai solusi *hybrid* modern yang diusulkan dalam penelitian terkini justru memiliki kompleksitas tinggi dan memerlukan sumber daya komputasi besar, seperti arsitektur SCSHRS (HOSVD + ANFIS) dan MGRS-HFA (*Graph Neural Network-based Hybrid Filtering*) [13]. Berdasarkan hal tersebut, terdapat celah penelitian (*research gap*) untuk mengembangkan sistem *hybrid recommender* yang bersifat lebih sederhana, namun tetap efektif dalam menangani permasalahan utama, yaitu *cold start* pada pengguna baru.

Berdasarkan permasalahan tersebut, penelitian ini bertujuan untuk merancang dan membangun sistem rekomendasi *Hybrid Filtering* dengan mekanisme *Switching* yang adaptif. Pendekatan ini dirancang untuk mengatasi masalah utama secara simultan, yaitu *cold start* pada pengguna baru dengan memanfaatkan *Content-Based Filtering* (CBF) berbasis genre film [10], [11], serta menangani masalah *data sparsity* pada pengguna terdaftar menggunakan *Singular Value Decomposition* (SVD) [7], [12]. Dengan pendekatan ini, diharapkan sistem dapat memberikan rekomendasi yang relevan sejak interaksi pertama pengguna, sekaligus menjaga akurasi yang tinggi saat data interaksi mulai terbentuk seiring waktu [9].

---

## 1.2. Rumusan Masalah

Berdasarkan uraian pada bagian latar belakang, permasalahan utama yang diidentifikasi dalam penelitian ini adalah keterbatasan metode *Collaborative Filtering* (CF) murni, terutama pada isu *data sparsity* dan *Cold Start Problem* (CSP). Berdasarkan hal tersebut, rumusan masalah yang akan dijawab melalui penelitian ini adalah sebagai berikut:

1. Bagaimana penerapan *Content-Based Filtering* (CBF) berbasis genre film dapat memberikan rekomendasi awal yang relevan untuk mengatasi permasalahan *cold start* pada pengguna baru?
2. Bagaimana efektivitas penerapan metode SVD dalam arsitektur *hybrid* dapat membantu mengurangi permasalahan *data sparsity* dan meningkatkan akurasi rekomendasi pada pengguna yang telah memiliki histori interaksi?
3. Bagaimana mengintegrasikan metode CBF dan SVD dalam arsitektur *hybrid* dengan mekanisme *switching* yang mampu memilih metode rekomendasi yang tepat berdasarkan status pengguna?

---

## 1.3. Tujuan dan Manfaat

Berdasarkan rumusan masalah yang telah dijelaskan sebelumnya, tujuan dari penelitian ini adalah sebagai berikut. Pertama, menerapkan metode *Content-Based Filtering* (CBF) berbasis genre film untuk menghasilkan rekomendasi awal yang relevan sebagai solusi terhadap permasalahan *cold start* pada pengguna baru. Kedua, menerapkan metode *Model-Based Collaborative Filtering* dengan pendekatan *Matrix Factorization* (SVD) untuk mengatasi permasalahan *data sparsity* pada pengguna yang telah memiliki histori interaksi. Ketiga, mengimplementasikan arsitektur *Hybrid Switching* ke dalam sistem rekomendasi berbasis web yang divalidasi melalui pengujian akurasi (RMSE/MAE) dan evaluasi pengguna (*User Acceptance Testing*).

Adapun manfaat yang diharapkan dari penelitian ini adalah tersedianya sebuah prototipe sistem rekomendasi film berbasis web yang mampu memberikan rekomendasi relevan kepada pengguna baru maupun pengguna terdaftar secara adaptif. Selain itu, penelitian ini diharapkan dapat menjadi referensi bagi pengembangan sistem rekomendasi *hybrid* yang lebih sederhana namun efektif, khususnya dalam konteks penanganan *cold start* pada platform hiburan digital.

Tabel 1.1 berikut menggambarkan keterkaitan antara tujuan penelitian, skenario pengujian, dan kesimpulan yang diharapkan.

**Tabel 1.1.** Tabel keterkaitan antara tujuan, pengujian, dan kesimpulan.

| No. | Tujuan | Pengujian | Kesimpulan |
|-----|--------|-----------|------------|
| 1 | Menerapkan CBF berbasis genre untuk mengatasi *cold start* pengguna baru | *User Acceptance Testing* (UAT) pada skenario pengguna baru | CBF berbasis genre mampu/tidak mampu memberikan rekomendasi awal yang relevan bagi pengguna baru |
| 2 | Menerapkan SVD untuk mengatasi *data sparsity* pada pengguna terdaftar | Pengujian kuantitatif dengan metrik RMSE dan MAE | SVD mampu/tidak mampu meningkatkan akurasi rekomendasi pada pengguna dengan histori interaksi |
| 3 | Mengimplementasikan arsitektur *Hybrid Switching* pada sistem berbasis web | Pengujian fungsional mekanisme *switching* dan UAT keseluruhan sistem | Arsitektur *Hybrid Switching* berhasil/tidak berhasil mengintegrasikan CBF dan SVD secara adaptif |

---

## 1.4. Batasan Masalah

Dalam pelaksanaan penelitian ini, terdapat beberapa batasan yang ditetapkan untuk menyederhanakan permasalahan agar dapat dikerjakan dalam lingkup Tugas Akhir satu semester. Batasan-batasan tersebut adalah sebagai berikut:

1. Dataset yang digunakan adalah dataset publik MovieLens (*MovieLens Small Dataset*) yang terdiri dari 100.000 data *rating* dari 600 pengguna terhadap 9.000 film. Dataset yang lebih besar tidak digunakan karena keterbatasan sumber daya komputasi yang tersedia.
2. Fitur konten yang digunakan pada metode *Content-Based Filtering* hanya terbatas pada atribut genre film. Fitur lain seperti sutradara, aktor, dan sinopsis tidak diikutsertakan karena memerlukan proses ekstraksi teks yang lebih kompleks dan berada di luar cakupan penelitian ini.
3. Mekanisme *switching* pada arsitektur *hybrid* ditentukan berdasarkan satu kriteria heuristik sederhana, yaitu jumlah *rating* yang telah diberikan oleh pengguna. Pengguna dengan jumlah *rating* di bawah ambang batas tertentu dikategorikan sebagai pengguna baru (*cold start*) dan dilayani oleh CBF, sedangkan pengguna dengan jumlah *rating* yang mencukupi dilayani oleh SVD.
4. Evaluasi sistem dilakukan melalui dua metode, yaitu pengujian kuantitatif (RMSE/MAE) untuk model SVD dan pengujian kualitatif (*User Acceptance Testing*) untuk menilai relevansi rekomendasi. Pengujian *online* dalam skala produksi tidak dilakukan karena keterbatasan waktu dan infrastruktur.
5. Sistem diimplementasikan sebagai prototipe aplikasi web menggunakan *framework* Django berbasis Python dan tidak mencakup fitur-fitur produksi seperti autentikasi OAuth, skalabilitas *cloud*, atau pembaruan model secara *real-time*.

---

## 1.5. Metode Penelitian

Penelitian ini dilaksanakan dengan menggunakan pendekatan rekayasa perangkat lunak (*software engineering*) yang dikombinasikan dengan eksperimen komputasional. Secara garis besar, metode penelitian yang diterapkan meliputi tahapan-tahapan berikut.

Pertama, **studi literatur**, yaitu penelusuran dan kajian terhadap berbagai sumber ilmiah yang relevan, meliputi jurnal internasional, prosiding konferensi, dan buku teks yang membahas sistem rekomendasi, *Collaborative Filtering*, *Content-Based Filtering*, *Hybrid Filtering*, dan *Matrix Factorization* (SVD).

Kedua, **pengumpulan dan praproses data**, yaitu pengunduhan dataset MovieLens dari sumber resmi, diikuti dengan proses pembersihan data (*data cleaning*), transformasi format, dan pembagian data menjadi data latih dan data uji.

Ketiga, **perancangan sistem**, yaitu perancangan arsitektur *Hybrid Switching* yang mencakup alur kerja CBF untuk pengguna baru dan alur kerja SVD untuk pengguna terdaftar, termasuk perancangan antarmuka pengguna (*user interface*) berbasis web.

Keempat, **implementasi sistem**, yaitu pembangunan prototipe sistem rekomendasi berbasis web menggunakan *framework* Django (Python), dengan mengintegrasikan model SVD dari pustaka *Surprise* dan implementasi CBF berbasis genre menggunakan *pandas*.

Kelima, **pengujian dan analisis**, yaitu evaluasi kinerja sistem menggunakan metrik RMSE dan MAE untuk model SVD, serta *User Acceptance Testing* (UAT) untuk menilai relevansi rekomendasi pada skenario pengguna baru.

Keenam, **penulisan laporan**, yaitu penyusunan buku Tugas Akhir secara bertahap sesuai dengan perkembangan penelitian dan hasil implementasi.

---

## 1.6. Jadwal Pelaksanaan

Berdasarkan rencana kegiatan yang telah disusun, Tabel 1.2 menyajikan detail jadwal pelaksanaan dari setiap tahapan yang direncanakan.

**Tabel 1.2.** Jadwal Pelaksanaan Tugas Akhir.

| No. | Deskripsi Tahapan | Bulan 1 | Bulan 2 | Bulan 3 | Bulan 4 | Bulan 5 | Bulan 6 |
|-----|-------------------|---------|---------|---------|---------|---------|---------|
| 1 | Studi Literatur | ✓ | ✓ | | | | |
| 2 | Pengumpulan dan Praproses Data | ✓ | ✓ | | | | |
| 3 | Perancangan Sistem | | ✓ | ✓ | | | |
| 4 | Implementasi Sistem | | | ✓ | ✓ | | |
| 5 | Pengujian dan Analisis Hasil | | | | ✓ | ✓ | |
| 6 | Penyusunan Laporan/Buku TA | | | | | ✓ | ✓ |

---

*Catatan: Dokumen ini merupakan draf Bab 1 Tugas Akhir — Gemayel Peramana Ginting (1301213540)*
*Program Studi Sarjana Informatika, Fakultas Informatika, Universitas Telkom*
