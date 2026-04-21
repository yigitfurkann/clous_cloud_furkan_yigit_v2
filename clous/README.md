# Clous.cloud.furkan.yigit

Huawei MaaS (ModelArts as a Service) API için Python + Flask tabanlı web arayüzü.

---

## Kurulum

```bash
pip install -r requirements.txt
python app.py
```

Tarayıcıda aç: **http://localhost:5000**

---

## Huawei MaaS API Bilgileri Nereden Alınır?

1. **Huawei Cloud Console** → ModelArts → MaaS → Model Deployment
2. Dağıtılan modeli seç → **API Endpoint** URL'sini kopyala
3. **IAM** → Kullanıcı → Güvenlik → **API Key** oluştur

### Endpoint Format
```
https://maas-api.ap-southeast-3.myhuaweicloud.com/v1/{proje_id}/{model_adi}
```

Uygulama otomatik olarak `/v1/chat/completions` ekler (OpenAI uyumlu format).

---

## Desteklenen Modeller

| Model | Açıklama |
|-------|----------|
| `deepseek-v3` | DeepSeek V3 |
| `deepseek-r1` | DeepSeek R1 (reasoning) |
| `glm-4` | GLM-4 |
| `Qwen2.5-72B-Instruct` | Qwen 2.5 72B |
| Özel | Kendi model adını gir |

---

## Proje Yapısı

```
clous/
├── app.py              # Flask backend
├── requirements.txt
└── templates/
    └── index.html      # Web arayüzü
```
