import matplotlib.pyplot as plt

ana_para_listesi = []
yatirim_miktari_listesi = []
kar_listesi = []
kar_yuzdesi_listesi = []

ana_para = 0
aylik_yatirim = 100
faiz_orani = 0.0125
ay_versiyonlari = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240, 252, 264, 276]

for ay1 in ay_versiyonlari:
    ana_para = 0
    for ay in range(ay1):
        ana_para += aylik_yatirim + ana_para * faiz_orani
    ana_para_listesi.append(ana_para)
    yatirim_miktari_listesi.append(ay1 * aylik_yatirim)
    kar_listesi.append(ana_para - ay1 * aylik_yatirim)
    kar_yuzdesi_listesi.append((ana_para - ay1 * aylik_yatirim) / ana_para)

plt.figure(figsize=(10, 6))

plt.plot(ay_versiyonlari, ana_para_listesi, marker='o', color='b', label='Toplam Para Miktarı')
plt.plot(ay_versiyonlari, yatirim_miktari_listesi, marker='o', color='g', label='Toplam Yatırılmış Para Miktarı')
plt.plot(ay_versiyonlari, kar_listesi, marker='o', color='r', label='Toplam Kar')
plt.plot(ay_versiyonlari, kar_yuzdesi_listesi, marker='o', color='purple', label='Toplam Kar Yüzdesi')

plt.title('Yatırımın Zamanla Değişimi')
plt.xlabel('Ay')
plt.ylabel('Miktar')
plt.legend()

plt.grid(True)
plt.show()
