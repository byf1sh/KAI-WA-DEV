import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def save_to_excel(data, filename=os.getenv("ONEDRIVE_FOLDER")):
    df = pd.DataFrame(data)
    if os.path.exists(filename):
        existing_df = pd.read_excel(filename)
        updated_df = pd.concat([existing_df, df], ignore_index=True)
        updated_df.to_excel(filename, index=False)
    else:
        df.to_excel(filename, index=False)
