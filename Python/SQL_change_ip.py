import pyodbc

def log_ip_change(interface_name, new_ip):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-HFNC2CB\SQLEXPRESS;DATABASE=LABVIEW;Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO IP_Changes (interface_name, new_ip) VALUES (?, ?)",
                   interface_name, new_ip)
    conn.commit()
    cursor.close()
    conn.close()
    return "Inserted into DB"
