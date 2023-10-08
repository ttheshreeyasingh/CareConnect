from flask import Flask, request, make_response
from plivo import plivoxml
from flask_cors import CORS
import plivo
import os
from dotenv import load_dotenv
from diagnosis import diagnosis_medic 

load_dotenv()

app = Flask(__name__)
CORS(app)
# Access the variables from dotenv file
auth_id = os.getenv("auth_id")
auth_token = os.getenv("auth_token")
ngrok_url = os.getenv("ngrok_url")
client = plivo.RestClient(auth_id, auth_token)

@app.route('/')
def index():
    return "Welcome to CareConnect"

@app.route('/handle_speech', methods=['POST'])
def handle_speech():
    input_text = request.form.get('Speech')
    
    if input_text:
        diagnosis = diagnosis_medic(input_text)
        print(f"the diagnosis is {diagnosis}")
        xml_response = f'''
        <Response>
            <Speak language = "en-US">Based on your symptoms, it appears you may have {diagnosis}. </Speak>
        </Response>
        '''
    else:
        xml_response = '''
        <Response>
            <Speak language = "en-US">Sorry, I couldn't understand your symptoms.</Speak>
        </Response>
        '''
    
    response = make_response(xml_response)
    response.headers['Content-Type'] = 'text/xml'
    
    return response


@app.route('/answer', methods=['POST'])
def answer_call():
    
    xml_file_path = '../templates/response.xml'

    with open(xml_file_path, 'r') as file:
        xml_response = file.read()

    response = make_response(xml_response)
    response.headers['Content-Type'] = 'text/xml'
    
    return response

@app.route('/make_call', methods=['POST'])
def make_outbound_call():
    phone_number = request.json.get('phone_number')

     # Making an Outbound call
    response = client.calls.create(
        from_='441392342326',
        to_=phone_number,
        answer_url=ngrok_url+'/answer',
        answer_method='POST'
    )
    print(response)


    return {
        'message': 'Call has been made'
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
