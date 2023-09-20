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
<h3>TUGAS 3</h3>
<h4>1. Apa perbedaan antara form POST dan form GET dalam Django?</h4>
<p>Dalam <b>POST</b>, browser mengumpulkan data dari form, me-<i>encode</i> datanya, mengirimkan datanya ke server, lalu menerima response. Oleh karena itu, POST biasanya digunakan untuk operasi yang mengubah atau membuat data di server. <br>
<b>GET</b> disisi lain, mengumpulkan data yang disubmisi ke dalam string dan menggunakannya untuk membuat URL. URL-nya mengandung alamat ke mana data harus dikirim, termasuk <i>keys</i> dan <i>value</i> dari data. Oleh karena itu, GET cocok untuk operasi <i>read-only</i>.</p> <br>

<h4>2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?</h4>
<p>XML menyajikan data dalam bentuk elemen yang diapit oleh <i>tags</i> dan dengan struktur hierarki<br>
JSON menyajikan data dalam bentuk pasangan <i>key-value</i><br>
HTML digunakan untuk menampilkan halaman web dari request</p> <br>
<h4>3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?</h4>
<p>Karena JSON memiliki struktur yang simpel sehingga mudah dibaca, ditulis dan dipahami. JSON juga dapat diubah ke objek JavaScript sehingga lebih nyaman untuk web developer yang menggunakan JavaScript.</p> <br>
<h4>4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</h4>
<p>- Membuat folder baru bernama templates lalu buat file dengan nama base.html pada folder tersebut.<br>
- Isi file sesuai dengan yang ada di tutorial<br>
- Tambahkan base.html sebagai template pada settings.py di subdirektori project_inventory <br>
- Ubah main.html agar meng-extend base.html<br>
- Buat berkas baru pada direktori main dengan nama forms.py <br>
- Atur isi forms.py dengan model yang akan digunakan beserta field yang akan diisi pada form <br>
- Buat fungsi baru bernama create_product untuk menghasilkan form yang dapat menambahkan data item secara otomatis ketika data di submit.<br>
- Tambahkan items pada fungsi show_main<br>
- import fungsi create_product pada urls.py di main, dan tambahkan path urlnya<br>
- Buat berkas bernama create_product.html pada main/templates dan sesuaikan isinya dengan tutorial<br>
- Tambahkan kode yang ada di tutorial pada main.html. Sesuaikan atribut-atributnya dengan model yang digunakan (item)<br>
- import HttpResponse dan serializers pada main/views.py lalu buat fungsi bernama show_xml<br>
- Tambahkan data = Item.objects.all() pada fungsi lalu return HttpResponse dalam bentuk xml menggunakan serializer<br>
- Lakukan hal yang sama untuk JSON<br>
- Buat fungsi baru bernama show_xml_by_id dan tambahkan parameter id<br>
- Tambahkan data = Product.objects.filter(pk=id) pada fungsi lalu return HttpResponse dala bentuk xml menggunakan serializer<br>
-Lakukan hal serupa untuk JSON</p><br>
<h4>5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.</h4>

![Alt text](image.png)

![Alt text](image-1.png)

![Alt text](image-2.png)

![Alt text](image-3.png)

![Alt text](image-4.png)