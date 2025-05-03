import os
from dotenv import load_dotenv
from services.excel_service import add_to_excel
from services.auth import get_access_token
from services.onedrive import list_onedrive_root_files
load_dotenv()

def start_graph(data):
    APPLICATION_ID = os.getenv("APPLICATION_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    SCOPES = ['User.Read', 'Files.ReadWrite', 'Files.Read']

    try:
        token = get_access_token(APPLICATION_ID, CLIENT_SECRET, SCOPES)
        # list_onedrive_root_files(token)
        add_to_excel(token, data)
    except Exception as e:
        print(f'Error: {e}')