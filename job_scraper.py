import datetime
import csv
import os

jobs_to_analyze = [
    {"title": "ERP Uzmanı", "description": "SQL, süreç analizi, mühendislik."},
    {"title": "Veri Analisti", "description": "İleri SQL, Power BI, Excel."},
    {"title": "E-Ticaret Planlama", "description": "ERP, KPI, Excel, stok planlama."}
]

def analyze_and_save():
    keywords = ["SQL", "Excel", "Power BI", "ERP", "Python", "Mühendislik"]
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    
    # Dosya yoksa başlıkları ekle
    file_exists = os.path.isfile('market_report.csv')
    
    with open('market_report.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Tarih', 'Pozisyon', 'Bulunan Yetenekler'])
            
        for job in jobs_to_analyze:
            found = [skill for skill in keywords if skill.lower() in job['description'].lower()]
            writer.writerow([date_str, job['title'], ', '.join(found)])
    
    print("✅ Analiz tamamlandı ve market_report.csv dosyasına kaydedildi.")

if __name__ == "__main__":
    analyze_and_save()
