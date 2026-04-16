class CRCEngine:
    """CRC (Cyclic Redundancy Check) Berechnungsmodul für automobile Sensordaten."""
    
    def __init__(self, polynomial: str):
        self.poly = polynomial
        self.poly_len = len(polynomial)

    def _xor(self, a: str, b: str) -> str:
        """Führt eine bitweise XOR-Operation zwischen zwei binären Strings aus."""
        result = []
        for i in range(1, len(b)):
            result.append('0' if a[i] == b[i] else '1')
        return ''.join(result)

    def _mod2div(self, dividend: str) -> str:
        """Führt eine Modulo-2-Division aus, um den Rest (Remainder) zu berechnen."""
        pick = self.poly_len
        tmp = dividend[0:pick]

        while pick < len(dividend):
            if tmp[0] == '1':
                tmp = self._xor(self.poly, tmp) + dividend[pick]
            else:
                tmp = self._xor('0' * pick, tmp) + dividend[pick]
            pick += 1

        if tmp[0] == '1':
            tmp = self._xor(self.poly, tmp)
        else:
            tmp = self._xor('0' * pick, tmp)

        return tmp

    def encode(self, data: str) -> str:
        """Hängt die berechneten CRC-Bits an die Nutzdaten an (erstellt den Frame)."""
        appended_data = data + '0' * (self.poly_len - 1)
        remainder = self._mod2div(appended_data)
        return data + remainder

    def check(self, received_data: str) -> bool:
        """Überprüft die Integrität der empfangenen Daten. Gibt True zurück, wenn fehlerfrei."""
        remainder = self._mod2div(received_data)
        return '1' not in remainder