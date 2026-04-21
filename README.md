# 🌐 Clous.cloud — Huawei MaaS Interface

> Huawei ModelArts MaaS servisleri için sade, hızlı ve kullanıma hazır bir sohbet arayüzü.

**Canlı:** [clous.cloud](https://www.clous.cloud)  
**Geliştirici:** Furkan Yiğit

---

## 📁 Proje Yapısı

```
clous/
├── app.py                  # Flask backend — API proxy
├── requirements.txt        # Python bağımlılıkları
├── railway.toml            # Railway deploy konfigürasyonu
└── templates/
    └── index.html          # Tek sayfa frontend (logo + favicon gömülü)
```

---

## ⚙️ Nasıl Çalışır?

```
Tarayıcı → Flask (app.py) → Huawei MaaS API
```

Kullanıcı API bilgilerini frontend'e girer. Flask bu bilgileri alıp Huawei MaaS endpoint'ine proxy olarak iletir. Streaming (Server-Sent Events) ile yanıtlar gerçek zamanlı akar.

---

## 🤖 Desteklenen Modeller

| Model | Tip |
|---|---|
| DeepSeek-V3.2 | Text Generation |
| DeepSeek-V3.1 | Text Generation |
| DeepSeek-V3 | Text Generation |
| GLM-5 | Text Generation |
| GLM-5.1 | Text Generation |
| DeepSeek-R1-0528 | Text Generation |

---

## 🔌 API Bağlantısı

| Alan | Değer |
|---|---|
| **Endpoint** | `https://api-ap-southeast-1.modelarts-maas.com/openai/v1/chat/completions` |
| **Auth** | Bearer Token (Huawei MaaS API Key) |
| **Format** | OpenAI Chat Completions uyumlu |

API Key almak için: Huawei Cloud → ModelArts → MaaS → API Key Management

---

🚀 Deploy — Cloud
Bu repoyu GitHub üzerinden bağlayarak bir Web Service oluştur.

Aşağıdaki yapılandırmayı kullan:

Root Directory: clous

Build Command: pip install -r requirements.txt

Start Command: python app.py

Projenin canlı versiyonuna bu adresten ulaşabilirsin:
👉 https://clous-cloud-furkan-yigit.onrender.com/

Environment variable gerekmez — PORT ve HOST ayarları kod içerisinde otomatik olarak yapılandırılmıştır.
---

## 💻 Lokal Geliştirme

```bash
# Bağımlılıkları yükle
pip install -r requirements.txt

# Uygulamayı başlat
python app.py

# Tarayıcıda aç
http://localhost:5000
```

---

## 🗂️ Dosya Detayları

### `app.py`
Flask backend. Tek görevi: frontend'den gelen isteği alıp Huawei MaaS API'sine iletmek ve streaming yanıtı tarayıcıya aktarmak.

- `GET /` → `templates/index.html` render eder
- `POST /api/chat` → Huawei MaaS'a proxy, SSE stream döner

### `templates/index.html`
Tüm frontend tek dosyada. Harici bağımlılık yok (logo ve favicon base64 gömülü).

- **Sol panel:** Endpoint URL, API Key, Model seçimi, Temperature, Max Tokens, Sistem Promptu
- **Sağ panel:** Sohbet ekranı, hızlı başlangıç butonları, mesaj geçmişi
- **Topbar:** Dışa Aktar, Kopyala, Temizle

### `requirements.txt`
```
flask>=3.0.0
requests>=2.31.0
gunicorn>=21.2.0
```

### `railway.toml`
Railway'e başlatma komutunu söyler: `python app.py`

---

## 📝 Lisans

MIT — Furkan Yiğit  Cloud Solution Architect / Clous Cloud

<img width="1222" height="404" alt="clous2tr" src="https://github.com/user-attachments/assets/52e03cc1-ba7f-4bb6-87ef-0fb440c4a453" />

