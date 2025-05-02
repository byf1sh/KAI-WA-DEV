from flask import request, jsonify, send_from_directory, render_template_string
from services.excel_service import save_to_excel
import os
from dotenv import load_dotenv

load_dotenv()

last_updated = ""

def register_routes(app):
    @app.route('/receive', methods=['POST'])
    def receive_post():
        global last_updated
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON received'}), 400

        last_updated = data[-1].get("timestamp", "")
        save_to_excel(data)
        return jsonify({'status': 'Data received and saved to Excel'}), 200

    @app.route('/')
    def index():
        return render_template_string('''
            <!DOCTYPE html>
            <html>
            <head><title>Download Excel</title></head>
            <body>
                <h2>Download File Excel : last updated : {{ last_updated }}</h2>
                <a href="/excel" download>
                    <button>Download output.xlsx</button>
                </a>
            </body>
            </html>
        ''', last_updated=last_updated)

    @app.route('/excel')
    def download_excel():
        return send_from_directory(os.getenv('ONEDRIVE_DIR'), 'KAI_WA_TRACKING.xlsx', as_attachment=True)
