from flask import Flask, request, jsonify, render_template
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)


def DoSomething(fileImage):
    return {"status": "success", "filename": fileImage.filename}

@app.route('/', methods=['GET'])
def send_html():
    return render_template('index.html')

@app.route('/process-image', methods=['POST'])
def main_upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    result = DoSomething(file)
    return jsonify({"message": "File uploaded successfully!", "result": result}), 200

# Swagger UI setup
SWAGGER_URL = '/swagger'
API_URL = '/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Handwrite Reader"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

