from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))

PERISKOPE_API_KEY = os.getenv("PERISKOPE_API_KEY")
PERISKOPE_SIGNING_KEY = os.getenv("PERISKOPE_SIGNING_KEY")
PERISKOPE_WORKSPACE_ID = os.getenv("PERISKOPE_WORKSPACE_ID")

HERMES_URL = os.getenv("HERMES_URL")