import requests

from atem.config import QUOTE_API, QUOTE_RANDOM


class Quote:
    def __init__(self):
        self.random_quote = requests.get(f'http://{QUOTE_API}/{QUOTE_RANDOM}')
        pass
    
    def randomQuote(self):
        rq_json = self.random_quote.json()

        return{
            "quote": rq_json["content"],
            "author": rq_json["author"]
        }