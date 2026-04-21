"""
Clous.cloud — Huawei MaaS Web Interface
"""

from flask import Flask, render_template, request, Response, jsonify
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    endpoint = data.get('endpoint', '').strip().rstrip('/')
    api_key  = data.get('api_key', '')
    model    = data.get('model', '')
    messages = data.get('messages', [])
    temperature  = float(data.get('temperature', 0.7))
    max_tokens   = int(data.get('max_tokens', 2048))
    system_prompt = data.get('system_prompt', '')
    stream = data.get('stream', True)

    if not endpoint or not api_key or not model:
        return jsonify({"error": "Endpoint, API Key ve Model gerekli"}), 400

    # ── URL: kullanıcının girdiği endpoint'i olduğu gibi kullan ──
    # Eğer zaten /chat/completions ile bitiyorsa dokunma,
    # bitmiyor ama /v1 varsa sadece /chat/completions ekle,
    # hiçbiri yoksa tam path ekle.
    if endpoint.endswith('/chat/completions'):
        url = endpoint
    elif '/v1' in endpoint:
        url = endpoint + '/chat/completions'
    else:
        url = endpoint + '/v1/chat/completions'

    # ── Mesajlar ──
    full_messages = []
    if system_prompt:
        full_messages.append({"role": "system", "content": system_prompt})
    full_messages.extend(messages)

    # ── Payload ──
    payload = {
        "model": model,
        "messages": full_messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": stream
    }
    body_str = json.dumps(payload)

    # ── Headers ──
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # ── İstek ──
    try:
        if stream:
            def generate():
                with requests.post(
                    url, headers=headers,
                    data=body_str.encode('utf-8'),
                    stream=True, timeout=90
                ) as r:
                    if r.status_code != 200:
                        err = r.text[:600]
                        yield f"data: {json.dumps({'error': f'API {r.status_code}: {err}'})}\n\n"
                        return
                    for line in r.iter_lines():
                        if line:
                            yield f"{line.decode('utf-8')}\n\n"

            return Response(
                generate(),
                mimetype='text/event-stream',
                headers={'Cache-Control': 'no-cache', 'X-Accel-Buffering': 'no'}
            )
        else:
            r = requests.post(url, headers=headers, data=body_str.encode('utf-8'), timeout=90)
            return jsonify(r.json())

    except requests.exceptions.Timeout:
        return jsonify({"error": "İstek zaman aşımına uğradı (90s)"}), 504
    except requests.exceptions.ConnectionError as e:
        return jsonify({"error": f"Bağlantı hatası: {str(e)}"}), 503
    except Exception as e:
        return jsonify({"error": str(e)}), 500


import os  # Dosyanın en başında os kütüphanesinin olduğundan emin ol

if __name__ == '__main__':
    print()
    print("  ██████╗██╗      ██████╗ ██╗   ██╗███████╗")
    print(" ██╔════╝██║     ██╔═══██╗██║   ██║██╔════╝")
    print(" ██║     ██║     ██║   ██║██║   ██║███████╗")
    print(" ██║     ██║     ██║   ██║██║   ██║╚════██║")
    print(" ╚██████╗███████╗╚██████╔╝╚██████╔╝███████║")
    print("  ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝")
    print()
    print("  Clous.cloud — Huawei MaaS Interface")
    
    # Render'ın atadığı PORT'u alıyoruz, bulamazsak 5000'i kullanıyoruz.
    port = int(os.environ.get("PORT", 5000))
    print(f"  → Running on port: {port}")
    print()

    # host="0.0.0.0" eklemezsen Render trafiği içeri alamaz!
    app.run(debug=True, host="0.0.0.0", port=port, threaded=True)
