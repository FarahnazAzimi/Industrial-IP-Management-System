# upload_image.py

import pyodbc
import os
import datetime

def upload_image(file_path):
    if not os.path.exists(file_path):
        return "File not found."

    file_size_kb = os.path.getsize(file_path) // 1024
    upload_time = datetime.datetime.now()

    with open(file_path, 'rb') as f:
        image_data = f.read()

    conn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=DESKTOP-HFNC2CB\SQLEXPRESS;DATABASE=LABVIEW;Trusted_Connection=yes;'
    )
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO ImageLog (FilePath, FileSizeKB, UploadTime, ImageData)
        VALUES (?, ?, ?, ?)
    """, (file_path, file_size_kb, upload_time, image_data))

    conn.commit()
    conn.close()

    return "Upload successful."
