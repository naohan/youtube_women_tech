# utils.py
import csv
import json
from datetime import datetime

def save_to_csv(filename, data, headers):
    """
    Guarda una lista de diccionarios en un archivo CSV.
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    print(f"✅ Datos guardados en {filename}")

def save_to_json(filename, data):
    """
    Guarda datos en formato JSON.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"✅ Datos guardados en {filename}")

def format_date(iso_date):
    """
    Convierte una fecha ISO 8601 de YouTube a formato legible.
    """
    try:
        return datetime.strptime(iso_date, "%Y-%m-%dT%H:%M:%SZ").strftime("%d-%m-%Y %H:%M")
    except Exception:
        return iso_date
