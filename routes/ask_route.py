from quart import Blueprint, request, jsonify
from services.chat_service import get_chat_response, clear_chat_history, set_user_language, user_languages
import time
from services.metrics import REQUEST_COUNT, REQUEST_LATENCY
from services.translation_service import translate_text

ask_bp = Blueprint('ask_bp', __name__)

@ask_bp.before_request
async def before_request():
    request.start_time = time.time()

@ask_bp.after_request
async def after_request(response):
    request_latency = time.time() - request.start_time
    endpoint = request.endpoint or 'unknown'
    REQUEST_LATENCY.labels(endpoint=endpoint).observe(request_latency)
    REQUEST_COUNT.labels(endpoint=endpoint, method=request.method, status_code=response.status_code).inc()
    return response

@ask_bp.route('/api/ask', methods=['POST'])
async def ask():
    data = await request.get_json()
    question = data.get('question')
    user_id = data.get('user_id')

    if not question or not user_id:
        REQUEST_COUNT.labels(endpoint='/api/ask', method='POST', status_code=400).inc()
        return jsonify({'error': 'Soru veya kullanıcı ID\'si sağlanmadı'}), 400

    if user_id not in user_languages:
        user_languages[user_id] = 'tr'

    if question.strip().lower() == "/clean":
        clear_chat_history(user_id)
        response_message = "Sohbet geçmişi temizlendi. Yeni bir konuşma başlatabilirsiniz."
        if user_languages[user_id] != 'tr':
            response_message = translate_text(response_message, user_languages[user_id])
        REQUEST_COUNT.labels(endpoint='/api/ask', method='POST', status_code=200).inc()
        return jsonify({'answer': response_message})

    if question.startswith("/language"):
        _, language = question.split()
        set_user_language(user_id, language)
        response_message = f"Dil **{language}** olarak ayarlandı"
        if language != 'tr':
            response_message = translate_text(response_message, language)
        REQUEST_COUNT.labels(endpoint='/api/ask', method='POST', status_code=200).inc()
        return jsonify({'answer': response_message})

    try:
        response_content = get_chat_response(user_id, "Unknown User", question)
        REQUEST_LATENCY.labels(endpoint='/api/ask').observe(time.time() - request.start_time)
        REQUEST_COUNT.labels(endpoint='/api/ask', method='POST', status_code=200).inc()
        return jsonify({'answer': response_content})
    except Exception as e:
        print(e)
        REQUEST_COUNT.labels(endpoint='/api/ask', method='POST', status_code=500).inc()
        return jsonify({'error': 'Sunucu Hatası'}), 500
