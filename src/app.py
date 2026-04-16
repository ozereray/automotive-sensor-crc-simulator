from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import os
import sys

# --- VERCEL PATH- & IMPORT-KORREKTUREN ---
# Ermittelt das absolute Verzeichnis dieser Datei (src), damit Vercel die Pfade korrekt auflöst.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Fügt das src-Verzeichnis zum Python-Pfad hinzu, damit lokale Module gefunden werden.
sys.path.append(BASE_DIR)

# Definiert den absoluten Pfad zum templates-Ordner für Jinja2.
templates_dir = os.path.join(BASE_DIR, "templates")
# ----------------------------------------

# Nun können die lokalen Module sicher importiert werden
from crc_engine import CRCEngine
from channel import ChannelSimulator

# Initialisierung der FastAPI-Anwendung für das Dashboard
app = FastAPI(title="Automotive Sensor Simulator")

# Konfiguration der Template-Engine (Jinja2) für das Frontend mit dem absoluten Pfad
templates = Jinja2Templates(directory=templates_dir)

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """
    Rendert die Hauptseite des Dashboards (index.html).
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/simulate")
def simulate(data: str = "1001110110101100", poly: str = "1001", error_length: int = 3):
    """
    Führt die CRC-Simulation über eine REST-API aus und gibt das Ergebnis als JSON zurück.
    
    Parameter:
    - data: Die ursprünglichen Sensordaten (Nutzdaten).
    - poly: Das Generatorpolynom (z.B. 1001 für x^3+1).
    - error_length: Die Länge des Burst-Fehlers, der durch EMI verursacht wird.
    """
    crc = CRCEngine(polynomial=poly)
    
    # 1. Phase: Encode (CRC-Bits berechnen und an den Frame anhängen)
    encoded_frame = crc.encode(data)
    
    # 2. Phase: Kanal (Elektromagnetische Interferenz / EMI simulieren)
    received_frame = ChannelSimulator.inject_burst_error(encoded_frame, error_length=error_length)
    
    # 3. Phase: Decode (Fehlerprüfung auf der Empfängerseite)
    is_valid = crc.check(received_frame)
    
    return {
        "sensor_data": data,
        "encoded_frame": encoded_frame,
        "received_frame": received_frame,
        "is_valid": is_valid,
        "error_injected": encoded_frame != received_frame
    }

if __name__ == "__main__":
    # Startet den lokalen Uvicorn-Server für die Entwicklung
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)