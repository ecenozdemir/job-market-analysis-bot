import datetime
import csv
import os
import feedparser # İnternetten veri çekmek için kütüphanemiz

def analyze_real_jobs():
    # Arama terimi: ERP jobs 
    # Örnek olarak bir RSS kaynağı kullanıyoruz
    rss_url = "https://www.upwork.com/ab/feed/jobs/rss?q=erp+specialist" 
    # Not: Kariyer.net vb. RSS vermediği için Upwork veya Jooble benzeri açık kaynaklar kullanılır.
    
    feed = feedparser.parse(rss_url)
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    keywords = ["SQL", "Excel", "ERP", "Python", "Tekstil", "Textile", "Manufacturing"]
    alerts = []
    
    file_exists = os.path.isfile('market_report.csv')
    
    with open('market_report.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Tarih', 'Pozisyon', 'Bulunan Yetenekler'])
            
        # İnternetten gelen her ilanı tara
        for entry in feed.entries:
            title = entry.title
            desc = entry.description.lower()
            
            found = [skill for skill in keywords if skill.lower() in desc]
            writer.writerow([date_str, title, ', '.join(found)])
            
            # ÖZEL ALARM: Eğer tekstil veya üretimle ilgili bir ERP ilanı bulursa
            if "erp" in desc and ("textile" in desc or "tekstil" in desc or "manufacturing" in desc):
                alerts.append(f"🎯 **GERÇEK FIRSAT:** {title} (Tekstil/Üretim odaklı ERP ilanı!)")

    # GitHub Summary ekranına yazdır
    if 'GITHUB_STEP_SUMMARY' in os.environ:
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
            summary.write(f"## 🌍 Gerçek Zamanlı Analiz ({date_str})\n")
            summary.write(f"Tarama yapılan ilan sayısı: {len(feed.entries)}\n\n")
            if alerts:
                summary.write("### 🚨 KRİTİK ALARMLAR!\n")
                for alert in alerts:
                    summary.write(f"- {alert}\n")
            else:
                summary.write("✅ Bugün kriterlerine tam uyan yeni bir global ilan bulunamadı.\n")

    print(f"✅ {len(feed.entries)} adet gerçek ilan analiz edildi.")

if __name__ == "__main__":
    analyze_real_jobs()
