from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)


#----------------------------------
def DoSomething(fileImage):
    pass                            #main logic
                                    #return json
#-----------------------------------


@app.route('/process_image', methods=['POST'])
def main_upload():
        file = request.files['file']
        if not file:
                return jsonify({'message': 'No file'}), 400

    
        result = DoSomething(file)


        #work with image
        # return result
        
        return jsonify({    #return json data
        'message': 'data'
                }), 200

SWAGGER_URL = '/swagger'
API_URL = '/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Handwrite reader"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
        app.run()


