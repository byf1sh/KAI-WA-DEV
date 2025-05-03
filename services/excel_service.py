import requests

def add_to_excel_backup(token, data):
    access_token = token
    file_path = "TRACKING/KAI_WA_TRACKING.xlsx"
    table_name = "Table1"  # pastikan kamu tahu nama table-nya

    url = f"https://graph.microsoft.com/v1.0/me/drive/root:/{file_path}:/workbook/tables/{table_name}/rows/add"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print("✅ Data berhasil ditambahkan.")
    else:
        print("❌ Gagal:", response.status_code, response.text)

def add_to_excel(token, data):
    access_token = token
    file_path = "TRACKING/KAI_WA_TRACKING.xlsx"
    table_name = "Table1"

    url = f"https://graph.microsoft.com/v1.0/me/drive/root:/{file_path}:/workbook/tables/{table_name}/rows/add"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Ubah list of dict jadi list of list
    values = []
    for row in data:
        # Pastikan urutan kolom sesuai dengan urutan kolom di Excel
        values.append([
            row.get("timestamp", ""),
            row.get("message", "")  # hilangkan newline jika ada
        ])

    payload = {"values": values}
    
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("✅ Data berhasil ditambahkan.")
    else:
        print("❌ Gagal:", response.status_code, response.text)
