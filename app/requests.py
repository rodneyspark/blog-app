import requests,json
from .models import Quote

base_url = None

def  configure_request(app):
    global base_url 
    base_url = app.config["QUOTE_URL"]

def get_quotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    if response.status_code == 200:
        quote = response.json()
        return quote
