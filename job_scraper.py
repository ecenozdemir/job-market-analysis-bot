import datetime
import csv
import os

# Test için 'tekstil' kelimesini eklediğimizden emin olalım
jobs_to_analyze = [
    {"title": "ERP Uzmanı", "description": "Tekstil sektöründe deneyimli, ERP süreçlerini yönetecek uzman."},
    {"title": "Veri Analisti", "description": "SQL ve Power BI bilen analist."},
    {"title": "E-Ticaret Planlama", "description": "ERP ve stok yönetimi."}
]

def analyze_and_save():
    keywords = ["SQL", "Excel", "Power BI", "ERP", "Python", "Tekstil"]
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    alerts = []
    
    file_exists = os.path.isfile('market_report.csv')
    
    with open('market_report.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Tarih', 'Pozisyon', 'Bulunan Yetenekler'])
            
        for job in jobs_to_analyze:
            desc = job['description'].lower()
            found = [skill for skill in keywords if skill.lower() in desc]
            writer.writerow([date_str, job['title'], ', '.join(found)])
            
            # ALARM: Kelimeleri kontrol et
            if "erp" in desc and "tekstil" in desc:
                alerts.append(f"🔥 **{job['title']}** ilanı tam sana göre (ERP + Tekstil içeriği)!")
    
    # GITHUB ÖZET SAYFASINA YAZDIRMA (Burası sihirli kısım)
    if alerts and 'GITHUB_STEP_SUMMARY' in os.environ:
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
            summary.write("## 🚨 KRİTİK İŞ ALARMI!\n")
            for alert in alerts:
                summary.write(f"{alert}\n")

    print("✅ Analiz tamamlandı ve kaydedildi.")

if __name__ == "__main__":
    analyze_and_save()
