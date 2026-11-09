ana_branşlar = ( "Yazılım", "Tasarım", "Pazarlama")
print(ana_branşlar)

tüm_öğrenciler = []

ad1 = "Ahmet ".strip()
tüm_öğrenciler.append([ad1,[ "Yazılım"]])

ad2 =  "Ayşe".strip()
tüm_öğrenciler.append([ad2,[ "Tasarım"]])

ad3 = "Mehmet".strip()
tüm_öğrenciler.append([ad3,["Pazarlama"]])

tüm_öğrenciler.insert(0,["Başkan",["Yazılım"]])
print("Toplam Kayıtlı Öğrenci Sayısı:",len(tüm_öğrenciler))

tüm_öğrenciler.remove(["Ayşe",["Tasarım"]])

çıkan_öğrenci = tüm_öğrenciler.pop()
print(f"Sistemden en son çıkan öğrenci:[{çıkan_öğrenci[0]}]")

tüm_öğrenciler.append(["Burak Tan",["Tasarım"]])
sıralı_kopya = sorted(tüm_öğrenciler, key=lambda öğrenci: öğrenci[0])
print("Alfabetik geçici kopya:",sıralı_kopya)
print("Orijinal liste:",tüm_öğrenciler)

tüm_öğrenciler.sort(key=lambda öğrenci: öğrenci[0])
print("Kalıcı olarak sıralanmış liste:",tüm_öğrenciler)