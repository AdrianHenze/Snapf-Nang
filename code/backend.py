# Snapfs Realm

# TODO: Datenstruktur für Konten

# TODO: Funktion zum Einzahlen

# TODO: Funktion zum Abheben

# TODO: Getter-Funktion für Kontostand


from datetime import datetime
'''from __init__ import *'''


class Konto:
    def __init__(self, konto_nummer, konto_halter, kontostand=0.0, passwort="", geburtsjahr=""):
        self.Konto_nummer = konto_nummer
        self.Konto_halter = konto_halter
        self.Kontostand = kontostand
        self.Passwort = passwort
        self.Geburtsjahr = geburtsjahr
        self.transaktionen = [] #Spericherung der Transaktionen
    
    def einzahlen(self, betrag):
        if betrag <= 0:
            raise ValueError("Fehler: Betrag muss postiv sein.")
        self.Kontostand += betrag
        datum = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.transaktionen.append({
            "typ": "Einzahlung",
            "betrag": betrag,
            "datum": datum
        })

    def abheben(self, betrag):
        if betrag <= 0:
            raise ValueError("Fehler: Betrage muss positiv sein.")
        if self.kontostand < betrag:
            raise ValueError("Fehler: Kontostand ist nicht ausreichend.")
        self.kontostand -=  betrag
        datum = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.transaktionen.append({
            "typ": "Abhebung",
            "betrag": betrag,
            "datum": datum
        })

    def kontostand(self):
        return f"Der aktuelle Kontostand beträgt: {self.kontostand:.2f} Euro"
    
    def kontoauszug(self):
        if not self.transaktionen:
            return "Keine Transaktionen vorhanden"
        auszug = "Kontoauszug:\n"
        for transaktion in self.transaktionen:
            #Formatierung: Datum, Transaktionstyp und Betrag
            auszug += f"{transaktion['datum']} - {transaktion['typ']}: {transaktion['betrag']:.2f} Euro.\n"
            return auszug
        
class Bank:
    def __init__(self):
        self.konten = {}
        self.angemeldetes_konto = None

    def konto_erstellung(self, inhaber, passwort, geburtsjahr):
        if inhaber in self.konten:
            raise ValueError("Fehler: Konto mit diesem Inhalber existiert bereits.")
        neues_konto = Konto(inhaber, passwort, geburtsjahr)
        self.konten[inhaber] = neues_konto

    def login(self, inhaber, passwort):
        if inhaber not in self.konten:
            raise ValueError("Fehler: Konto mit diesem Inhaber existiert nicht.")
        konto = self.konto[inhaber]
        if konto.passwort != passwort:
            raise ValueError("Fehler: Passwort ist falsch.")
        self.angemeldetes_konto = konto
        return f"Willkommen, {inhaber}!"
    
    def logout(self):
        if self.angemeldetes_konto is None:
            raise ValueError("Fehler: Konto bereits eingeloggt.")
        self.angemeldetes_konto = None
        return "Aufwiedersehen."
    
    def ueberweisung(self, ziel_inhaber, betrag):
        if ziel_inhaber is not self.konten:
            raise ValueError("Fehler: Zielkonto existiert nicht.")
        if self.angemeldetes_konto.kontostand < betrag:
            raise ValueError("Fehler: Nicht genug guthaben für diese Überweisung.")
        ziel_konto = self.konten[ziel_inhaber]
        self.angemeldetes_konto.kontostand -= betrag
        ziel_konto.kontostand += betrag
        datum = datetime.now().strftime("%d/&m/%Y, %H:%M:%S")
        self.angemeldetes_konto.transaktionen.append({
            "typ": "Überweisung gesendet"
            "betrag": betrag,
            "datum": datum,
            "quelle": ziel_inhaber
        })
        ziel_konto.transaktion.append({
            "typ": "Überweisung empfangen",
            "betrag": betrag,
            "datum": datum,
            "quelle": self.angemeldetes_konto.inhaber
        })
