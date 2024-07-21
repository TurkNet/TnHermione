from quart import Quart
from routes.ask_route import ask_bp
from routes.messages_route import messages_bp
from routes.metrics_route import metrics_bp

app = Quart(__name__)

app.register_blueprint(ask_bp)
app.register_blueprint(messages_bp)
app.register_blueprint(metrics_bp)

@app.route('/')
async def home():
    return "I'm Running"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3978)
