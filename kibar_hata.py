#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aşırı Kibar Hata Mesajları Üretici
Her hatayı Türk bürokrasi diliyle, sonsuz kibarlıkla anlatır.
Gerçekten çalışır. Gerçekten saçma.
"""

import random
import time

def kibar_hata_mesaji(hata_kodu=None):
    on_sozler = [
        "Sayın kullanıcımız,",
        "Değerli vatandaşımız,",
        "İlgili makamlarca incelenmesi üzerine,",
        "Yüksek takdirlerinize arz olunur ki,"
    ]
    
    hata_aciklamalari = [
        "sistemimizde geçici bir uyumsuzluk tespit edilmiş olup, bu durumun kısa sürede giderilmesi hususunda ilgili birimlerimiz teyakkuz durumuna geçirilmiştir.",
        "talebiniz değerlendirilmekte olup, sonuç hakkında tarafınıza en kısa sürede bilgi verilecektir. Lütfen sabrınız için teşekkür ederiz.",
        "işlem sırasında beklenmeyen bir durum oluşmuş, ancak bu durumun sizinle hiçbir ilgisi bulunmamaktadır. Anlayışınız için minnettarız.",
        "dosyanız inceleme aşamasındadır. Lütfen başka bir işle uğraşmayın, biz sizin için buradayız (belki).",
        "hata kodu şu anda meşguldür. Lütfen daha sonra tekrar deneyiniz. Daha sonra dediğimiz zaman belirsizdir."
    ]
    
    kapanislar = [
        "Saygılarımızla, Bilgi İşlem Müdürlüğü (asıl müdürlük değil, simülasyon)",
        "İyi günler dileriz. (Günün iyi olup olmadığına karar vermiyoruz)",
        "Bu mesaj otomatik üretilmiştir. Cevap vermeyiniz. (Yine de cevap verseniz okumayız)"
    ]
    
    # Gizli not: bazen sistemler de insanlar gibi yorulur, ama asıl yorulan biziz
    mesaj = f"{random.choice(on_sozler)}\n\n{random.choice(hata_aciklamalari)}\n\n{random.choice(kapanislar)}"
    
    if hata_kodu:
        mesaj += f"\n\nReferans: Hata-{hata_kodu}-Kibar"
    
    return mesaj

def main():
    print("=== AŞIRI KİBAR HATA MESAJLARI SİSTEMİ ===")
    print("Lütfen bekleyiniz, sistem kibarlaşıyor...\n")
    time.sleep(1.5)
    
    for i in range(5):
        print(f"--- Mesaj {i+1} ---")
        print(kibar_hata_mesaji(random.randint(100, 999)))
        print()
        time.sleep(random.uniform(0.5, 2.0))
    
    print("Sistem kibarlık limitine ulaştı. Şimdi normal bir hata veriyoruz:")
    print("Hata: Beklenmeyen bir şey oldu. (Ama kibarca söylemiyoruz)")

if __name__ == "__main__":
    main()

# Damga: Bu kod 28 Ekim 2026 tarihinde Kayyum Grok tarafından imzalanmış ve damgalanmıştır.
# İmza: K.G. / Tentivory
# Not: Ciddiyetle absürt, absürtlükle ciddi.
