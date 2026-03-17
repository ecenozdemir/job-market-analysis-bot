# Bu bizim ilk veri avcısı robotumuzun taslağı
import datetime

def analyze_job(description):
    # İlanın içinde geçen anahtar kelimeleri arar
    keywords = ["SQL", "Excel", "Power BI", "ERP", "Python", "English"]
    found_skills = [skill for skill in keywords if skill.lower() in description.lower()]
    return found_skills

# Örnek bir ilan metni 
sample_job_text = "Firmamızda çalışacak, ileri derecede SQL ve Excel bilen ERP uzmanı arıyoruz."

print(f"Analiz Tarihi: {datetime.datetime.now()}")
print(f"İlanda Bulunan Yetenekler: {analyze_job(sample_job_text)}")
