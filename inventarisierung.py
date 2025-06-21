import os
import platform
import socket
import uuid
import json
import psutil
import winreg
import requests
import wmi
from getmac import get_mac_address

WEBHOOK_URL = "xxxxxxxxx"

# Benutzer auslesen
def get_username():
    username = os.getenv("USERNAME")
    if username and "." in username:
        parts = username.split(".")
        return f"{parts[1]}, {parts[0]}".title()
    return "N/A"

def get_user_accounts():
    user_dir = "C:/Users"
    users = []
    last_user = None
    last_time = 0

    if not os.path.exists(user_dir):
        return users, "N/A"

    for name in os.listdir(user_dir):
        path = os.path.join(user_dir, name)
        if not os.path.isdir(path):
            continue
        if name in {"Public", "All Users", "defaultuser0", "SimpleDA"} or name.startswith("$"):
            continue

        users.append(name)
        modified_time = os.path.getmtime(path)
        if modified_time > last_time:
            last_user = name
            last_time = modified_time

    formatted_last_user = (
        f"{last_user.split('.')[1]}, {last_user.split('.')[0]}".title()
        if last_user and '.' in last_user else "N/A"
    )

    return users, formatted_last_user

# Hardware auslesen
def get_hardware_info():
    try:
        wmi_conn = wmi.WMI()
        system = wmi_conn.Win32_ComputerSystem()[0]
        bios = wmi_conn.Win32_BIOS()[0]
        return bios.SerialNumber, system.Model
    except Exception as e:
        print(f"[Fehler] WMI-Fehler: {e}")
        return "N/A", "N/A"

def get_ram_info():
    total_ram = psutil.virtual_memory().total
    return f"{(total_ram // (1024 ** 3)) + 1} GB"

def get_drive_info():
    drives = []
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            drives.append(
                f"{partition.device} Total: {usage.total // (1024 ** 3)} GB. "
                f"Frei: {usage.free // (1024 ** 3)} GB"
            )
        except Exception:
            continue
    return drives

# Software auslesen
def get_installed_software():
    software = []
    try:
        with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
        ) as key:
            for i in range(winreg.QueryInfoKey(key)[0]):
                try:
                    subkey_name = winreg.EnumKey(key, i)
                    with winreg.OpenKey(key, subkey_name) as subkey:
                        name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                        software.append(name)
                except Exception:
                    continue
    except Exception as e:
        print(f"[Fehler] Registry-Zugriff fehlgeschlagen: {e}")
    return software

# Netzwerk auslesen
def get_network_info():
    return {
        "Computername": socket.gethostname(),
        "Betriebssystem": platform.platform(),
        "IP-Adresse": socket.gethostbyname(socket.getfqdn()),
        "MAC-Adresse": get_mac_address(),
        "HWID": f"HWID: {uuid.getnode()}",
    }

# Zusammenführen der Daten
def collect_system_info():
    serial_number, model = get_hardware_info()
    users, last_user = get_user_accounts()

    info = {
        "Seriennummer": serial_number,
        "Model": model,
        "RAM": get_ram_info(),
        "Laufwerke": get_drive_info(),
        "Benutzer": users,
        "Letzter Benutzer": last_user or get_username(),
        "Software": get_installed_software()
    }

    info.update(get_network_info())
    return info

# An den Webhook senden
def send_to_webhook(data, url):
    try:
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )
        response.raise_for_status()
        print("[OK] Systeminfo erfolgreich gesendet.")
    except requests.RequestException as err:
        print(f"[Fehler] Webhook-Senden fehlgeschlagen: {err}")

# Main
if __name__ == "__main__":
    system_info = collect_system_info()
    send_to_webhook(system_info, WEBHOOK_URL)
