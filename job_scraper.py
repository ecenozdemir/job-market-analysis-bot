import datetime
import csv
import os
import feedparser

def analyze_real_jobs():
    # Arama terimlerini genişlettik: ERP, Data Analyst ve SQL bir arada
    search_query = "erp+OR+sql+OR+data+analyst"
    rss_url = f"https://www.upwork.com/ab/feed/jobs/rss?q={search_query}&sort=recency" 
    
    feed = feedparser.parse(rss_url)
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    
    # Aradığımız kritik yetenek listesini büyüttük
    keywords = ["SQL", "Excel", "Power BI", "ERP", "Python", "Tableau", "Reporting", "Tekstil", "Textile"]
    alerts = []
    
    file_exists = os.path.isfile('market_report.csv')
    
    with open('market_report.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Tarih', 'Pozisyon', 'Bulunan Yetenekler'])
            
        for entry in feed.entries:
            title = entry.title
            desc = entry.description.lower()
            found = [skill for skill in keywords if skill.lower() in desc]
            
            if found: # Sadece içinde anahtar kelimelerimiz geçen ilanları kaydet (Gürültüyü azaltır)
                writer.writerow([date_str, title, ', '.join(found)])
            
            # KRİTİK ALARM: ERP + Tekstil veya SQL + Data Analyst kombinasyonları
            if ("erp" in desc and ("textile" in desc or "manufacturing" in desc)):
                alerts.append(f"🎯 **SEKTÖREL FIRSAT:** {title}")
            elif ("sql" in desc and "python" in desc):
                alerts.append(f"🐍 **VERİ ANALİZİ FIRSATI:** {title}")

    # GitHub Summary
    if 'GITHUB_STEP_SUMMARY' in os.environ:
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
            summary.write(f"## 🌍 Genişletilmiş Piyasa Analizi ({date_str})\n")
            summary.write(f"İncelenen yeni ilan sayısı: {len(feed.entries)}\n\n")
            if alerts:
                summary.write("### 🚨 RADARIMIZA TAKILANLAR!\n")
                for alert in alerts:
                    summary.write(f"- {alert}\n")
            else:
                summary.write("✅ Kriterlerine tam uyan özel bir alarm tetiklenmedi, ama tüm veriler CSV'ye işlendi.\n")

    print(f"✅ {len(feed.entries)} ilan tarandı.")

if __name__ == "__main__":
    analyze_real_jobs()
