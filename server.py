import os
import json
import logging
from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='static')
CORS(app)  # Enable CORS for all routes

# Datadog API endpoints
DATADOG_LOGS_ENDPOINT = "https://http-intake.logs.datadoghq.com/api/v2/logs"
DATADOG_METRICS_ENDPOINT = "https://api.datadoghq.com/api/v2/series"

# Get API key from environment variable
def get_datadog_api_key():
    api_key = os.environ.get("DD_API_KEY")
    if not api_key:
        logger.warning("DD_API_KEY environment variable not set")
        return None
    return api_key

@app.route('/proxy/logs', methods=['POST'])
def proxy_logs():
    """Proxy logs to Datadog"""
    api_key = get_datadog_api_key()
    if not api_key:
        return jsonify({"error": "Datadog API key not configured"}), 500
    
    try:
        logs_data = request.json
        
        headers = {
            "Content-Type": "application/json",
            "DD-API-KEY": api_key
        }
        
        response = requests.post(
            DATADOG_LOGS_ENDPOINT,
            headers=headers,
            json=logs_data
        )
        
        logger.info(f"Proxy logs response: {response.status_code}")
        
        return jsonify({
            "status": response.status_code,
            "message": "Logs sent to Datadog",
            "response": response.text
        }), response.status_code
        
    except Exception as e:
        logger.error(f"Error in proxy_logs: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/proxy/metrics', methods=['POST'])
def proxy_metrics():
    """Proxy metrics to Datadog"""
    api_key = get_datadog_api_key()
    if not api_key:
        return jsonify({"error": "Datadog API key not configured"}), 500
    
    try:
        metrics_data = request.json
        logger.info(f"Sending metrics data to Datadog: {json.dumps(metrics_data, indent=2)}")
        
        headers = {
            "Content-Type": "application/json",
            "DD-API-KEY": api_key
        }
        
        response = requests.post(
            DATADOG_METRICS_ENDPOINT,
            headers=headers,
            json=metrics_data
        )
        
        if response.status_code not in (200, 202):
            logger.error(f"Error response from Datadog: {response.text}")
        else:
            logger.info(f"Metrics successfully sent to Datadog: {response.status_code}")
        
        return jsonify({
            "status": response.status_code,
            "message": "Metrics sent to Datadog",
            "response": response.text
        }), response.status_code
        
    except Exception as e:
        logger.error(f"Error in proxy_metrics: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "ok"})

@app.route('/')
def index():
    """Serve the index.html file"""
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    # Check for API key on startup
    if not get_datadog_api_key():
        logger.warning("DD_API_KEY not set. Please set this environment variable.")
        logger.warning("Example: export DD_API_KEY=your_api_key_here")
    
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
    logger.info(f"Server running on port {port}")

