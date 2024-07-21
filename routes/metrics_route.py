from quart import Blueprint
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

metrics_bp = Blueprint('metrics_bp', __name__)

@metrics_bp.route('/metrics')
async def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}
