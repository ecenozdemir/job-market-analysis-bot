-- Bu tablo ilanların genel bilgilerini tutar
CREATE TABLE jobs (
    id INTEGER PRIMARY KEY,
    title TEXT, -- İlan Başlığı (Örn: ERP Uzmanı)
    company TEXT, -- Şirket Adı
    location TEXT, -- Şehir
    posted_date DATE -- İlanın tarihi
);

-- Bu tablo ilanlarda istenen teknik yetenekleri tutar
CREATE TABLE skills (
    id INTEGER PRIMARY KEY,
    job_id INTEGER,
    skill_name TEXT, -- SQL, Excel, Python vb.
    importance TEXT, -- Zorunlu mu yoksa tercih mi?
    FOREIGN KEY (job_id) REFERENCES jobs(id)
);
