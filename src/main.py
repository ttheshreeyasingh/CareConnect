import plivo
import os
from dotenv import load_dotenv

load_dotenv()
# Access the variables
auth_id = os.getenv("auth_id")
auth_token = os.getenv("auth_token")

client = plivo.RestClient(auth_id, auth_token)

# Searching for a Number
# response = client.numbers.search(country_iso='GB')

# Renting a number
# response = client.numbers.buy(number='441392342326')
  
# Making an Outbound call
response = client.calls.create(
    from_='441392342326',
    to_='+918978843640',
    answer_url='https://s3.amazonaws.com/static.plivo.com/answer.xml',
    answer_method='GET'
)

print(response)
