import datetime

# Analiz edilecek gerçek ilan metinleri 
jobs_to_analyze = [
    {
        "title": "ERP Uzmanı",
        "description": "Üniversitelerin mühendislik bölümlerinden mezun, Süreç analizi ve raporlama yapabilen, SQL ve HANA teitabanı bilen."
    },
    {
        "title": "Veri Analisti",
        "description": "İleri derecede SQL bilgisi ve tecrübesi olan, Power BI ve Excel bilen, veri modelleme yapabilen."
    },
    {
        "title": "E-Ticaret Planlama",
        "description": "E-ticaret ERP sistemlerinde yetkin, stok planlama ve KPI takibi yapabilen, Excel bilen."
    }
]

def analyze_market():
    keywords = ["SQL", "Excel", "Power BI", "ERP", "Python", "Mühendislik", "İngilizce"]
    print(f"--- PİYASA ANALİZ RAPORU ({datetime.date.today()}) ---")
    
    for job in jobs_to_analyze:
        found = [skill for skill in keywords if skill.lower() in job['description'].lower()]
        print(f"📍 Pozisyon: {job['title']}")
        print(f"🔎 Aranan Kritik Yetenekler: {', '.join(found)}")
        print("-" * 30)

if __name__ == "__main__":
    analyze_market()
