import os

from dotenv import load_dotenv
load_dotenv()


# Quotes API
QUOTE_API = os.environ.get("QUOTE_API", "<your-api-key>")
QUOTE_RANDOM = os.environ.get("QUOTE_RANDOM", "<your-api-endpoint>")