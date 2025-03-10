# Snapfs Realm

# TODO: Datenstruktur für Konten

# TODO: Funktion zum Einzahlen

# TODO: Funktion zum Abheben

# TODO: Getter-Funktion für Kontostand


import sqlite3

class Konto:
    def __init__(self, konto_nummer, konto_halter, guthaben=0.0, passwort="", geburtsjahr=""):
        """
        Erstellung eines Kontos mit Kontonummer, Inhaber, Guthaben und Passwort
        wenn benötigt kann auch ein Unterkonto erstellt werden.
        """
        self.Konto_nummer = konto_nummer
        self.Konto_halter = konto_halter
        self.Guthaben = guthaben
        self.Passwort = passwort
        self.Geburtsjahr = geburtsjahr

    

