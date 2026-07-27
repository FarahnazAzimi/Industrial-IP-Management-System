import subprocess
import os
import getpass
import datetime
import pyodbc
import threading

def log_program_usage(program_name, program_path, username, launch_time):
    try:
        # اجرای برنامه
        process = subprocess.Popen([program_path])
        
        # صبر تا زمانی که برنامه بسته شود
        process.wait()
        
        # محاسبه مدت استفاده
        duration = int((datetime.datetime.now() - launch_time).total_seconds())
        
        # اتصال و درج اطلاعات در SQL
        conn = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=DESKTOP-HFNC2CB\SQLEXPRESS;'
            'DATABASE=LABVIEW;'
            'Trusted_Connection=yes;'
        )
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO ProgramLog (ProgramName, Username, LaunchTime, DurationSeconds)
            VALUES (?, ?, ?, ?)
        ''', (program_name, username, launch_time, duration))

        conn.commit()
        conn.close()
        
    except Exception as e:
        print(f"Error logging usage for {program_name}: {str(e)}")


def launch_program_and_log(program_name):
    # مسیرهای برنامه‌ها
    program_paths = {
        "Arduino": r"F:\APP\ARDUINO.2.3.4.Portable.x64_YasDL.com\Arduino IDE.exe",
        "Word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
        "Excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
    }

    if program_name not in program_paths:
        return f"Error: Unknown program '{program_name}'"

    program_path = program_paths[program_name]
    username = getpass.getuser()
    launch_time = datetime.datetime.now()

    try:
        # اجرای ترد لاگ‌گیری به صورت جدا
        threading.Thread(target=log_program_usage, args=(program_name, program_path, username, launch_time)).start()
        return f"Success: {program_name} launched successfully."  # فوراً ریترن کن

    except Exception as e:
        return f"Error: {str(e)}"
