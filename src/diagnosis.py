import time
import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
token_hugging_face = os.getenv("token_hugging_face")

headers = {"Authorization": f"Bearer {token_hugging_face}"} #TOKEN HUGGING FACE
API_URL_DIAGNOSTIC = "https://api-inference.huggingface.co/models/abhirajeshbhai/symptom-2-disease-net" 


#Disease prediction model
def diagnostic_medic(voice_text):

    """
    INPUT: PATIENT'S SYMPTOMPS IN A TEXT FORMAT
    
    OUTPUT: PATIENT'S DISEASE
    """

    synthomps = {"inputs": voice_text}

    data = json.dumps(synthomps)

      

    time.sleep(1)

    while True:

        try:

            response = requests.request("POST", API_URL_DIAGNOSTIC, headers=headers, data=data)  

            output = json.loads(response.content.decode("utf-8"))

            final_output = output[0][0]['label']

            break

        except KeyError:

            continue

    return final_output