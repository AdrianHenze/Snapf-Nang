class Konto:
    def __init__(self, konto_nummer, konto_halter, guthaben=0.0, ober_konto=None):
        """
        Erstellung eines Kontos mit Kontonummer, Inhaber und Guthaben
        wenn benötigt kann auch ein Unterkonto erstellt werden.
        """
        self.Konto_nummer = konto_nummer
        self.Konto_halter = konto_halter
        self.Guthaben = guthaben
        self.Ober_konto = ober_konto

        