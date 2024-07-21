from quart import Blueprint, request, jsonify
from handlers.bot_handler import messages
import time
from services.metrics import REQUEST_COUNT, REQUEST_LATENCY

messages_bp = Blueprint('messages_bp', __name__)

@messages_bp.before_request
async def before_request():
    request.start_time = time.time()

@messages_bp.after_request
async def after_request(response):
    request_latency = time.time() - request.start_time
    endpoint = request.endpoint or 'unknown'
    REQUEST_LATENCY.labels(endpoint=endpoint).observe(request_latency)
    REQUEST_COUNT.labels(endpoint=endpoint, method=request.method, status_code=response.status_code).inc()
    return response

@messages_bp.route('/api/messages', methods=['POST'])
async def bot_messages():
    try:
        response = await messages()
        return response
    except Exception as e:
        print(e)
        return jsonify({'error': 'Internal Server Error'}), 500
