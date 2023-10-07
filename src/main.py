from flask import Flask, request, make_response
from plivo import plivoxml
import plivo
import os
from dotenv import load_dotenv
from diagnosis import diagnosis_medic 

load_dotenv()

app = Flask(__name__)

# Access the variables from dotenv file
auth_id = os.getenv("auth_id")
auth_token = os.getenv("auth_token")
client = plivo.RestClient(auth_id, auth_token)

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


@app.route('/make_call', methods=['GET'])
def make_outbound_call():
    # Making an Outbound call
    response = client.calls.create(
        from_='441392342326',
        to_='+918978843640',
        answer_url='https://c9d6-106-221-176-87.ngrok.io/answer',
        answer_method='POST'
    )

    return str(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
