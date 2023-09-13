<h4>1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</h4>
<p>- Membuat direktori lokal untuk project <br>
- Inisiasi git <br>
- Buat dan aktifkan virtual environment. <br>
- Menginstall dependencies. <br>
- Start project django <br>
- Mengatur konfigurasi Allowed hosts pada settings.py <br>
- Membuat aplikasi main dan menambahkannya ke daftar proyek <br>
- Membuat direktori untuk template dan menambahkan file template yaitu main.html <br>
- Mengisi main.html sesuai kebutuhan <br>
- Membuat model dengan nama Item dengan atribut nama, amount dan description <br>
- Migrasi model <br>
- Membuat fungi show_main pada berkas views.py dan mengisi data yang akan ditampilkan <br>
- Konfigurasi routing URL aplikasi main dengan menambahkan fungsi show_main ke list urlpatterns pada urls.py <br>
- Konfigurasi routing URL proyek <br>
- Buat repositori baru di github untuk proyek <br>
- Setelah keluar dari virtual environment, lakukan add dan commit pada direktori proyek <br>
- Buat branch utama baru, hubungkan direktori lokal dengan repositori github, lalu push</p>

<h4>2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan<br>antara urls.py, views.py, models.py, dan berkas html.</h4>

![img](mvt.png)

<p>urls.py akan meneruskan request ke views.py, lalu views.py akan mengambil data yang diperlukan dari models.py lalu ditampilkan melalui berkas .html</p>

<h4>3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?</h4>
<p>Virtual environment digunakan untuk menghindari konflik dependencies dari proyek berbeda. Virtual environment mengisolasi package dan dependencies dari aplikasi<br>
Kita tetap bisa membuat aplikasi django tanpa virtual environment. Namun, jika kita mengerjakan lebih dari satu proyek dengan versi django yang berbeda, maka akan terjadi konflik akibat perbedaan versi django pada perangkat lokal.</p>

<h4>4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.</h4>
<p>MVC, MVT dan MVVM merupakan design pattern yang digunakan dalam pemrograman berbasis platform.<br>
<b>MVC (Movdel-View-Controller)</b><br>
- Model: Mewakili data dan logika bisnis<br>
- View: Menampilkan data kepada pengguna<br>
- Controller: Perantara antara view dan model, mengelola interaksi pengguna<br>
<b>MVT (Model-View-Template)</b><br>
- Model: Mewakili data<br>
- View: Bagian logika bisnis, menampilkan template kepada pengguna<br>
- Template: Tampilan html yang dapat disesuaikan dengan input pada model<br>
<b>MVVM (Model-View-ViewModel)</b><br>
- Model: Mewakili data<br>
- View: Menampilkan data kepada pengguna<br>
- ViewModel: Mengubah data dari Model menjadi format yang lebih sesuai untuk tampilan. <br>
ViewModel juga menangani perintah dari View dan memperbarui Model jika diperlukan.<br></p>
