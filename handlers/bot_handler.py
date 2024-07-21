from quart import request, jsonify
from botbuilder.schema import Activity
from adapters.bot_adapter import adapter
from services.bot_service import MyBot

bot = MyBot()

async def messages():
    if 'application/json' in request.headers['Content-Type']:
        body = await request.get_json()
    else:
        return jsonify({'error': 'Unsupported content type'}), 400

    activity = Activity().deserialize(body)
    auth_header = request.headers['Authorization'] if 'Authorization' in request.headers else ''
    
    async def aux_func(turn_context):
        await bot.on_turn(turn_context)

    await adapter.process_activity(activity, auth_header, aux_func)
    return jsonify({'status': 'ok'})
