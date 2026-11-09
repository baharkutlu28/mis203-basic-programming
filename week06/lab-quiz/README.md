## Kulüp Öğrenci Kayıt Sistemi

Bu Python çalışmasında kulübün branşları bir tuple içinde, öğrenci kayıtları ise iç içe listeler içinde tutulur. Her öğrenci kaydı `[öğrenci_adı, [branş]]` biçimindedir.

### Kullanılan işlemler

- `ana_branslar` tuple’ı: Yazılım, Tasarım ve Pazarlama branşlarını tutar.
- `tum_ogrenciler` listesi: Öğrenci kayıtlarını saklar.
- `strip()`: İsimlerin başındaki ve sonundaki boşlukları temizler.
- `insert()` ve `len()`: Başkan kaydını listenin başına ekler ve toplam kayıt sayısını yazdırır.
- `remove()` ve `pop()`: Bir öğrenciyi adıyla siler ve listenin sonundaki öğrenciyi çıkarır.
- `sorted()` ve `sort()`: Öğrenci kayıtlarını önce geçici bir kopyada, ardından ana listede alfabetik sıralar.

