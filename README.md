# todo-cli
Görevleri JSON doyasında saklayan, program kapanıp açılsa bile listeyi kaybetmeyen basit bir terminal yapılacaklar listesi.

## Nasıl çalıştırılır

    python3 ekle.py # listeye "kitap oku" görevini ekler
    python3 tamamla.py # listedeki ilk görevi tamamlandı yapar

Görevler "gorevler.json" dosyasında saklanır. Dosya yoksa program boş bir listeyle başlar ve dosyayı kendisi oluşturur.

"json_deneme.py" bir öğrenme dosyasıdır: çalıştırınca listeyi 3 örnek görevle sıfırlar.

## Ne öğrendim

- Programın içindeki liste kapanınca silinir. Listeyi "json.dump" ile dosyaya yazıp "json.load" ile geri okuyunca görevler kalıcı olur.
- Uygulama ilk açıldığında dosya henüz yok. "try/except FileNotFoundError" ile program çökmek yerine boş bir listeyle başlıyor.
- "gorevler.json" bir veri dosyası kod değil. Bu yüzden ".gitignore"'a ekledim, repoyu indirenler kendi boş listesiyle başlıyor.
