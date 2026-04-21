# ☁️ Clous-Cloud-Furkan-Yigit. — Huawei MaaS Interface

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/Flask-3.x-black?style=flat-square&logo=flask" />
  <img src="https://img.shields.io/badge/Huawei%20MaaS-API-red?style=flat-square" />
  <img src="https://img.shields.io/badge/Render-Deployed-46E3B7?style=flat-square&logo=render" />
</p>

<p align="center">
  Huawei ModelArts Studio (MaaS) üzerindeki büyük dil modellerini kolayca kullanabileceğiniz, hafif ve şık bir web arayüzü.
</p>

<p align="center">
  🌐 <strong><a href="https://clous-cloud-furkan-yigit.onrender.com/">Canlıyı Deneyin →</a></strong>
</p>

---

## ✨ Özellikler

- **Streaming yanıtlar** — Gerçek zamanlı token akışı, cevaplar yazılırken görüntülenir
- **Çoklu model desteği** — DeepSeek-V3.1-128K, DeepSeek-V3.2, GLM-5, GLM-5.1
- **Sistem promptu** — Modelin davranışını özelleştirin
- **Temperature & Max Tokens** — İstek ayarlarını sürükle-bırak ile kontrol edin
- **Sohbet geçmişi** — Konuşmayı `.txt` olarak dışa aktarın
- **Temiz UI** — Sora + JetBrains Mono ile minimal beyaz tema
- **Ücretsiz dağıtım** — Render.com üzerinde kolayca yayınlanır

---

## 🚀 Başlarken

### 1. Depoyu klonlayın

```bash
git clone https://github.com/yigitfurkann/clous_cloud_furkan_yigit_v2.git
cd clous_cloud_furkan_yigit_v2/clous
```

### 2. Bağımlılıkları yükleyin

```bash
pip install flask requests
```

### 3. Uygulamayı çalıştırın

```bash
python app.py
```

Tarayıcıda `http://localhost:5000` adresini açın.

---

## 🔧 Kullanım

1. **Endpoint URL** — Huawei MaaS konsolundan aldığınız API endpoint adresini girin
2. **API Anahtarı** — MaaS'tan oluşturduğunuz Bearer token'ı yapıştırın
3. **Model** — Kullanmak istediğiniz modeli seçin
4. **Bağlan & Başlat** butonuna tıklayın
5. Sohbete başlayın!

> MaaS API anahtarı ve endpoint için [Huawei ModelArts Studio](https://www.huaweicloud.com/product/modelarts.html) konsoluna giriş yapmanız gerekir.

---

## 📦 Proje Yapısı

```
clous/
├── app.py              # Flask backend — API proxy
└── templates/
    └── index.html      # Tek dosya frontend (HTML + CSS + JS)
```

---

## 🤖 Desteklenen Modeller

| Model | Context | Özellik |
|---|---|---|
| DeepSeek-V3.1-128K | 128K | En güncel, uzun bağlam |
| DeepSeek-V3.2 | 160K | Yüksek verimlilik |
| GLM-5 | 198K | ZHIPU AI genel amaçlı |
| GLM-5.1 | 198K | Kodlama odaklı |

---


---

## 🛠️ Teknolojiler

- **Backend:** Python, Flask
- **Frontend:** Vanilla HTML/CSS/JS (bağımlılık yok)
- **API:** Huawei MaaS OpenAI-uyumlu endpoint
- **Font:** Sora, JetBrains Mono

---

## 📄 Lisans

MIT License — Furkan YİĞİT Cloud Solution Architect | Clous Cloud 

---

<p align="center">
  <a href="https://clous-cloud-furkan-yigit.onrender.com/">clous-cloud-furkan-yigit.onrender.com</a> · Made with ☁️
</p>

## 👨‍💻 Geliştirici

<p align="center">
  Geliştirici ile iletişime geçmek için:<br><br>
  <a href="https://github.com/yigitfurkann">
    <img src="https://img.shields.io/badge/GitHub-yigitfurkann-181717?style=flat-square&logo=github" />
  </a>
</p>
