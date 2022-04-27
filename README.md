# django-blog
django blog for PriviaSec internship approvment

# Kurulum
Projeyi indirdikten sonra proje dizini içerisine sanal ortam kurmamız gerekmektedir.<br>
`pip install virtualenv`<br>
`virtualenv env`<br>
Yaparak sanal ortamımızı oluşturuyoruz.<br><br>
Sanal ortamımızı aktif etmek için:<br> 
Linux & Mac: `source venv/bin/activate`<br>
Windows: `venv\Scripts\activate`<br><br>
Gerekli python kütüphanelerini kurmak için:<br> `pip install -r requirements.txt`<br><br>
Projede veritabanı olarak postgresql kullandığımdan dolayı postgresql indirip proje için bir veritabanı oluşturmanız gerekiyor. <br>
Veritabanı bilgilerini settings.py dosyasındaki `DATABASES={}` kısmında doldurunuz.<br><br>
`python managa.py makemigrations`<br>
`python manage.py migrate`  komutlarıyla projemizin veritabanını oluşturuyoruz.<br><br>
`python manage.py createsuperuser` komutuyla kendimize admin kullanıcısı tanımlıyoruz.<br><br>
`python manage.py runserver` diyerek sunucumuzu çalıştırıyoruz.
