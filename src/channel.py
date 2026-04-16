import random

class ChannelSimulator:
    """Klasse zur Simulation des Übertragungskanals und elektrischer Störungen (z.B. EMI im Fahrzeug)."""
    
    @staticmethod
    def inject_burst_error(data: str, error_length: int) -> str:
        """Erzeugt Burst-Fehler (aufeinanderfolgende Bit-Flips) einer bestimmten Länge."""
        if error_length <= 0 or error_length > len(data):
            return data

        # Wählt einen zufälligen Startindex für den Burst-Fehler
        start_idx = random.randint(0, len(data) - error_length)
        
        data_list = list(data)
        for i in range(start_idx, start_idx + error_length):
            # Invertiert die Bits (Bit-Flip)
            data_list[i] = '1' if data_list[i] == '0' else '0'
            
        return ''.join(data_list)