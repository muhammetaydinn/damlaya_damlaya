# Yatırımın Zamanla Değişimi

Bu Python kodu, belirli bir yatırım stratejisine dayalı olarak zaman içinde yatırımın nasıl değiştiğini görselleştirmek için kullanılır. Kod, farklı vade sürelerinde yapılan yatırımların toplam para miktarı, toplam yatırılmış para miktarı, toplam kar ve toplam kar yüzdesi üzerindeki etkisini gösteren bir grafik oluşturur.

## Gereksinimler

Bu kodun çalışması için Python 3 ve matplotlib kütüphanesinin yüklü olması gerekmektedir.
Kütüphane yüklü değilse, aşağıdaki komutu kullanarak yükleyebilirsiniz:
```bash
pip install matplotlib
```

## Kullanım

1. Kodu çalıştırın: Python yatirim_grafik.py
2. Oluşturulan grafik penceresini gözlemleyin.
3. Grafikteki farklı çizgilerin her biri bir metriği temsil eder:
    - Mavi çizgi: Toplam para miktarı
    - Yeşil çizgi: Toplam yatırılmış para miktarı
    - Kırmızı çizgi: Toplam kar
    - Mor çizgi: Toplam kar yüzdesi
4. Grafikteki eksenler ve çizgiler üzerindeki etiketler size verileri açıklar.

## Değişkenlerin Açıklaması

- ana_para_listesi: Her vade süresi için hesaplanan toplam para miktarını içeren bir liste.
- yatirim_miktari_listesi: Her vade süresi için hesaplanan toplam yatırılmış para miktarını içeren bir liste.
- kar_listesi: Her vade süresi için hesaplanan toplam karı içeren bir liste.
- kar_yuzdesi_listesi: Her vade süresi için hesaplanan toplam kar yüzdesini içeren bir liste.
- ana_para: Anlık hesaplanan toplam para miktarı.
- aylik_yatirim: Her ay yapılan sabit yatırım miktarı.
- faiz_orani: Yıllık faiz oranı.
- ay_versiyonlari: Farklı vade sürelerini içeren bir liste.

