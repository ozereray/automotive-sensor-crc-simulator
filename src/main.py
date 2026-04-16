import logging
from crc_engine import CRCEngine
from channel import ChannelSimulator

# Professionelle Logging-Konfiguration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def main():
    logging.info("Simulation für CRC-Fehlererkennung in autonomen Sensordaten gestartet...")
    
    # Beispieldaten: Rohe Sensordaten (z.B. von einem LiDAR oder einer Kamera)
    sensor_data = "1001110110101100" 
    
    # Generatorpolynom aus der Übungsaufgabe 3.5: C(x) = x^3 + 1 -> Binär: 1001
    generator_poly = "1001" 
    
    crc = CRCEngine(polynomial=generator_poly)
    
    # ---------------------------------------------------------
    # 1. PHASE: SENDER (Sensormodul)
    # ---------------------------------------------------------
    encoded_frame = crc.encode(sensor_data)
    logging.info(f"Ursprüngliche Daten:         {sensor_data}")
    logging.info(f"Zu übertragender Frame:      {encoded_frame}")
    
    # ---------------------------------------------------------
    # 2. PHASE: KANAL (z.B. Automotive Ethernet oder CAN-Bus)
    # ---------------------------------------------------------
    logging.warning("Elektromagnetische Interferenz (EMI) im Kanal erkannt!")
    
    # Wir fügen einen 3-Bit-Burst-Fehler ein, wie in den Vorlesungsunterlagen diskutiert
    received_frame = ChannelSimulator.inject_burst_error(encoded_frame, error_length=3)
    
    logging.info(f"Empfangener Frame (defekt):  {received_frame}")
    
    # ---------------------------------------------------------
    # 3. PHASE: EMPFÄNGER (Hauptprozessor / ECU)
    # ---------------------------------------------------------
    is_valid = crc.check(received_frame)
    
    if is_valid:
        logging.info("✅ ERGEBNIS: Daten erfolgreich verifiziert. Kein Fehler gefunden.")
    else:
        logging.error("❌ ERGEBNIS: CRC-FEHLER ERKANNT! Daten sind fehlerhaft (Frame verworfen).")

if __name__ == "__main__":
    main()