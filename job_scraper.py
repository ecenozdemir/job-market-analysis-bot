import datetime
import csv
import os

jobs_to_analyze = [
    {"title": "ERP Uzmanı", "description": "Tekstil fabrikamızda süreçleri yönetecek, SQL bilen uzman."}, # Eşleşecek!
    {"title": "Veri Analisti", "description": "İleri SQL, Power BI, Excel."},
    {"title": "E-Ticaret Planlama", "description": "ERP, KPI, Excel, stok planlama."}
]

def analyze_and_save():
    keywords = ["SQL", "Excel", "Power BI", "ERP", "Python", "Mühendislik", "Tekstil"]
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    alerts = [] # Alarmları burada toplayacağız
    
    file_exists = os.path.isfile('market_report.csv')
    
    with open('market_report.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Tarih', 'Pozisyon', 'Bulunan Yetenekler'])
            
        for job in jobs_to_analyze:
            desc = job['description'].lower()
            found = [skill for skill in keywords if skill.lower() in desc]
            writer.writerow([date_str, job['title'], ', '.join(found)])
            
            # ALARM MEKANİZMASI: ERP ve Tekstil aynı anda geçiyor mu?
            if "erp" in desc and "tekstil" in desc:
                alerts.append(f"🔥 DİKKAT: {job['title']} ilanı tam sana göre (ERP + Tekstil içeriği)!")
    
    # Sonuçları ekrana bas (GitHub Actions loglarında görünecek)
    if alerts:
        print("\n" + "!"*30)
        for alert in alerts:
            print(alert)
        print("!"*30 + "\n")
    
    print("✅ Analiz tamamlandı ve kaydedildi.")

if __name__ == "__main__":
    analyze_and_save()
