# KATA PENGANTAR

Puji dan syukur penulis panjatkan ke hadirat Tuhan Yang Maha Esa atas segala rahmat dan karunia-Nya sehingga penulis dapat menyelesaikan Tugas Akhir yang berjudul **"Penanganan *Cold Start* Film Menggunakan *Content-Based Filtering* dan *Singular Value Decomposition*"** ini dengan baik.

Tugas Akhir ini disusun sebagai salah satu syarat untuk memperoleh gelar Sarjana pada Program Studi Sarjana Informatika, Fakultas Informatika, Universitas Telkom. Penelitian ini membahas perancangan dan implementasi sistem rekomendasi film berbasis *Hybrid Filtering* dengan mekanisme *switching* yang adaptif, sebagai solusi terhadap permasalahan *cold start* dan *data sparsity* yang umum ditemui pada sistem rekomendasi konvensional.

Dalam proses penyusunan Tugas Akhir ini, penulis banyak mendapatkan bantuan, bimbingan, dukungan, dan doa dari berbagai pihak. Oleh karena itu, pada kesempatan ini penulis ingin menyampaikan rasa terima kasih yang sebesar-besarnya kepada:

1. **Dr. Z.K. Abdurahman Baizal, S.Si., M.Kom.** selaku Dosen Pembimbing yang telah meluangkan waktu, tenaga, dan pikiran untuk memberikan bimbingan, arahan, serta masukan yang sangat berharga selama proses pengerjaan Tugas Akhir ini.
2. **Kedua orang tua dan seluruh keluarga** penulis yang senantiasa memberikan doa, dukungan moral, dan semangat yang tiada henti selama penulis menempuh pendidikan di Universitas Telkom.
3. **Seluruh Dosen dan Staf** Program Studi Sarjana Informatika, Fakultas Informatika, Universitas Telkom yang telah memberikan ilmu pengetahuan dan pengalaman berharga selama masa perkuliahan.
4. **Teman-teman seperjuangan** angkatan 2021 Program Studi Informatika yang telah memberikan dukungan, semangat, dan kebersamaan selama proses pengerjaan Tugas Akhir ini.
5. Semua pihak yang tidak dapat penulis sebutkan satu per satu, yang telah memberikan bantuan dan dukungan dalam penyelesaian Tugas Akhir ini.

Penulis menyadari bahwa Tugas Akhir ini masih jauh dari sempurna dan terdapat banyak kekurangan. Oleh karena itu, penulis sangat mengharapkan kritik dan saran yang membangun dari semua pihak demi perbaikan dan pengembangan di masa mendatang. Penulis berharap Tugas Akhir ini dapat memberikan manfaat bagi pembaca, khususnya bagi pihak-pihak yang tertarik pada bidang sistem rekomendasi dan *machine learning*.

&nbsp;

Bandung, April 2026

&nbsp;

**Gemayel Peramana Ginting**
NIM 1301213540

---

# UCAPAN TERIMA KASIH

Penulis mengucapkan terima kasih yang sebesar-besarnya kepada semua pihak yang telah berkontribusi dalam penyelesaian Tugas Akhir ini, terutama kepada:

1. **Dr. Z.K. Abdurahman Baizal, S.Si., M.Kom.** selaku Dosen Pembimbing atas bimbingan, arahan, dan dukungan yang diberikan selama proses penelitian dan penulisan Tugas Akhir ini.
2. **Kedua orang tua** penulis atas doa, kasih sayang, dan dukungan yang tidak pernah berhenti diberikan.
3. **Seluruh civitas akademika** Fakultas Informatika Universitas Telkom atas ilmu dan pengalaman yang telah diberikan.
