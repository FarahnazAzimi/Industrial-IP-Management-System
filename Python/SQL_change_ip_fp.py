import pyodbc
import ipaddress

def log_ip_change(interface_name, new_ip):
    try:
        # اعتبارسنجی فرمت و بازه IP
        ipaddress.IPv4Address(new_ip)
    except ValueError:
        return f"Invalid IP address: {new_ip}"

    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-HFNC2CB\\SQLEXPRESS;'
            'DATABASE=LABVIEW;'
            'Trusted_Connection=yes;'
        )
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO IP_Changes (interface_name, new_ip) VALUES (?, ?)",
            interface_name, new_ip
        )
        conn.commit()
        cursor.close()
        conn.close()
        return "Inserted into DB"

    except Exception as e:
        return f"Database error: {e}"
