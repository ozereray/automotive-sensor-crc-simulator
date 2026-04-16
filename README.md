# Automotive Sensor-Daten CRC Simulator

### Echtzeit-Fehlersimulation für Software-Defined Vehicles (SDVs)

## 🚗 Projektübersicht

Dieses Projekt demonstriert die Implementierung der zyklischen Redundanzprüfung (CRC) zur Fehlererkennung in automobilen Sensorsystemen. In modernen Fahrzeugarchitekturen (SDVs) ist die Integrität der Datenübertragung (z. B. über Automotive Ethernet oder CAN-Bus) aufgrund elektromagnetischer Interferenzen (EMI) von kritischer Bedeutung.

## 🛠 Features

- **CRC-Engine:** Implementierung der Modulo-2-Division zur Berechnung von Prüfsummen.
- **EMI-Simulator:** Simulation von Burst-Fehlern (aufeinanderfolgende Bit-Flips), die in realen Fahrzeugumgebungen auftreten können.
- **Interaktives Dashboard:** Eine moderne Weboberfläche zur Visualisierung des Einflusses von Fehlern auf die Datenframes.
- **Enterprise-Logging:** Vollständige Protokollierung der Sende- und Empfangsprozesse.

## 📚 Fachlicher Hintergrund

Das System verwendet ein frei wählbares Generatorpolynom (Standard: $C(x) = x^3 + 1$). Es zeigt auf, wie Burst-Fehler einer bestimmten Länge erkannt werden und fehlerhafte Frames automatisch verworfen werden, um die funktionale Sicherheit (Functional Safety) des Fahrzeugs zu gewährleisten.

## 🚀 Installation & Ausführung

1. Repository klonen:
   `git clone https://github.com/ozereray/automotive-sensor-crc-simulator.git`
2. Abhängigkeiten installieren:
   `pip install -r requirements.txt`
3. Server starten:
   `uvicorn src.app:app --reload`

## 👨‍💻 Autor

Eray Özer - Hochschule Trier
