import os
import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials

load_dotenv()

google_cred = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

def init_firebase():
    cred = credentials.Certificate("path/to/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)